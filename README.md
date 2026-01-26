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

