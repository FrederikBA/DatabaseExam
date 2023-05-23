import React, { useState } from 'react';
import apiUtils from '../utils/apiUtils';

import Posters from '../components/Posters';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSearch } from '@fortawesome/free-solid-svg-icons'

const MovieSearch = () => {
  const [searchValue, setSearchValue] = useState('');
  const [movies, setMovies] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  const URL = apiUtils.getUrl()

  const searchIcon = <FontAwesomeIcon icon={faSearch} />

  const search = async () => {
    const response = await apiUtils.getAxios().get(URL + `/movies/title/${searchValue}`)
    setMovies(response.data);
    console.log(movies);
    setIsLoading(false)
  }

  const handleKeyDown = (event) => {
    if (event.key === 'Enter') {
      search();
    }
  };

  return (
    <div className='center'>
      <div className="text-area-div mt-2">
        <div className="text-area">
          <div className="input-group">
            <input type="search" onKeyDown={handleKeyDown} onChange={(e) => setSearchValue(e.target.value)} className="form-control border-end-0 border rounded-pill" id="searchInput" placeholder="Søg på film" />
            <span className="input-group-append">
              <div className="btn bg-white rounded-pill search-icon-input" type="button">
                <i></i>{searchIcon}
              </div>
            </span>
          </div>
        </div>
      </div>
      <div className='container mt-5'>
        <Posters movies={movies} isLoading={isLoading} />
      </div>

    </div>
  );
};

export default MovieSearch
