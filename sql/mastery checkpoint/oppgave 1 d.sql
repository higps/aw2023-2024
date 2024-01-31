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