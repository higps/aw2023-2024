--4. 
-- Write SQL queries to create the following database.
--Note that phone number in the EMP table can only be 8 characters. SSN in the PERSON table can
--only be 11 characters. ZIP in the ADDRESS table can only be 4 characters. Explain any assumptions
--you make when creating the tables.


CREATE TABLE PERSON (
    PHONE INT PRIMARY KEY,
    LAST_NAME VARCHAR(50),
    FIRST_NAME VARCHAR(50),
    MID_INT VARCHAR(50),
    SSN VARCHAR(11) NOT NULL
);


CREATE TABLE ADDRESS (
    user_id SERIAL PRIMARY KEY,
    ST_ADDR VARCHAR(50) NOT NULL,
    CITY VARCHAR(50) NOT NULL,
    STATE VARCHAR(50) NOT NULL,
    ZIP VARCHAR(4) NOT NULL
);

CREATE TABLE EMP (
    EMP_INFO INT REFERENCES PERSON(SSN),
    ADDR_INFO INT REFERENCES ADDRESS(ST_ADDR),
    PRIMARY KEY (EMP_INFO, ADDR_INFO)
);





CREATE TABLE marius_users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

-- Create a table for products with a primary key
CREATE TABLE marius.marius_products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL
);

-- Create a composite table with foreign keys referencing the primary keys of the users and products tables
CREATE TABLE marius.marius_composite_table (
    user_id INT REFERENCES marius.marius_users(user_id),
    product_id INT REFERENCES marius.marius_products(product_id),
    PRIMARY KEY (user_id, product_id)
);