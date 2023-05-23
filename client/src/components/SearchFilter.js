import React, { useState, useEffect } from 'react';

const SearchFilter = () => {
  const [searchValue, setSearchValue] = useState('');
  const [filterValue, setFilterValue] = useState('');
  const [movies, setMovies] = useState([]);
  const [isSearchClicked, setIsSearchClicked] = useState(false);

  const handleSearchChange = (e) => {
    setSearchValue(e.target.value);
  };

  const handleFilterChange = (e) => {
    setFilterValue(e.target.value);
  };

  const handleSearchClick = () => {
    setIsSearchClicked(true);
  };

  useEffect(() => {
    const fetchMovies = async () => {
      if (isSearchClicked) {
        const response = await fetch(`http://127.0.0.1:8000/movies/title/${searchValue}`);
        const data = await response.json();
        setMovies(data);
        setIsSearchClicked(false);
      }
    };

    fetchMovies();
  }, [isSearchClicked]);

  return (
    <div className='center'>
      <input
        type="text"
        placeholder="Search movies..."
        value={searchValue}
        onChange={handleSearchChange}
      />
      <select value={filterValue} onChange={handleFilterChange}>
        <option value="">All Genres</option>
        <option value="action">Action</option>
        <option value="comedy">Comedy</option>
        <option value="drama">Drama</option>
      </select>

      <button onClick={handleSearchClick}>Search</button>

      <div className="movie-list">
        {movies.map((movie, index) => (
          <div key={index}>{movie}</div>
        ))}
      </div>
    </div>
  );
};

export default SearchFilter;
