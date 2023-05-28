// Recommend five movies based on the movies the user rent on the website.

  MATCH (m:Movie)-[r:SIMILAR]-(n:Movie)
    WHERE m.Id IN $ids AND NOT n.Id IN $ids
    RETURN n.Title AS movie_title, n.Id AS movie_id, n.Release_year AS ReleaseYear, n.Poster AS Poster, n.Price AS Price, n.Rating AS Rating, AVG(r.Score) AS average_similarity
    ORDER BY average_similarity DESC
    LIMIT 5