
# ¿Qué tengo que hacer?
# En esta actividad trabajaras con el conjunto de datos asignado para el reto. Tienes que replicar los pasos vistos durante las horas de salón en un diferente conjunto de datos, en este caso el Dataset de Spotify.

# spotify.csv Download spotify.csv

# Carga los datos usando tu lector de csv o con pandas. Es recomendable hacerlo con pandas.
# Verifica la cantidad de datos que tienes, las variables que contiene cada vector de datos e identifica el tipo de variables.
# Analiza las variables para saber que representa cada una y en que rangos se encuentran. Si la descripción del problema no te lo indica, utiliza el máximo y el mínimo para encontrarlo.
# Basándose en la media, mediana y desviación estándar de cada variable, que conclusiones puedes entregar de los datos.

import pandas as pd
import numpy as np
from pathlib import Path

# Local CSV path (file is expected next to this script)
file_path = Path(__file__).with_name('spotify.csv')

# Cargar los datos
df = pd.read_csv(file_path)


def print_section(title: str):
	print('\n' + '=' * 6 + f' {title} ' + '=' * 6)


if __name__ == '__main__':
	# Basic info
	print_section('Info del DataFrame')
	print(f"Ruta del archivo: {file_path}")
	print(f"Shape: {df.shape}")
	print('\nDtypes:')
	print(df.dtypes)
	print('\nPrimeras filas:')
	print(df.head(5))
	print('\nResumen (info):')
	df.info()

	# Valores nulos por columna
	print_section('Valores nulos por columna')
	valores_nulos = df.isnull().sum()
	print(valores_nulos)

	# Estadísticos descriptivos para columnas numéricas
	print_section('Estadísticos descriptivos (numéricos)')
	print(df.describe())

	# Estadísticas adicionales: media, mediana, desviación estándar, min, max por numéricas
	numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
	print_section('Medidas por columna numérica')
	for col in numeric_cols:
		col_data = df[col].dropna()
		print(f"- {col}: mean={col_data.mean():.4f}, median={col_data.median():.4f}, std={col_data.std():.4f}, min={col_data.min()}, max={col_data.max()}")

	# Métrica de ejemplo pedida
	if 'popularity' in df.columns:
		mediana = df['popularity'].median()
		print_section('Métrica ejemplo')
		print(f"Mediana de 'popularity': {mediana}")


	# Helper functions adapted to Spotify dataset
	def tracks_by_genre(df: pd.DataFrame, genre: str) -> pd.DataFrame:
		"""Regresa los tracks que contienen el género especificado."""
		return df[df['track_genre'].str.contains(genre, na=False)][['track_name', 'artists', 'popularity', 'track_genre']]


	def search_tracks_by_keyword(df: pd.DataFrame, keyword: str) -> pd.DataFrame:
		"""Busca títulos por palabra clave en el nombre (case-insensitive)."""
		return df[df['track_name'].str.contains(keyword, case=False, na=False)][['track_name', 'artists', 'album_name', 'popularity']]


	def top_artists(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
		"""Regresa los artistas con más tracks en el dataset.

		Nota: la columna 'artists' puede contener varios artistas separados por ';'.
		Esta función los separa y cuenta por artista individual.
		"""
		if 'artists' not in df.columns:
			return pd.DataFrame()
		artists_exploded = df.assign(artist_split=df['artists'].str.split(';')).explode('artist_split')
		artists_exploded['artist_split'] = artists_exploded['artist_split'].str.strip()
		grouped = artists_exploded.groupby('artist_split').agg(tracks_count=('track_name', 'count'), avg_popularity=('popularity', 'mean')).sort_values('tracks_count', ascending=False)
		return grouped.head(n)


	def longest_shortest_tracks(df: pd.DataFrame):
		"""Regresa el track más largo y el más corto (por duration_ms)."""
		out = {}
		if 'duration_ms' in df.columns:
			out['longest'] = df.loc[df['duration_ms'].idxmax(), ['track_name', 'artists', 'duration_ms', 'popularity']]
			out['shortest'] = df.loc[df['duration_ms'].idxmin(), ['track_name', 'artists', 'duration_ms', 'popularity']]
		return out


	def top_genres(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
		if 'track_genre' not in df.columns:
			return pd.DataFrame()
		return df['track_genre'].value_counts().head(n)


	# Ejemplos de uso e impresiones
	print_section('Top 10 géneros')
	top10_genres = top_genres(df, 10)
	print(top10_genres)

	print_section('Top artistas (por número de tracks)')
	print(top_artists(df, 10))

	print_section('Track más largo y más corto')
	ls = longest_shortest_tracks(df)
	if ls:
		print('Más largo:')
		print(ls['longest'].to_dict())
		print('Más corto:')
		print(ls['shortest'].to_dict())

	print_section('Ejemplos de búsqueda')
	print("Tracks que contienen 'Love' en el título:")
	print(search_tracks_by_keyword(df, 'Love').head(10))

	print("Tracks en género 'acoustic' (ejemplo):")
	print(tracks_by_genre(df, 'acoustic').head(10))

	# Tabla resumen: cuántos tracks por artista (top 20) y por género (top 20)
	print_section('Resumen: tracks por artista (top 20)')
	print(top_artists(df, 20))

	print_section('Resumen: tracks por género (top 20)')
	print(df['track_genre'].value_counts().head(20))

	# Gráfica opcional de los 10 géneros más populares
	try:
		import matplotlib.pyplot as plt

		print_section('Generando gráfica: top 10 géneros')
		ax = top10_genres.plot(kind='bar', figsize=(8, 5), title='Top 10 géneros')
		ax.set_xlabel('Género')
		ax.set_ylabel('Número de tracks')
		plt.tight_layout()
		outpath = Path(__file__).with_name('top_genres.png')
		plt.savefig(outpath)
		print(f'Gráfica guardada en: {outpath}')
		plt.close()
	except Exception as e:
		print('No se pudo generar la gráfica (¿matplotlib instalado?). Error:', e)


