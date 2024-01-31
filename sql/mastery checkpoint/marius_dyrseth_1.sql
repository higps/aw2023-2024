--A (LEVEL 1)
--Write a query to find all horror films described as being “beautiful”. The query should return the film
--titles, category names and description of all such films, ordered by film name.

SELECT f.title AS "Film Name", c.name AS "Category", f.description FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON fc.category_id  = c.category_id
WHERE f.description LIKE '%Beautiful%'
AND c.name = 'Horror'
ORDER BY f.title;

--B (LEVEL 1)
--Write a query to find all action movies whose descriptions indicate they involve a database
--administrator. The query should return the film titles, category names and description of all such
--films, ordered by film name.

SELECT f.title AS "Film Name", c.name AS "Category", f.description FROM film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON fc.category_id  = c.category_id
WHERE f.description LIKE '%Database Administrator%'
AND c.name = 'Action'
ORDER BY f.title;

--C (LEVEL 1)
--Use the two queries above to write a single query which lists all horror films described as being
--“beautiful”, and all action movies whose descriptions indicate they involve a database administrator.
--The query should return the film titles, category names and description of all such films.

WITH horror_films AS (
	SELECT f.title AS "Film Name", c.name AS "Category", f.description FROM film f
	JOIN film_category fc ON fc.film_id = f.film_id
	JOIN category c ON fc.category_id  = c.category_id
	WHERE f.description LIKE '%Beautiful%'
	AND c.name = 'Horror'
	ORDER BY f.title),
	action_films AS(
		SELECT f.title AS "Film Name", c.name AS "Category", f.description FROM film f
		JOIN film_category fc ON fc.film_id = f.film_id
		JOIN category c ON fc.category_id  = c.category_id
		WHERE f.description LIKE '%Database Administrator%'
		AND c.name = 'Action'
		ORDER BY f.title
)
SELECT DISTINCT f.title, c.name, f.description 
FROM horror_films hf, action_films af, film f
JOIN film_category fc ON fc.film_id = f.film_id
JOIN category c ON fc.category_id  = c.category_id
WHERE hf."Film Name" = f.title
OR af."Film Name" = f.title
ORDER BY c."name";

