# Write your MySQL query statement below
WITH UserRatingsCount AS (
    SELECT 
        u.name,
        COUNT(mr.movie_id) AS rating_count
    FROM 
        Users u
    JOIN 
        MovieRating mr ON u.user_id = mr.user_id
    GROUP BY 
        u.name
),
MaxUserRatings AS (
    SELECT 
        name
    FROM 
        UserRatingsCount
    WHERE 
        rating_count = (SELECT MAX(rating_count) FROM UserRatingsCount)
    ORDER BY 
        name
    LIMIT 1
),
Feb2020MovieRatings AS (
    SELECT 
        m.title,
        AVG(mr.rating) AS avg_rating
    FROM 
        Movies m
    JOIN 
        MovieRating mr ON m.movie_id = mr.movie_id
    WHERE 
        mr.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY 
        m.title
),
MaxAvgRatingMovies AS (
    SELECT 
        title
    FROM 
        Feb2020MovieRatings
    WHERE 
        avg_rating = (SELECT MAX(avg_rating) FROM Feb2020MovieRatings)
    ORDER BY 
        title
    LIMIT 1
)

SELECT 
    (SELECT name FROM MaxUserRatings) AS results
UNION ALL
SELECT 
    (SELECT title FROM MaxAvgRatingMovies) AS results;
