import React, { useState, useEffect } from 'react';
import apiUtils from '../utils/apiUtils';

const GenreDropdown = ({ onSelectGenre }) => {
  const [genres, setGenres] = useState([]);
  const [selectedGenre, setSelectedGenre] = useState('');

  useEffect(() => {
    // Fetch the list of genres from your backend API
    const fetchGenres = async () => {
      try {
        const response = await apiUtils.getAxios().get(URL + `/movies/genre/${genres}`); 
        setGenres(response.data);
        console.log(response.data);
      } catch (error) {
        console.error('Error fetching genres:', error);
      }
    };

    fetchGenres();
  }, []);

  const handleGenreChange = (event) => {
    setSelectedGenre(event.target.value);
  };

  const handleButtonClick = () => {
    onSelectGenre(selectedGenre);
  };

  return (
    <div>
      <select value={selectedGenre} onChange={handleGenreChange}>
        <option value="">Select a genre</option>
        {genres.map((genre) => (
          <option key={genre} value={genre}>
            {genre}
          </option>
        ))}
      </select>
      <button onClick={handleButtonClick}>Get Movies</button>
    </div>
  );
};

export default GenreDropdown;
