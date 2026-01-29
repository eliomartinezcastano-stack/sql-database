USE videogames;


SELECT * FROM metacritic;
SELECT * FROM sales;

-- 1 Identificación de facturación por región y facturación global por género desde 2015 hasta 2024.
SELECT
s.genre,
ROUND(SUM(s.na_sales),2) as ventas_norteamerica,
ROUND(SUM(s.jp_sales),2) as ventas_japon,
ROUND(SUM(s.pal_sales),2) as ventas_europa_africa,
ROUND(SUM(s.other_sales),2) as otras_regiones,
ROUND(SUM(s.total_sales),2) as ventas_totales
FROM sales as s
INNER JOIN metacritic m on s.title = m.title
WHERE m.release_date >= '2015-01-01'
GROUP BY s.genre
ORDER BY ventas_totales DESC;

-- 2.1 Relación entre ventas y crítica ( meta_score y user_score)desde 2015 hasta 2024 ordenado por total ventas.

SELECT
s.genre,
ROUND(SUM(s.total_sales),2) AS total_ventas_millones,
ROUND(AVG(m.meta_score),2) AS nota_meta,
ROUND(AVG(m.user_score),2) AS nota_user,
COUNT(s.title) AS cantidad_juegos
FROM sales as s
INNER JOIN metacritic m on s.title = m.title
WHERE m.release_date >= '2015-01-01'
GROUP BY s.genre
HAVING cantidad_juegos >= 5
ORDER BY total_ventas_millones DESC;

-- 2.2 Relación entre ventas y crítica ( meta_score y user_score)desde 2015 hasta 2024 ordenado por metacritic.

SELECT
s.genre,
ROUND(SUM(s.total_sales),2) AS total_ventas_millones,
ROUND(AVG(m.meta_score),2) AS nota_meta,
ROUND(AVG(m.user_score),2) AS nota_user,
COUNT(s.title) AS cantidad_juegos
FROM sales as s
INNER JOIN metacritic m on s.title = m.title
WHERE m.release_date >= '2015-01-01'
GROUP BY s.genre
HAVING cantidad_juegos >= 5
ORDER BY nota_meta DESC;


-- 2.3 Relación entre ventas y crítica ( meta_score y user_score)desde 2015 hasta 2024  ordenado por user score.

SELECT
s.genre,
ROUND(SUM(s.total_sales),2) AS total_ventas_millones,
ROUND(AVG(m.meta_score),2) AS nota_meta,
ROUND(AVG(m.user_score),2) AS nota_user,
COUNT(s.title) AS cantidad_juegos
FROM sales as s
INNER JOIN metacritic m on s.title = m.title
WHERE m.release_date >= '2015-01-01'
GROUP BY s.genre
HAVING cantidad_juegos >= 5
ORDER BY nota_user DESC;



-- Porcentaje de riesgo según total de ventas por género en Japón desde 2015 hasta 2024 .

SELECT 
s.genre,
ROUND(SUM(s.jp_sales),2) AS ventas_japon_millones,
ROUND(SUM(s.total_sales),2) AS ventas_totales_millones,
ROUND(SUM(s.jp_sales)/ sum(s.total_sales) *100, 2) AS dependecia_japon
FROM sales AS s
INNER JOIN metacritic as m
on s.title = m.title
where m. release_date >= '2015-01-01'
GROUP BY genre
HAVING ventas_totales_millones > 1
ORDER BY dependecia_japon DESC;
    
    
-- Identificación de juegos con éxito comercial (mas 1 millones) y éxito en critica ( igual o mas 70) fuera de japon

SELECT
s.title AS titulo,
s.genre AS genero,
s.sales_non_japan AS ventas_no_japon,
m.meta_score AS meta_critica,
m.user_score AS user_critica
FROM sales AS s
INNER JOIN metacritic AS m
on s.title = m.title
WHERE release_date >= '2015-1-1'
AND s.total_sales > 1
AND m.meta_score >=70
AND m.user_score >=70
ORDER BY ventas_no_japon DESC;


-- Identificación de juegos con éxito comercial (mas 1 millones) y éxito en critica ( igual o mas 70) en  japon
SELECT
s.title AS titulo,
s.genre AS genero,
s.jp_sales  ventas_japon,
m.meta_score AS meta_critica,
m.user_score AS user_critica
FROM sales AS s
INNER JOIN metacritic AS m
on s.title = m.title
WHERE release_date >= '2015-1-1'
AND s.total_sales > 1
AND m.meta_score >=70
AND m.user_score >=70
ORDER BY ventas_japon DESC;


