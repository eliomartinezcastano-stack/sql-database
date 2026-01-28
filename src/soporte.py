
import pandas as pd
import numpy as np
import re 


### TABLA METACRITIC ###

def filtrar_y_renombrar_columnas(df):
    """ FUNCIÓN 1: Estructura """
    print(" 1. Seleccionando columnas útiles y renombrando para SQL")
    # Limpieza inicial de columnas
    df.columns = df.columns.astype(str).str.lower().str.strip()
    
    columnas_a_mantener = ['title', 'metascore', 'userscore', 'genres', 'releasedate']
    cols_existentes = [c for c in columnas_a_mantener if c in df.columns]
    
    df_resultado = df[cols_existentes].copy()
    
    nombres_sql = {
        'title': 'title',
        'metascore': 'meta_score',
        'userscore': 'user_score',
        'genres': 'genre',
        'releasedate': 'release_date'
    }
    
    df_resultado.rename(columns=nombres_sql, inplace=True)
    return df_resultado



def normalizar_textos_y_fechas(df):
    """ FUNCIÓN 2: Limpieza de Texto """
    print(" 2. Limpiando títulos y corrigiendo formato de fechas")
    
    if 'title' in df.columns:
        # 1. Minúsculas y espacios
        df['title'] = df['title'].astype(str).str.lower().str.strip()
        df['title'] = df['title'].str.replace(r'[^\w\s]', '', regex=True)
    
    if 'release_date' in df.columns:
        df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
        
    return df



def estandarizar_puntuaciones(df):
    """ FUNCIÓN 3: Scores """
    print(" 3. Convirtiendo scores a números y ajustando escala (0-100)")
    
    # Metascore
    if 'meta_score' in df.columns:
        df['meta_score'] = pd.to_numeric(df['meta_score'], errors='coerce')
        
    # User Score
    if 'user_score' in df.columns:
        df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')
        
        # Solo multiplicamos por 10 si el valor parece estar en escala 0-10
        mas_pequeños = df['user_score'] <= 10
        df.loc[mas_pequeños, 'user_score'] = df['user_score'] * 10
        
    # Eliminar filas vacías
    if 'title' in df.columns:
        df.dropna(subset=['title'], inplace=True)
        df = df[df['title'] != '']
    
    subset_scores = [c for c in ['meta_score', 'user_score'] if c in df.columns]
    if subset_scores:
        df.dropna(subset=subset_scores, how='all', inplace=True)
        
    return df
 


def unificar_juegos_duplicados(df):
    """ FUNCIÓN 4: Duplicados """
    print(" 4. Fusionando juegos duplicados y calculando media de notas")
    
    if 'genre' in df.columns:
        df['genre'] = df['genre'].astype(str).str.split(',').str[0].str.strip()
    
    if 'title' in df.columns:
        agrupacion = {
            'meta_score': 'mean',    
            'user_score': 'mean',    
            'genre': 'first',        
            'release_date': 'min'    
        }
        
        reglas = {k: v for k, v in agrupacion.items() if k in df.columns}
        
        df = df.groupby('title', as_index=False).agg(reglas)
        
        if 'meta_score' in df.columns:
            df['meta_score'] = df['meta_score'].round(1)
        if 'user_score' in df.columns:
            df['user_score'] = df['user_score'].round(1)

    return df

### TABLA VENTAS ###


def limpiar_estructura_ventas(df):
    """Función 1: Limpieza inicial """
    print(" Estructurando tabla de ventas...")
    
    columns_to_mantain = ['title', 'genre', 'critic_score', 'total_sales', 'na_sales', 'jp_sales', 'other_sales']
    # Filtramos solo las que existan para no dar error
    cols = [c for c in columns_to_mantain if c in df.columns]
    df = df[cols].copy()
    
    # Convertir a numérico
    cols_num = ['total_sales', 'na_sales', 'jp_sales', 'other_sales']
    for c in cols_num:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    # Eliminar titulos vacios
    if 'title' in df.columns:
        df.dropna(subset=['title'], inplace=True)
    
    return df


def agrupar_ventas(df):
    """Función 2: Agrupación y Cálculos Regionales """
    print("Agrupando y calculando regiones...")
    
    # 1. Agrupar por título (Sumar ventas)
    if 'title' in df.columns:
        reglas = {
            "total_sales": "sum",
            "na_sales": "sum",
            "jp_sales": "sum",
            "other_sales": "sum",
            "genre": "first"
        }
        # Filtrar reglas válidas
        reglas_validas = {k: v for k, v in reglas.items() if k in df.columns}
        
        df = df.groupby("title", as_index=False).agg(reglas_validas)
        
        # Ordenar
        if 'total_sales' in df.columns:
            df = df.sort_values(by="total_sales", ascending=False)

        # 2. Crear columnas regionales (Japón vs Resto)
        if 'jp_sales' in df.columns:
            df["sales_japan"] = df["jp_sales"]
        
        if 'na_sales' in df.columns and 'other_sales' in df.columns:
            df["sales_non_japan"] = df["na_sales"] + df["other_sales"]
            
        if 'total_sales' in df.columns:
            df["sales_total"] = df["total_sales"]
            
    return df




















