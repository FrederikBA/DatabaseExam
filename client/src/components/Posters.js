import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import star from '../img/star.png';
import apiUtils from '../utils/apiUtils';

const Posters = ({ movies, isLoading }) => {
  const navigate = useNavigate();
  const [hoveredMovieId, setHoveredMovieId] = useState(null);

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
      alert('There was an error adding the movie to the cart.');
    }
  };

  const handleMouseEnter = (movieId) => {
    setHoveredMovieId(movieId);
  };

  const handleMouseLeave = () => {
    setHoveredMovieId(null);
  };

  if (isLoading) {
    return <h2>Loading...</h2>;
  }

  return (
    <div className="row row-cols-5">
      {movies.map((movie) => (
        <div
          key={movie.movie_id}
          className="col mb-4 poster-container"
          onMouseEnter={() => handleMouseEnter(movie.movie_id)}
          onMouseLeave={handleMouseLeave}
        >
          <div className="hover-buttons">
            {hoveredMovieId === movie.movie_id ? (
              <>
                <button onClick={(e) => { e.stopPropagation(); addToCart(movie.movie_id, movie.price); }}>
                  Rent
                </button>
                <button onClick={() => handleMovieClick(movie.movie_id)}>
                  Movie Details
                </button>
              </>
            ) : null}
          </div>
          <img src={movie.poster} className="card-img-top" alt={movie.title} />
          <div className="card-body center">
            <p className="card-title">{movie.title}</p>
            <div>
              <img className="star" src={star} alt="Rating Star" />
              {movie.rating} / 10
            </div>
            <div>{movie.price}.- DKK</div>
          </div>
        </div>
      ))}
    </div>
  );




};

export default Posters;
