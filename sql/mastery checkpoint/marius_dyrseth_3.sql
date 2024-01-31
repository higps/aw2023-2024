--3 DQL (DVDRental) (LEVEL 1)
--We want to know how many customers we have around the world. Write a query that returns the
--top 5 districts ranked by how many customers live in them. The query should return district name,
--country name and customer count.

--Outputs the count and district, but is missing the country name, adding these results in loss of customer count
SELECT count(c.customer_id) AS "Customers", a.district, c3.country , c2.city 
	FROM customer c
	JOIN address a USING (address_id)
	JOIN city c2 USING (city_id)
	JOIN country c3 USING (country_id)
	GROUP BY a.district, c3.country , c2.city 
	ORDER BY "Customers" DESC
	LIMIT 5;

	
--Atttempted as with statement, still incorrect
WITH count_district AS (
	SELECT count(c.customer_id) AS "Customers", a.district
	FROM customer c
	JOIN address a USING (address_id)
	JOIN city c2 USING (city_id)
	JOIN country c3 USING (country_id)
	GROUP BY a.district
	ORDER BY "Customers" DESC
	LIMIT 5)
SELECT count(c.customer_id) AS "Customers", cd.district, c2.city , c3.country
	FROM customer c, count_district cd
	JOIN address a ON a.address_id = c.address_id 
	JOIN city c2 ON c2.city_id = a.city_id 
	JOIN country c3 ON c2.country_id = c3.country_id
	WHERE cd.district IN a.district
	GROUP BY a.district, c2.city, c3.country;


--Not correct, as the counts we get are wrong
SELECT DISTINCT the_list."Customers", the_list.district, c2.city, c3.country 
	FROM (
	SELECT count(c.customer_id) AS "Customers", a.district
	FROM customer c
	JOIN address a USING (address_id)
	JOIN city c2 USING (city_id)
	JOIN country c3 USING (country_id)
	GROUP BY a.district
	ORDER BY "Customers" DESC
	LIMIT 5
	) AS the_list, city c2  
	JOIN address a ON a.city_id = c2.city_id 
	JOIN country c3 ON c3.country_id = c2.country_id
WHERE the_list.district IN (SELECT address.district FROM address)
ORDER BY the_list."Customers" DESC
LIMIT 5;
