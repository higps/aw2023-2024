

-- Create DB table
CREATE TABLE food_items(
	food_id INTEGER PRIMARY KEY,
	food_name VARCHAR(30) NOT NULL,
	food_type VARCHAR(30) NOT NULL,
	food_rating INT CHECK (food_rating BETWEEN 1 AND 5),
	food_price FLOAT NOT NULL
);

--SELECT DISTINCT food_name FROM food_items;


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


-- 1 Write a SQL query that counts the total number of rows.
SELECT COUNT(*) as total_number_of_rows from food_items;


-- 2. Write a SQL query that counts the number of non-null food types.
SELECT COUNT(food_type) FROM food_items
WHERE food_type IS NOT NULL;

-- 3 Write a SQL query that sums the prices of each food type. 
-- You should output the food type and the sum of the prices as the only two columns. 
-- Order by the food type the most expensive summed price.

SELECT food_type, SUM(food_price) as total_price FROM food_items
GROUP BY food_type
ORDER BY SUM(food_price) DESC;

-- 4 Write a SQL query that returns the average price of all combinations of food type and rating 
-- (Hint: You must ORDER BY two columns together). Make the output be columns of food type, rating and average price and have them
-- ordered alphabetically by food type followed by rating starting from 5 down to 1.

SELECT food_type, food_rating, AVG(food_price) as average_price from food_items
GROUP by food_type, food_rating
ORDER BY food_type, food_rating DESC;

-- 5 Write a SQL query that returns the least expensive item for each rating.

SELECT food_name, food_rating, MIN(food_price) from food_items
GROUP BY food_rating
ORDER BY food_rating;

-- 6 Write a SQL query that returns the food type and the count of foods in that category, but only for groups with more than one item in them.

SELECT food_type as 'Food Category', COUNT(food_type) as 'Count' from food_items
GROUP BY food_type
HAVING COUNT(food_type) > 1;
