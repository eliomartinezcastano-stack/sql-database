# sql-database
"Análisis de datos de Nintendo: Estrategia de videojuegos con SQL y Python." 

'hola'

## Estructura del Proyecto

sql-database/
│
├── data/
│   ├── raw/                <-- GUARDA AQUÍ tus CSVs descargados hoy
│   └── processed/          <-- Aquí guardaremos los CSVs limpios mañana
│
├── notebooks/
│   ├── 1_exploracion.ipynb <-- Tu cuaderno de sucio (trabajo de hoy)
│   ├── 2_limpieza.ipynb    <-- Tu cuaderno de transformación (trabajo de mañana)
│   └── 3_reporte.ipynb     <-- El informe final con gráficas y narrativa
│
├── src/                    <-- CÓDIGO FUENTE (Vital para la nota)
│   ├── soporte.py          <-- Aquí escribirás tus funciones de limpieza (def clean_data...)
│   └── __init__.py         <-- (Opcional) Archivo vacío para que Python reconozca la carpeta
│
├── sql/
│   ├── esquema.sql         <-- El código CREATE TABLE para crear la base de datos
│   ├── consultas.sql       <-- Todas las queries (SELECT, JOIN) que hagas
│   └── erd_diagrama.png    <-- La imagen de tu diagrama de relaciones
│
├── .gitignore              <-- Archivo de configuración para Git
└── README.md               <-- La documentación del proyecto



🧪 Hipótesis del Proyecto
Para responder a la pregunta de negocio, hemos planteado dos hipótesis analíticas que validaremos mediante datos (SQL & Python):

## Hipótesis 1: Benchmarking Competitivo y Océanos Rojos
 -- "La Estrategia de Diferenciación"

-- Planteamiento: Los principales competidores del mercado (Publisher != 'Nintendo') concentran la mayor parte de sus ingresos en géneros sobresaturados como Shooters y Acción, creando un "Océano Rojo" (alta competencia, márgenes ajustados).

-- Validación: Si los datos demuestran que Nintendo lidera nichos de mercado exclusivos (como Plataformas o Aventura Familiar) donde la competencia es mínima, la recomendación será MANTENER EL RUMBO en cuanto a desarrollo de producto, evitando imitar a la competencia.

## Hipótesis 2: Divergencia Regional y Localización
"La Estrategia de Expansión Global"

-- Planteamiento: Existe una discrepancia significativa en la recepción de productos entre el mercado local (Japón) y el mercado global (Occidente). Históricamente, se asignan recursos a títulos que solo funcionan en Japón (JP_Sales), descuidando el potencial de crecimiento en Norteamérica y Europa.

-- Validación: Si los datos revelan que la rentabilidad de géneros clave (como RPGs) cae drásticamente fuera de Japón, mientras que otros géneros tienen demanda universal, la recomendación será CAMBIAR LA ESTRATEGIA de ventas, priorizando la "occidentalización" del catálogo y optimizando el presupuesto de marketing global.

## 📊 Fuentes de Datos
-- Para este análisis se integrarán dos fuentes de datos complementarias:

-- Ventas y Mercado (Quantitative): Video Game Sales 2024 (Incluyendo datos históricos y de Nintendo Switch).

-- Crítica y Calidad (Qualitative): Metacritic Reviews 2025 (Metascore y User Score).