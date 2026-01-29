
import pandas as pd
import numpy as np
import re 
from sqlalchemy import text


# ESTRUCTURA SQL (Para crear tablas limpias)

def crear_tablas_videogames(engine):
    
    print(" Iniciando tablas en SQL...")
    
    queries = [
        "DROP TABLE IF EXISTS sales;",
        "DROP TABLE IF EXISTS metacritic;",
        
        
        """
        
        CREATE TABLE metacritic (
            title VARCHAR(255) NOT NULL,
            release_date DATE,
            genre VARCHAR(255),
            meta_score INT,
            user_score FLOAT, 
            PRIMARY KEY (title)
        );
        """,
        
        """
        CREATE TABLE sales (
            title VARCHAR(255) NOT NULL,
            genre VARCHAR(255),
            total_sales FLOAT,
            na_sales FLOAT,
            jp_sales FLOAT,
            pal_sales FLOAT,
            other_sales FLOAT,
            sales_non_japan FLOAT,
            PRIMARY KEY (title)
        );
        """
    ]
    
    with engine.connect() as conn:
        for query in queries:
            conn.execute(text(query))
        conn.commit()
        
    print(" Tablas 'metacritic' y 'sales' creadas.")


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


def clean_metacritic_df(df):
    """Pipeline completo Metacritic."""
    df = filtrar_y_renombrar_columnas(df)
    df = normalizar_textos_y_fechas(df)
    df = estandarizar_puntuaciones(df)
    df = unificar_juegos_duplicados(df)
    return df


### TABLA VENTAS ###

def limpiar_estructura_ventas(df):
    """ Función 1: Limpieza inicial """
    print(" 1. Estructurando tabla de ventas...")
    
    # Columnas a mantener 
    columns_to_mantain = [ 
        'title', 'genre', 'critic_score', 'total_sales', 
        'na_sales', 'jp_sales', 'pal_sales', 'other_sales'
    ]
    
    # Filtramos solo las que existan
    cols = [c for c in columns_to_mantain if c in df.columns]
    df = df[cols].copy()
    
    
    cols_num = ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales']
    for c in cols_num:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    # Eliminar títulos vacíos
    if 'title' in df.columns:
        df.dropna(subset=['title'], inplace=True)
    
    return df


def agrupar_ventas(df):
    """ Función 2: Agrupación y Cálculos Regionales """
    print(" 2. Agrupando y calculando regiones...")
    
    # 1. Agrupar por título
    if 'title' in df.columns:
        reglas = {
            "total_sales": "sum",
            "na_sales": "sum",
            "jp_sales": "sum",
            "pal_sales": "sum",    
            "other_sales": "sum",
            "genre": "first"
        }
        reglas_activas = {k: v for k, v in reglas.items() if k in df.columns}
        
        df = df.groupby("title", as_index=False).agg(reglas_activas)
        
        # Ordenar
        if 'total_sales' in df.columns:
            df = df.sort_values(by="total_sales", ascending=False)

        
        # Sumamos: Norteamérica + Europa/Africa (PAL) + Otros
        cols_non_japan = ['na_sales', 'pal_sales', 'other_sales']
        
        # Verificamos que existan antes de sumar
        cols_presentes = [c for c in cols_non_japan if c in df.columns]
        
        if cols_presentes:
            df["sales_non_japan"] = df[cols_presentes].sum(axis=1)

    return df

def round_sales_columns(df, decimals=2):
    """ Función 3: Redondeo de columnas de ventas """
    print(" 3. Redondeando columnas de ventas...")
    cols = [
        'total_sales', 'na_sales', 'jp_sales',
        'pal_sales', 'other_sales', 'sales_non_japan'
    ]
    cols = [c for c in cols if c in df.columns]
    df = df.copy()
    df[cols] = df[cols].round(decimals)
    return df


def clean_sales_df(df):
    """Pipeline completo ventas."""
    df = limpiar_estructura_ventas(df)
    df = normalizar_textos_y_fechas(df)
    df = agrupar_ventas(df)
    df = round_sales_columns(df, 2)
    return df













