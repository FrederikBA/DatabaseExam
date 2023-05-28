// Get the details of the movie when clicking on a movie poster from the front page

MATCH (m:Movie {Id: $movieId})
    OPTIONAL MATCH (m)<-[r:`STARRED_IN`]-(actor:Actor)
    OPTIONAL MATCH (m)<-[:INSTRUCTED]-(director:Director)
    OPTIONAL MATCH (m)-[:HAS]->(genre:Genre)
    OPTIONAL MATCH (m)<-[:PUBLISHED]-(publisher:Publisher)
    OPTIONAL MATCH (m)<-[:FOR]-(review:Review)
    RETURN m.Title AS Title, m.Id AS movieId, m.Rating AS Rating, m.Summary AS Summary,
    m.Release_year AS ReleaseYear, m.Runtime AS Runtime, m.Certificate AS Certificate, m.Poster AS Poster,
    COLLECT(DISTINCT actor.Name) AS Actors, COLLECT(DISTINCT director.Name) AS Directors,
    COLLECT(DISTINCT genre.Genre) AS Genres, COLLECT(DISTINCT publisher.Name) AS Publishers,
    COLLECT(DISTINCT review.Content) AS Reviews