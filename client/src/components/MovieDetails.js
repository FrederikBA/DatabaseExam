import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import apiUtils from '../utils/apiUtils';

const MovieDetails = () => {
    const { movieId } = useParams();
    const [movie, setMovie] = useState(null);
    const [isLoading, setIsLoading] = useState(true);


    const URL = apiUtils.getUrl()

useEffect(() => {
    const getMovieDetails = async () => {
        const response = await apiUtils.getAxios().get(URL + `/movies/${movieId}`)
        setMovie(response.data)
        setIsLoading(false)
    }
    getMovieDetails()
},[URL, movieId]);

    if (isLoading) {
        return <h2>Loading...</h2>;
    }

    if (!movie) {
        return <h2>Movie not found</h2>;
    }

    return (
        <div>
            <h2>{movie.title}</h2>
            {/* Render other movie details */}
        </div>
    );
};

export default MovieDetails;
