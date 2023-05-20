import React from 'react';
import { useNavigate } from 'react-router-dom';
import star from '../img/star.png';
import apiUtils from '../utils/apiUtils'; // Import apiUtils

const Posters = ({ movies, isLoading }) => {
    const navigate = useNavigate();

    const handleMovieClick = (movieId) => {
        navigate(`/movies/${movieId}`);
    };

    const addToCart = async (movieId, price) => {
        const userId = 1; // This should be replaced with the actual user Id
        const duration = 7; // Set duration to 7 days as default

        try {
            await apiUtils.getAxios().post(apiUtils.getUrl() + '/addtocart', {
                user_id: userId,
                movie_id: movieId,
                duration: duration,
                price: price,
            });

            alert('Movie added to cart!');
        } catch (error) {
            console.log(error);
            alert('There was an error adding the movie to the cart.');
        }
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
                            <button onClick={(e) => {e.stopPropagation(); addToCart(movie.movie_id, movie.price)}}>Rent</button>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default Posters;
