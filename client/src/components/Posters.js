import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import star from '../img/star.png';
import apiUtils from '../utils/apiUtils';

const Posters = ({ movies, isLoading, rentNotifySuccess, rentNotifyError, rentNotifyLogin }) => {
  const navigate = useNavigate();
  const [hoveredMovieId, setHoveredMovieId] = useState(null);


  const addToCart = async (movieId, price) => {

    try {
      if (localStorage.getItem('jwtToken') !== null) {
        await apiUtils.getAxios().post(apiUtils.getUrl() + '/addtocart', {
          user_id: localStorage.getItem('userId'),
          movie_id: movieId,
          price: price,
        });
        rentNotifySuccess()
      } else {
        rentNotifyLogin()
      }

    } catch (error) {
      rentNotifyError()
    }
  };

  const handleMovieClick = (movieId) => {
    navigate(`/movies/id/${movieId}`);
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
              <button onClick={() => handleMovieClick(movie.movie_id)} className="btn show-more">Vis mere</button>
              <button onClick={(e) => { e.stopPropagation(); addToCart(movie.movie_id, movie.price); }} id="rent-button" className="btn rent">Læg i kurv</button>
            </>
          ) : null}

          <div className="card-body center">
            <p className="card-title">{movie.title} ({movie.release_year})</p>
            <div className="poster-text"><img className="star" src={star} alt="Rating Star" />{movie.rating} / 10</div>
            <span className="poster-text">Lej for: {movie.price} kr.</span>
          </div>
        </div>
      ))}
    </div>
  );




};

export default Posters;
