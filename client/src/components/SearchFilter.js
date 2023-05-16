import React, { useState } from 'react';

const SearchFilter = () => {
  const [searchValue, setSearchValue] = useState('');
  const [filterValue, setFilterValue] = useState('');

  const handleSearchChange = (e) => {
    setSearchValue(e.target.value);
  };

  const handleFilterChange = (e) => {
    setFilterValue(e.target.value);
  };

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
    </div>
  );
};

export default SearchFilter;