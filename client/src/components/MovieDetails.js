import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import apiUtils from '../utils/apiUtils';
import star from '../img/star.png';
import '../MovieDetails.css';

const MovieDetails = () => {
  const { movieId } = useParams();
  const [movie, setMovie] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  const URL = apiUtils.getUrl();

  useEffect(() => {
    const getMovieDetails = async () => {
      const response = await apiUtils.getAxios().get(URL + `/movies/id/${movieId}`);
      setMovie(response.data);
      setIsLoading(false);
    };
    getMovieDetails();
  }, [URL, movieId]);

  if (isLoading) {
    return <h2>Loading...</h2>;
  }

  if (!movie) {
    return <h2>Movie not found</h2>;
  }

  return (
    <div className="movie-details-container">
      <h2 className="movie-title">{movie.title} ({movie.release_year})</h2>
      <div className="movie-poster">
        <img src={movie.poster} alt="Movie Poster" />
      </div>
      <div className="movie-info">
        <div>
          <h3>Rating</h3>
          <span className="details-rating">
            <img className="star" src={star} alt="Rating Star" />
            {movie.rating}
          </span>
        </div>
        <div>
          <h3>Runtime</h3>
          <span className="details-rating">
            {movie.runtime} minutes
          </span>
        </div>
        <div className="movie-summary">
          <h3>Summary</h3>
          <p>{movie.summary}</p>
        </div>
        <div>
          <h3>Actors</h3>
          <ul>
            {movie.actors.map((actor) => (
              <li key={actor}>{actor}</li>
            ))}
          </ul>
        </div>
        <div className="movie-directors">
          <h3>Directors</h3>
          <ul>
            {movie.directors.map((director) => (
              <li key={director}>{director}</li>
            ))}
          </ul>
        </div>
        <div className="movie-genres">
          <h3>Genres</h3>
          <ul>
            {movie.genres.map((genre) => (
              <li key={genre}>{genre}</li>
            ))}
          </ul>
        </div>
        <div className="movie-publishers">
          <h3>Publishers</h3>
          <ul className="details-list">
            {movie.publishers.map((publisher) => (
              <li key={publisher}>{publisher}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );

};

export default MovieDetails;
