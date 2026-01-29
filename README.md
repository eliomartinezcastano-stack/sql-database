## 🎮 Nintendo Data Analytics: Regional Sales & Review Insights for Genre Strategy


 ## 🧭 Objetivo del proyecto 
Construir una base de datos integrada de ventas y críticas de videojuegos para identificar qué géneros funcionan mejor por región y evaluar si el género más vendido coincide con el mejor valorado (crítica profesional y usuarios).


## 🏢 Contexto del negocio  
Empresa: Nintendo (equipo interno de Data Analytics).

Desafío: Priorizar el desarrollo y la estrategia de lanzamiento de nuevos títulos basándose en diferencias regionales de demanda y en la relación entre ventas y percepción de calidad.

Decisiones clave: 
- Qué géneros priorizar para Japón vs mercados occidentales (NA y Europa/África).
- Si apostar por géneros “top ventas” implica también buena recepción crítica.


## 🗂️ Estructura del Proyecto

sql-database/
 data/        → datasets originales y procesados 
 notebooks/   → exploración y limpieza 
 sql/         → esquema de la base de datos, consultas y ERD
 src/         → funciones reutilizables de Python


 ## 📊 Fuentes de Datos
-- Para este análisis se integrarán dos fuentes de datos complementarias:

-- Ventas y Mercado (Quantitative): Video Game Sales 2024 (Incluyendo datos históricos y de Nintendo Switch).

-- Crítica y Calidad (Qualitative): Metacritic Reviews 2025 (Metascore y User Score) 

### 1. Tabla: `metacritic`
Contiene metadatos y puntuaciones de crítica de videojuegos.

| Columna | Tipo | Descripción |
|---------|------|-------------|
| **title** | VARCHAR(255) | Título del videojuego (Clave Primaria) |
| **release_date** | DATE | Fecha de lanzamiento del juego |
| **genre** | VARCHAR(255) | Género del videojuego |
| **meta_score** | INT | Puntuación de Metacritic (crítica profesional) |
| **user_score** | INT | Puntuación de usuarios en Metacritic |

---

### 2. Tabla: `sales`
Contiene datos de ventas por región de videojuegos.

| Columna | Tipo | Descripción |
|---------|------|-------------|
| **title** | VARCHAR(255) | Título del videojuego (Clave Primaria) |
| **genre** | VARCHAR(255) | Género del videojuego |
| **total_sales** | FLOAT | Ventas totales mundiales (en millones) |
| **na_sales** | FLOAT | Ventas en Norteamérica (en millones) |
| **jp_sales** | FLOAT | Ventas en Japón (en millones) |
| **pal_sales** | FLOAT | Ventas en Europa y África (en millones) |
| **other_sales** | FLOAT | Ventas en otras regiones (en millones) |
| **sales_non_japan** | FLOAT | Ventas fuera de Japón (calculada) |

---

## ❓ Preguntas clave 
- H1. ¿Qué géneros lideran las ventas (porcentaje del total) en cada región: Japón, Norteamérica, Europa/África y otros mercados?
- H2. ¿El género más vendido coincide con el género mejor valorado (metascore y userscore)? Si no coincide, ¿qué diferencias se observan?


## 🔍 Proceso de análisis 
- Lenguaje de datos: Python (Pandas, NumPy) + SQL
- Base de datos: MySQL
- ORM: SQLAlchemy
- Período analizado: 2015-2024
- Técnicas SQL: INNER JOIN, GROUP BY, HAVING, SUM, AVG, COUNT, ROUND

**Transformaciones Clave**
1. Deduplicación: Múltiples registros del mismo juego → consolidación con media de puntuaciones
2. Estandarización: Escalas inconsistentes de puntuación → escala 0-100 uniforme
3. Agregación regional: Ventas por plataforma → sumatoria por región geográfica
4. Enriquecimiento: Cálculo de nuevas métricas (ventas no-Japón, dependencia regional, porcentajes)

## 📈 Resultados / Insights 
- Insight H1: Occidente (NA + Europa + Otros): Shooter & Sports dominan (37-40% del mercado)
Japón: RPG lidera absoluto (37%), 6x más que en occidente
La brecha es INMENSA: RPG es 27% del mercado japonés vs 8% en Europa

- Insight H2: Los géneros de Mayor Venta (Sports, Shooter) tienen CRÍTICA BAJA → La gente compra sin importar la crítica
Los géneros Mejor Valorados (MMO, Visual Novel) tienen VENTAS BAJAS → La crítica no garantiza éxito comercial
La única excepción: RPG → Logra balance: buenas ventas + buena crítica (74/71)


## 💡 Recomendaciones de negocio  
Problemas: Ausencia en Shooter ($144M/año, 2º mercado) y Crítica baja en géneros top (Sports/Shooter venden sin calidad).

 Acciones:
1. Mejorar la estrategia por región.
2. Mejorar el marketing en géneros que funcionan más en Japón para expandirlos en otras regiones.
   

## ⚠️ Limitaciones 
- Falta de variables como precio o campañas de marketing.
- Datos hasta 2024 (mercado puede haber cambiado).

## 🚀 Próximos pasos 
- Usar keys adicionales para mejorar el matching (plataforma, publisher).
- Analizar por consola o plataforma además de por género.
- Incluir análisis de tendencias por año.
- Analizar por rating ESRB para ver el impacto del público objetivo.

