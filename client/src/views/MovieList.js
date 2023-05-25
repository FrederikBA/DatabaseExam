import React, { useState, useEffect } from 'react';
import GenreDropdown from '../components/GenreDropdown';
import apiUtils from '../utils/apiUtils';


const MovieList = () => {
  const [movies, setMovies] = useState([]);
  const [selectedGenre, setSelectedGenre] = useState('');

  const fetchMoviesByGenre = async (genre) => {
    try {
      const response = await apiUtils.getAxios().get(URL + `/api/movies/genre/${selectedGenre}`)
      setMovies(response.data);
    } catch (error) {
      console.error('Error fetching movies:', error);
    }
  };

  useEffect(() => {
    if (selectedGenre) {
      fetchMoviesByGenre(selectedGenre);
    }
  }, [fetchMoviesByGenre]);

  const handleSelectGenre = (genre) => {
    setSelectedGenre(genre);
  };

  return (
    <div>
      <h2>Movies</h2>
      <GenreDropdown onSelectGenre={handleSelectGenre} />
      {movies.length > 0 ? (
        <ul>
          {movies.map((movie) => (
            <li key={movie.title}>{movie.title}</li>
          ))}
        </ul>
      ) : (
        <p>No movies found.</p>
      )}
    </div>
  );
};

export default MovieList;
