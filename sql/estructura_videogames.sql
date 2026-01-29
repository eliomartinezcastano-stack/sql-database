USE videogames;

-- TABLA METACRITIC

ALTER TABLE metacritic
MODIFY COLUMN title VARCHAR(255) NOT NULL;

ALTER TABLE metacritic
MODIFY COLUMN release_date DATE;

ALTER TABLE metacritic
MODIFY COLUMN meta_score INT;

ALTER TABLE metacritic
MODIFY COLUMN user_score INT;

ALTER TABLE metacritic
MODIFY COLUMN genre VARCHAR(255);

ALTER TABLE metacritic
ADD PRIMARY KEY (title);


-- TABLA SALES

 ALTER TABLE sales
 MODIFY COLUMN title VARCHAR(255) NOT NULL;

ALTER TABLE sales
MODIFY COLUMN genre VARCHAR(255);

ALTER TABLE sales
MODIFY COLUMN  total_sales FLOAT;

ALTER TABLE sales
MODIFY COLUMN  na_sales FLOAT;

ALTER TABLE sales
MODIFY COLUMN  jp_sales FLOAT;

ALTER TABLE sales
MODIFY COLUMN  pal_sales FLOAT;

ALTER TABLE sales
MODIFY COLUMN  other_sales FLOAT;

ALTER TABLE sales
MODIFY COLUMN  sales_non_japan FLOAT;

ALTER TABLE sales
ADD PRIMARY KEY (title);


-- Hemos decidido NO incluir la restricción de Foreign Key .
-- La razón es que hay juegos en la tabla 'sales' que no existen en 'metacritic'.
-- Si forzamos la FK, el script fallaría o tendríamos que borrar esas ventas.
--
-- Es mejor conservar los datos de ventas (aunque no tengan crítica) 
-- que perderlos por una regla estricta. Trabajaremos con LEFT JOIN.

-- Query para comprobar los juegos que dan conflicto :
-- SELECT s.title 
-- FROM sales s
-- LEFT JOIN metacritic m ON s.title = m.title
-- WHERE m.title IS NULL;





