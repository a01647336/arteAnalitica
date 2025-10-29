# Análisis de Datos - Spotify (Proyecto personal)

Este repositorio contiene un análisis exploratorio rápido de un dataset de Spotify. El trabajo principal está en el notebook `spotify.ipynb` (y hay un notebook adicional `Untitled.ipynb`).

## Qué hice

- Cargué el dataset `spotify.csv` y realicé una exploración inicial.
- Añadí comentarios, encabezados y mensajes en español con un tono personal para que el notebook parezca hecho por mí.
- Realicé un análisis básico de las variables numéricas: listé columnas numéricas, calculé mínimos, máximos, medias, medianas y desviaciones estándar.
- Añadí una visualización rápida: histograma de la columna `popularity` (si existe en el CSV).
- Incluí una sección de conclusiones con observaciones generales sobre popularidad, duración y otros atributos.

## Estructura del repositorio (relevante)

- `spotify.csv` — archivo con los datos (asegúrate de que está en la misma carpeta que los notebooks).
- `spotify.ipynb` — notebook principal con el análisis y visualizaciones.
- `Untitled.ipynb` — notebook alternativo / versión previa del análisis.
- `main.py` — (si existe) script auxiliar; revisa su contenido antes de ejecutarlo.

## Requisitos

- Python 3.8+ (se recomienda 3.10+)
- Las siguientes librerías (puedes instalarlas con pip):
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - jupyter (opcional, si quieres abrir el notebook en Jupyter)

Ejemplo para crear un entorno virtual y instalar dependencias (zsh/macOS):

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pandas numpy matplotlib seaborn jupyter
```

Si prefieres instalar solo lo necesario sin entorno virtual:

```bash
pip install pandas numpy matplotlib seaborn
```

## Cómo ejecutar el notebook

Opción A — Abrir en Jupyter Notebook/Lab (recomendado si quieres ejecutar celda por celda):

```bash
# estando en la carpeta Spotify
jupyter notebook spotify.ipynb
# o
jupyter lab
```

Opción B — Abrir en VS Code

- Abre la carpeta `Spotify` en VS Code.
- Haz click en `spotify.ipynb` y ejecuta las celdas con el kernel de Python que tenga las dependencias instaladas.

Opción C — Ejecutar script (si `main.py` existe y es un runner):

```bash
python main.py
```

Nota: El notebook asume que `spotify.csv` está en la misma carpeta; si lo mueves, actualiza la ruta en la celda de carga de datos.

## Verificaciones rápidas después de ejecutar

- La celda de carga debe mostrar las primeras filas con `head()` sin errores.
- La celda de exploración debe imprimir las dimensiones, columnas y conteo de nulos.
- Si la columna `popularity` está presente, deberías ver un histograma. Si no, la celda imprimirá un mensaje indicando que falta la columna.

## Siguientes pasos recomendados (opcionales)

- Limpiar valores nulos: decidir imputación o eliminación según la columna.
- Normalizar/transformar variables con distribuciones sesgadas (log, z-score).
- Explorar correlaciones entre variables y construir un heatmap.
- Crear visualizaciones adicionales: scatter tempo vs popularity, boxplots por género/artist, clustering.
- Añadir un `requirements.txt` con las versiones exactas si vas a compartir el proyecto.

---

Si quieres, puedo:

- Crear un `requirements.txt` automáticamente con versiones aproximadas.
- Ejecutar el notebook aquí para comprobar que corre (necesitaría permisos de ejecución del kernel en este entorno).
- Añadir ejemplos de visualizaciones adicionales en el notebook.

_Dime cuál de estos pasos quieres que haga a continuación._
