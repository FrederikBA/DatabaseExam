import React from 'react';
import { useNavigate } from 'react-router-dom';
import star from '../img/star.png';

const Posters = ({ movies, isLoading }) => {
    const navigate = useNavigate();

    const handleMovieClick = (movieId) => {
        // Redirect to movie details page using movieId
        navigate(`/movies/${movieId}`);
    };

    if (isLoading) {
        return <h2>Loading...</h2>;
    }

    return (
        <div className="row row-cols-5">
            {movies.map((movie) => (
                <div key={movie.movie_id} className="col mb-4 poster" onClick={() => handleMovieClick(movie.movie_id)}>
                    <div className="">
                        <img src={movie.poster} className="card-img-top" alt={movie.title} />
                        <div className="card-body center">
                            <p className="card-title">{movie.title}</p>
                            <div><img className="star" src={star} alt="Rating Star" />{movie.rating} / 10</div>
                            <div>{movie.price}.- DKK</div>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default Posters;
