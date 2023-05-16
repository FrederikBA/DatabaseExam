import React from 'react';

const MovieList = () => {
  const movies = [
    {
      id: 1,
      title: 'Movie 1',
      poster: 'poster1.jpg',
      description: 'Lorem ipsum dolor sit amet.',
      rating: 7.5,
    },
    {
      id: 2,
      title: 'Movie 2',
      poster: 'poster2.jpg',
      description: 'Lorem ipsum dolor sit amet.',
      rating: 8.2,
    },
    // Add more movies as needed
  ];

  return (
    <div className='center'>
      {movies.map((movie) => (
        <div key={movie.id}>
          <img src={movie.poster} alt={movie.title} />
          <h2>{movie.title}</h2>
          <p>{movie.description}</p>
          <p>Rating: {movie.rating}</p>
        </div>
      ))}
    </div>
  );
};

export default MovieList;
