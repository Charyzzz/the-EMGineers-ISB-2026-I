"""
plotear_emg.py
==============
Script standalone para plotear señales EMG fusionadas (derecho + izquierdo)
sin necesidad de Streamlit. Sigue la arquitectura modular de la app.

Uso:
    python plotear_emg.py <archivo_emg_fusionado.txt>
"""

import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# CONFIGURACIÓN (igual a config.py de la app)
# ============================================================================
FS_HZ = 1000
HEADER_LINES = 3
COL_NSEQ = 0
COL_A1 = 5   # Trapecio Derecho
COL_A2 = 6   # Trapecio Izquierdo

# Conversión ADC -> mV
ADC_N_BITS = 10
ADC_VCC = 3.3
EMG_GAIN = 1009.0
UNIDAD_SENAL = "mV"

# Colores
COLOR_DERECHO = "#1F4E79"     # azul acero oscuro
COLOR_IZQUIERDO = "#8C1D18"   # granate oscuro
COLOR_NEUTRO = "#4B5563"      # gris pizarra

CANAL_DERECHO = "Trapecio Derecho (A1)"
CANAL_IZQUIERDO = "Trapecio Izquierdo (A2)"


# ============================================================================
# FUNCIONES DE CONVERSIÓN (igual a lectura.py)
# ============================================================================
def adc_a_mv(
    valores_adc: np.ndarray,
    n_bits: int = ADC_N_BITS,
    vcc: float = ADC_VCC,
    ganancia: float = EMG_GAIN,
) -> np.ndarray:
    """Convierte cuentas ADC crudas a milivoltios."""
    resolucion = 2 ** n_bits
    voltios = ((valores_adc / resolucion) - 0.5) * vcc / ganancia
    return voltios * 1000.0  # V -> mV


# ============================================================================
# LECTURA DE ARCHIVO
# ============================================================================
def leer_emg_fusionado(ruta_archivo: Path) -> dict:
    """
    Lee un archivo EMG fusionado generado por merge_opensignals.py
    
    Retorna un diccionario con:
    - tiempo: vector de tiempo en segundos
    - canal_derecho: señal A1 en mV
    - canal_izquierdo: señal A2 en mV
    - fs: frecuencia de muestreo
    - n_muestras: cantidad de muestras
    - duracion_segundos: duración total
    """
    if not ruta_archivo.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta_archivo}")
    
    # Leer datos (saltando las 3 líneas de cabecera)
    datos = np.loadtxt(ruta_archivo, skiprows=HEADER_LINES)
    
    if datos.ndim == 1:
        datos = datos.reshape(1, -1)
    
    # Extraer canales A1 y A2
    canal_derecho = adc_a_mv(datos[:, COL_A1].astype(float))
    canal_izquierdo = adc_a_mv(datos[:, COL_A2].astype(float))
    
    # Generar vector de tiempo
    n_muestras = len(canal_derecho)
    tiempo = np.arange(n_muestras) / FS_HZ
    
    return {
        "tiempo": tiempo,
        "canal_derecho": canal_derecho,
        "canal_izquierdo": canal_izquierdo,
        "fs": FS_HZ,
        "n_muestras": n_muestras,
        "duracion_segundos": n_muestras / FS_HZ,
    }


# ============================================================================
# FUNCIONES DE FILTRADO (igual a filtros.py)
# ============================================================================
def rectificar_onda_completa(senal: np.ndarray) -> np.ndarray:
    """Aplica rectificación de onda completa."""
    return np.abs(senal)


def filtro_pasa_banda(
    senal: np.ndarray,
    fs: int,
    f_baja: float = 20.0,
    f_alta: float = 450.0,
    orden: int = 4,
) -> np.ndarray:
    """Aplica filtro pasa banda Butterworth."""
    from scipy import signal
    
    nyquist = fs / 2.0
    f_alta_segura = min(f_alta, nyquist * 0.99)
    f_baja_segura = max(f_baja, 0.1)
    
    sos = signal.butter(
        orden,
        [f_baja_segura, f_alta_segura],
        btype="bandpass",
        fs=fs,
        output="sos",
    )
    return signal.sosfiltfilt(sos, senal)


def filtro_notch(
    senal: np.ndarray,
    fs: int,
    f_notch: float = 60.0,
    q: float = 30.0,
) -> np.ndarray:
    """Aplica filtro notch (rechaza 60 Hz)."""
    from scipy import signal
    
    b, a = signal.iirnotch(f_notch, q, fs)
    return signal.filtfilt(b, a, senal)


def aplicar_pipeline(
    senal: np.ndarray,
    fs: int,
    usar_rectificacion: bool = False,
    usar_pasa_banda: bool = False,
    usar_notch: bool = False,
    f_baja: float = 20.0,
    f_alta: float = 450.0,
    orden_pasa_banda: int = 4,
    f_notch: float = 60.0,
    q_notch: float = 30.0,
) -> np.ndarray:
    """Aplica secuencialmente los filtros seleccionados."""
    senal_procesada = senal.copy()
    
    if usar_pasa_banda:
        senal_procesada = filtro_pasa_banda(
            senal_procesada, fs, f_baja=f_baja, f_alta=f_alta, orden=orden_pasa_banda
        )
    
    if usar_notch:
        senal_procesada = filtro_notch(senal_procesada, fs, f_notch=f_notch, q=q_notch)
    
    if usar_rectificacion:
        senal_procesada = rectificar_onda_completa(senal_procesada)
    
    return senal_procesada


# ============================================================================
# FUNCIONES DE ESTADÍSTICAS
# ============================================================================
def calcular_estadisticas(senal: np.ndarray) -> dict:
    """Calcula estadísticos descriptivos de la señal."""
    return {
        "media": float(np.mean(senal)),
        "mediana": float(np.median(senal)),
        "std": float(np.std(senal)),
        "max": float(np.max(senal)),
        "min": float(np.min(senal)),
        "rms": float(np.sqrt(np.mean(np.square(senal)))),
        "mav": float(np.mean(np.abs(senal))),
        "varianza": float(np.var(senal)),
        "energia": float(np.sum(np.square(senal))),
    }


def calcular_asimetria(rms_derecho: float, rms_izquierdo: float) -> dict:
    """Calcula el índice de asimetría bilateral."""
    promedio = (rms_derecho + rms_izquierdo) / 2.0
    
    if promedio == 0:
        indice = 0.0
    else:
        indice = abs(rms_derecho - rms_izquierdo) / promedio * 100.0
    
    # Clasificación
    if indice <= 10.0:
        clasificacion = "Simetría adecuada"
    elif indice <= 20.0:
        clasificacion = "Asimetría leve"
    elif indice <= 40.0:
        clasificacion = "Asimetría moderada"
    else:
        clasificacion = "Asimetría severa"
    
    return {
        "indice": indice,
        "clasificacion": clasificacion,
    }


# ============================================================================
# GRÁFICOS
# ============================================================================
def crear_figura_individual(tiempo, senal, nombre_canal, color, unidad=UNIDAD_SENAL):
    """Crea una figura para un único canal."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(tiempo, senal, color=color, linewidth=0.8, label=nombre_canal)
    ax.set_xlabel("Tiempo (s)", fontsize=11)
    ax.set_ylabel(f"Amplitud ({unidad})", fontsize=11)
    ax.set_title(f"Señal EMG - {nombre_canal}", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")
    return fig, ax


def crear_figura_comparativa(tiempo, senal_derecha, senal_izquierda, unidad=UNIDAD_SENAL):
    """Crea una figura comparativa (ambos canales superpuestos)."""
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(tiempo, senal_derecha, color=COLOR_DERECHO, linewidth=0.8, label=CANAL_DERECHO, alpha=0.8)
    ax.plot(tiempo, senal_izquierda, color=COLOR_IZQUIERDO, linewidth=0.8, label=CANAL_IZQUIERDO, alpha=0.8)
    ax.set_xlabel("Tiempo (s)", fontsize=11)
    ax.set_ylabel(f"Amplitud ({unidad})", fontsize=11)
    ax.set_title("Comparación bilateral: Trapecio Derecho vs. Izquierdo", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")
    return fig, ax


def crear_figura_sincronizada(tiempo, senal_derecha, senal_izquierda, unidad=UNIDAD_SENAL):
    """Crea dos subgráficos sincronizados (apilados)."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)
    
    # Canal derecho
    ax1.plot(tiempo, senal_derecha, color=COLOR_DERECHO, linewidth=0.8)
    ax1.set_ylabel(f"Amplitud ({unidad})", fontsize=11)
    ax1.set_title(CANAL_DERECHO, fontsize=12, fontweight="bold")
    ax1.grid(True, alpha=0.3)
    
    # Canal izquierdo
    ax2.plot(tiempo, senal_izquierda, color=COLOR_IZQUIERDO, linewidth=0.8)
    ax2.set_xlabel("Tiempo (s)", fontsize=11)
    ax2.set_ylabel(f"Amplitud ({unidad})", fontsize=11)
    ax2.set_title(CANAL_IZQUIERDO, fontsize=12, fontweight="bold")
    ax2.grid(True, alpha=0.3)
    
    fig.suptitle("Comparación sincronizada entre canales", fontsize=13, fontweight="bold")
    plt.tight_layout()
    return fig, (ax1, ax2)


def crear_figura_barras_rms(rms_derecho, rms_izquierdo, unidad=UNIDAD_SENAL):
    """Crea un gráfico de barras comparando RMS."""
    fig, ax = plt.subplots(figsize=(8, 5))
    canales = [CANAL_DERECHO, CANAL_IZQUIERDO]
    valores = [rms_derecho, rms_izquierdo]
    colores = [COLOR_DERECHO, COLOR_IZQUIERDO]
    
    barras = ax.bar(canales, valores, color=colores, alpha=0.7, edgecolor='black', linewidth=1.5)
    
    # Agregar etiquetas en las barras
    for barra, valor in zip(barras, valores):
        height = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2., height,
                f'{valor:.3f}', ha='center', va='bottom', fontsize=10, fontweight='bold')
    
    ax.set_ylabel(f"RMS ({unidad})", fontsize=11)
    ax.set_title(f"RMS por canal ({unidad})", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3, axis='y')
    plt.tight_layout()
    return fig, ax


def crear_figura_espectral_fft(tiempo, senal_derecha, senal_izquierda, fs):
    """Crea FFT para ambos canales."""
    from scipy import signal as sp_signal
    
    # Calcular FFT
    n_derecho = len(senal_derecha)
    fft_derecho = np.fft.rfft(senal_derecha)
    freqs = np.fft.rfftfreq(n_derecho, d=1.0 / fs)
    mag_derecho = np.abs(fft_derecho) / n_derecho
    mag_derecho[1:] *= 2
    
    n_izquierdo = len(senal_izquierda)
    fft_izquierdo = np.fft.rfft(senal_izquierda)
    mag_izquierdo = np.abs(fft_izquierdo) / n_izquierdo
    mag_izquierdo[1:] *= 2
    
    # Plotear
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7))
    
    ax1.plot(freqs, mag_derecho, color=COLOR_DERECHO, linewidth=0.8)
    ax1.set_ylabel(f"Magnitud ({UNIDAD_SENAL})", fontsize=11)
    ax1.set_title(f"Espectro FFT - {CANAL_DERECHO}", fontsize=12, fontweight="bold")
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim(0, 500)
    
    ax2.plot(freqs, mag_izquierdo, color=COLOR_IZQUIERDO, linewidth=0.8)
    ax2.set_xlabel("Frecuencia (Hz)", fontsize=11)
    ax2.set_ylabel(f"Magnitud ({UNIDAD_SENAL})", fontsize=11)
    ax2.set_title(f"Espectro FFT - {CANAL_IZQUIERDO}", fontsize=12, fontweight="bold")
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim(0, 500)
    
    plt.tight_layout()
    return fig, (ax1, ax2)


def crear_figura_espectrograma(tiempo, senal_derecha, senal_izquierda, fs):
    """Crea espectrogramas (STFT) para ambos canales."""
    from scipy import signal as sp_signal
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Espectrograma derecho
    f, t, sxx_d = sp_signal.spectrogram(senal_derecha, fs=fs, nperseg=256, noverlap=128)
    im1 = ax1.pcolormesh(t, f, 10 * np.log10(sxx_d + 1e-12), shading='gouraud', cmap='gray')
    ax1.set_ylabel("Frecuencia (Hz)", fontsize=11)
    ax1.set_title(f"Espectrograma - {CANAL_DERECHO}", fontsize=12, fontweight="bold")
    ax1.set_ylim(0, 500)
    cbar1 = plt.colorbar(im1, ax=ax1)
    cbar1.set_label("dB", fontsize=10)
    
    # Espectrograma izquierdo
    f, t, sxx_i = sp_signal.spectrogram(senal_izquierda, fs=fs, nperseg=256, noverlap=128)
    im2 = ax2.pcolormesh(t, f, 10 * np.log10(sxx_i + 1e-12), shading='gouraud', cmap='gray')
    ax2.set_xlabel("Tiempo (s)", fontsize=11)
    ax2.set_ylabel("Frecuencia (Hz)", fontsize=11)
    ax2.set_title(f"Espectrograma - {CANAL_IZQUIERDO}", fontsize=12, fontweight="bold")
    ax2.set_ylim(0, 500)
    cbar2 = plt.colorbar(im2, ax=ax2)
    cbar2.set_label("dB", fontsize=10)
    
    plt.tight_layout()
    return fig, (ax1, ax2)


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
def main():
    """Función principal que coordina la lectura y ploteo."""
    
    # Obtener archivo de entrada
    if len(sys.argv) < 2:
        print("Uso: python plotear_emg.py <archivo_emg_fusionado.txt>")
        print("\nEjemplos:")
        print("  python plotear_emg.py basal_trapecio_merged.txt")
        sys.exit(1)
    
    archivo = Path(sys.argv[1])
    
    print(f"📂 Leyendo archivo: {archivo.name}")
    senal = leer_emg_fusionado(archivo)
    print(f"✓ Duración: {senal['duracion_segundos']:.2f} segundos")
    print(f"✓ Muestras: {senal['n_muestras']}")
    print(f"✓ Frecuencia: {senal['fs']} Hz\n")
    
    # Aplicar filtros (configurable)
    print("⚙️  Aplicando pipeline de filtrado...")
    canal_derecho_procesado = aplicar_pipeline(
        senal["canal_derecho"],
        senal["fs"],
        usar_pasa_banda=True,
        usar_notch=True,
        usar_rectificacion=False,
    )
    canal_izquierdo_procesado = aplicar_pipeline(
        senal["canal_izquierdo"],
        senal["fs"],
        usar_pasa_banda=True,
        usar_notch=True,
        usar_rectificacion=False,
    )
    print("✓ Filtrado completado\n")
    
    # Calcular estadísticas
    print("📊 Calculando estadísticas...")
    stats_derecho = calcular_estadisticas(canal_derecho_procesado)
    stats_izquierdo = calcular_estadisticas(canal_izquierdo_procesado)
    
    print(f"\n{'Trapecio Derecho (A1)':^40}")
    print(f"  RMS: {stats_derecho['rms']:.4f} {UNIDAD_SENAL}")
    print(f"  Media: {stats_derecho['media']:.4f} {UNIDAD_SENAL}")
    print(f"  Máx: {stats_derecho['max']:.4f} {UNIDAD_SENAL}")
    
    print(f"\n{'Trapecio Izquierdo (A2)':^40}")
    print(f"  RMS: {stats_izquierdo['rms']:.4f} {UNIDAD_SENAL}")
    print(f"  Media: {stats_izquierdo['media']:.4f} {UNIDAD_SENAL}")
    print(f"  Máx: {stats_izquierdo['max']:.4f} {UNIDAD_SENAL}")
    
    # Calcular asimetría
    asimetria = calcular_asimetria(stats_derecho['rms'], stats_izquierdo['rms'])
    print(f"\n{'Asimetría Bilateral':^40}")
    print(f"  Índice: {asimetria['indice']:.2f}%")
    print(f"  Clasificación: {asimetria['clasificacion']}\n")
    
    # Crear figuras
    print("📈 Generando gráficos...")
    
    # 1. Canal derecho
    fig1, _ = crear_figura_individual(
        senal["tiempo"], canal_derecho_procesado, CANAL_DERECHO, COLOR_DERECHO
    )
    fig1.savefig("01_canal_derecho.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 01_canal_derecho.png")
    
    # 2. Canal izquierdo
    fig2, _ = crear_figura_individual(
        senal["tiempo"], canal_izquierdo_procesado, CANAL_IZQUIERDO, COLOR_IZQUIERDO
    )
    fig2.savefig("02_canal_izquierdo.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 02_canal_izquierdo.png")
    
    # 3. Comparativa superpuesta
    fig3, _ = crear_figura_comparativa(
        senal["tiempo"], canal_derecho_procesado, canal_izquierdo_procesado
    )
    fig3.savefig("03_comparativa_superpuesta.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 03_comparativa_superpuesta.png")
    
    # 4. Comparativa sincronizada (apilada)
    fig4, _ = crear_figura_sincronizada(
        senal["tiempo"], canal_derecho_procesado, canal_izquierdo_procesado
    )
    fig4.savefig("04_comparativa_sincronizada.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 04_comparativa_sincronizada.png")
    
    # 5. Barras RMS
    fig5, _ = crear_figura_barras_rms(stats_derecho['rms'], stats_izquierdo['rms'])
    fig5.savefig("05_barras_rms.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 05_barras_rms.png")
    
    # 6. FFT
    fig6, _ = crear_figura_espectral_fft(
        senal["tiempo"], canal_derecho_procesado, canal_izquierdo_procesado, senal["fs"]
    )
    fig6.savefig("06_espectro_fft.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 06_espectro_fft.png")
    
    # 7. Espectrograma
    fig7, _ = crear_figura_espectrograma(
        senal["tiempo"], canal_derecho_procesado, canal_izquierdo_procesado, senal["fs"]
    )
    fig7.savefig("07_espectrograma.png", dpi=100, bbox_inches='tight')
    print("✓ Guardado: 07_espectrograma.png")
    
    print("\n✅ ¡Todos los gráficos han sido generados!")
    print("\nArchivos creados:")
    print("  01_canal_derecho.png")
    print("  02_canal_izquierdo.png")
    print("  03_comparativa_superpuesta.png")
    print("  04_comparativa_sincronizada.png")
    print("  05_barras_rms.png")
    print("  06_espectro_fft.png")
    print("  07_espectrograma.png")
    
    # Mostrar las gráficas
    plt.show()


if __name__ == "__main__":
    main()