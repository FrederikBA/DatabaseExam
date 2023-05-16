import React from 'react';

const MovieDetails = () => {
  const movie = {
    id: 1,
    title: 'Movie 1',
    poster: 'poster1.jpg',
    genre: 'Action',
    releaseYear: 2021,
    rating: 7.5,
    cast: ['Actor 1', 'Actor 2', 'Actor 3'],
    synopsis: 'Lorem ipsum dolor sit amet.',
  };

  return (
    <div className='center'>
      <img src={movie.poster} alt={movie.title} />
      <h2>{movie.title}</h2>
      <p>Genre: {movie.genre}</p>
      <p>Release Year: {movie.releaseYear}</p>
      <p>Rating: {movie.rating}</p>
      <p>Cast: {movie.cast.join(', ')}</p>
      <p>Synopsis: {movie.synopsis}</p>
      <button>Add to Cart</button>
    </div>
  );
};

export default MovieDetails;
