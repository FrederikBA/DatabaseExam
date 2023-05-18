import React, { useState, useEffect } from 'react';
import apiUtils from '../utils/apiUtils';

import Posters from '../components/Posters';
import Pagination from '../components/Pagination';


const Movies = () => {
    const [movies, setMovies] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const [moviesPerPage, setMoviesPerPage] = useState(50);

    const URL = apiUtils.getUrl()

    useEffect(() => {
        const getMovies = async () => {
            const response = await apiUtils.getAxios().get(URL + '/movies')
            setMovies(response.data)
            setIsLoading(false)
        }
        getMovies()
    }, [URL]);

    // Get current movies
    const indexOfLastMovie = currentPage * moviesPerPage;
    const indexOfFirstMovie = indexOfLastMovie - moviesPerPage;
    const currentMovies = movies.slice(indexOfFirstMovie, indexOfLastMovie);

    // Change page
    const paginate = pageNumber => setCurrentPage(pageNumber);

    return (
        <div className='container mt-5'>
            <Posters movies={currentMovies} isLoading={isLoading} />
            <Pagination
                moviesPerPage={moviesPerPage}
                totalMovies={movies.length}
                currentPage={currentPage}
                paginate={paginate}
            />
        </div>
    )
}

export default Movies