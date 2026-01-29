

USE videogames;


CREATE TABLE metacritic (
    title VARCHAR(255) NOT NULL,
    release_date DATE,
    genre VARCHAR(255),
    meta_score INT,
    user_score INT,
    PRIMARY KEY (title)
);


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

select * from sales;