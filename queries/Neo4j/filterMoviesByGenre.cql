// Used to filter the movies by genre

 MATCH (m:Movie)-[:HAS]->(g:Genre)
    WHERE g.Genre = '{genre}'
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster, m.Price AS Price,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers
    ORDER BY m.Title