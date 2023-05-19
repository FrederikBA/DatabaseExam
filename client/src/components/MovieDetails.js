import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

const MovieDetails = () => {
    const { movieId } = useParams();
    const [movie, setMovie] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        // Fetch movie data based on movieId
        // You can replace this with your own logic to fetch the movie data
        const fetchMovieData = async () => {
            try {
                // Make an API call or fetch data from your data source
                const response = await fetch(`/api/movies/${movieId}`);
                const data = await response.json();

                setMovie(data); // Update the movie state with the fetched data
                setIsLoading(false); // Set isLoading to false
            } catch (error) {
                console.log(error);
                setIsLoading(false); // Set isLoading to false in case of an error
            }
        };

        fetchMovieData(); // Call the fetchMovieData function
    }, [movieId]);

    if (isLoading) {
        return <h2>Loading...</h2>;
    }

    if (!movie) {
        return <h2>Movie not found</h2>;
    }

    return (
        <div>
            <h2>{movie.title}</h2>
            <p>Release Year: {movie.release_year}</p>
            <p>Rating: {movie.rating}</p>
            {/* Render other movie details */}
        </div>
    );
};

export default MovieDetails;
