# Análisis de Datos - Spotify (Proyecto personal)

Este repositorio contiene un análisis exploratorio rápido del dataset `spotify.csv`. El trabajo principal está en el notebook `spotify.ipynb`.

## Resumen de lo que hice

- Cargué el dataset `spotify.csv` y realicé una exploración inicial.
- Documenté las celdas con comentarios en español y un tono personal.
- Analicé las variables numéricas: listé columnas numéricas, obtuve mínimos/máximos, calculé media, mediana y desviación estándar.
- Añadí una visualización rápida: histograma de `popularity` (si la columna está presente).
- Incluí una sección de conclusiones con observaciones generales sobre popularidad, duración y otros atributos.

## Estructura relevante

- `spotify.csv` — dataset (debe estar en la misma carpeta que los notebooks o actualizar la ruta en la celda de carga).
- `spotify.ipynb` — notebook principal con el análisis y visualizaciones.

## Requisitos mínimos

- Python 3.8+ (recomendado 3.10+)
- Librerías: pandas, numpy, matplotlib, seaborn

Recomendado: crear un entorno virtual y luego instalar las dependencias.

Ejemplo (zsh / macOS):

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pandas numpy matplotlib seaborn jupyter
```

Si no usas entorno virtual puedes instalar directo:

```bash
pip install pandas numpy matplotlib seaborn
```

## Cómo ejecutar el notebook

Opción A — Jupyter Notebook/Lab (recomendado para ejecutar celda a celda):

```bash
# estando en la carpeta `Spotify`
jupyter notebook spotify.ipynb
# o
jupyter lab
```

Opción B — VS Code:

- Abre la carpeta `Spotify` en VS Code.
- Abre `spotify.ipynb` y selecciona un kernel de Python con las dependencias instaladas. Ejecuta las celdas.

> Nota: si mueves `spotify.csv`, actualiza la ruta en la celda que carga el archivo.

## Comprobaciones rápidas después de ejecutar

- `spotify.head()` debería mostrar las primeras filas sin errores.
- La celda de información debe imprimir dimensiones, tipos y conteo de valores nulos.
- Si existe `popularity`, verás un histograma; si no, la celda mostrará un aviso.

## Ejemplo rápido de salida (lo que verás)

- Dimensiones (filas, columnas): `(N, M)`
- Lista de columnas: `['name', 'artist', 'popularity', 'duration_ms', ...]`
- Estadísticas básicas (media / mediana / std) para columnas numéricas.
- Histograma de `popularity` (si aplica).
