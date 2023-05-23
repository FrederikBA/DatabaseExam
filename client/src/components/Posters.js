import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import star from '../img/star.png';
import apiUtils from '../utils/apiUtils';

const Posters = ({ movies, isLoading }) => {
  const navigate = useNavigate();
  const [hoveredMovieId, setHoveredMovieId] = useState(null);


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

  const handleMovieClick = (movieId) => {
    navigate(`/movies/${movieId}`);
  };

  const handleMouseEnter = (movieId) => {
    setHoveredMovieId(movieId);
  };

  const handleMouseLeave = () => {
    setHoveredMovieId(null);
  };

  if (isLoading) {
    return <br></br>;
  }

  return (
    <div className="row row-cols-5">
      {movies.map((movie) => (
        <div key={movie.movie_id} className="col mb-4 poster" onMouseEnter={() => handleMouseEnter(movie.movie_id)}
          onMouseLeave={handleMouseLeave}>
          <img src={movie.poster} className="card-img-top" alt={movie.title} />
          {hoveredMovieId === movie.movie_id ? (
            <>
              <button onClick={() => handleMovieClick(movie.movie_id)} class="btn show-more">Vis mere</button>
              <button class="btn rent">Læg i kurv</button>
            </>
          ) : null}

          <div className="card-body center">
            <p className="card-title">{movie.title}</p>
            <div className="poster-text"><img className="star" src={star} alt="Rating Star" />{movie.rating} / 10</div>
            <span className="poster-text">Lej for: {movie.price} kr.</span>
          </div>
        </div>
      ))}
    </div>
  );




};

export default Posters;
