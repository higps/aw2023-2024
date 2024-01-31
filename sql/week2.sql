

-- 1# Create DB table
CREATE TABLE food_items(
	food_id INTEGER PRIMARY KEY,
	food_name VARCHAR(30) NOT NULL,
	food_type VARCHAR(30),
	food_rating INT CHECK (food_rating BETWEEN 1 AND 5),
	food_price FLOAT NOT NULL
);

SELECT DISTINCT food_name FROM food_items;

-- #2 Populate food data
INSERT INTO food_items(food_name, food_type, food_rating, food_price)
VALUES 
('Beef', 'Meat', 5, 80.0),
('Chicken', 'Meat', 4, 70.0),
('Pork', 'Meat', 4, 75.5),
('Cheese', 'Dairy', 5, 50.0),
('Cucumber', 'Vegetable', 2, 15.0),
('Lettuce', 'Vegetable', 3, 10.0),
('Tomatoes', 'Vegetable', 3, 20.0),
('Onions', 'Vegetable', 1, 15.0),
('Jalapeños', 'Vegetable', 4, 25.5),
('Sour Cream', 'Dairy', 4, 40.0),
('Guacamole', 'Dip', 5, 60.0),
('Salsa', 'Dip', 4, 40.0),
('Taco Shell', 'Grain', 4, 30.25),
('Refried Beans', 'Legume', 3, 35.0),
('Corn', 'Vegetable', 2, 20.90),
('Rice', 'Grain', 2, 25.0),
('Olives', 'Fruit', 1, 30.90);


-- 3 Distinct food types sorted from Z to A
SELECT DISTINCT food_type from food_items
ORDER BY food_type DESC;

-- 4 Only food items that cost more than some price

SELECT * FROM food_items
WHERE food_price > 35.0
ORDER BY food_price DESC;

-- 5 retrieves only food items that cost more than some price and has a rating of 1 or 4

SELECT * FROM food_items
WHERE food_price > 15.0
AND food_rating IN (1,4)
ORDER BY food_rating DESC;

-- 6 retrieves only food items that cost more than some price and has a rating between 1 and 4

SELECT * FROM food_items
WHERE food_price > 15.0
AND food_rating BETWEEN 1 AND 4
ORDER BY food_rating DESC;

SELECT * FROM food_items
WHERE food_price > 15.0
AND food_rating IN (1,2,3,4)
ORDER BY food_rating DESC;

SELECT * FROM food_items
WHERE food_price > 15.0
AND (food_rating = 1 OR food_rating = 2 OR food_rating = 3 OR food_rating = 4)
ORDER BY food_rating DESC;

-- 7 retrieves the name, the type and the price for all products
SELECT food_name, food_type, food_price from food_items;


-- 8 retrieves the name, the type and the price for the top three most expensive products
SELECT food_name, food_type, food_price from food_items
ORDER BY food_price DESC
LIMIT 3;

-- 9 Write a SQL query that uses the LIKE operator to get all items beginning with a letter of your choice
SELECT * FROM food_items
WHERE food_name LIKE 'C%';

