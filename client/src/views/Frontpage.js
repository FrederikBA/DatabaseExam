import React, { useState, useEffect } from 'react';
import apiUtils from '../utils/apiUtils';

import Posters from '../components/Posters';
import Pagination from '../components/Pagination';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


const Movies = () => {
    const [movies, setMovies] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);

    const moviesPerPage = 50

    const URL = apiUtils.getUrl()

    useEffect(() => {
        const getMovies = async () => {
            const response = await apiUtils.getAxios().get(URL + '/movies')
            setMovies(response.data)
            setIsLoading(false)
        }
        getMovies()
    }, [URL]);

    // Toast
    //Toast
    const rentNotifySuccess = () => {
        toast.success('Movie added to cart!', { position: toast.POSITION.BOTTOM_RIGHT });
    };

    const rentNotifyError = () => {
        toast.error('There was an error adding the movie to cart', { position: toast.POSITION.BOTTOM_RIGHT });
    };

    // Get current movies
    const indexOfLastMovie = currentPage * moviesPerPage;
    const indexOfFirstMovie = indexOfLastMovie - moviesPerPage;
    const currentMovies = movies.slice(indexOfFirstMovie, indexOfLastMovie);

    // Change page
    const paginate = (pageNumber) => {
        setCurrentPage(pageNumber);
    }
    return (
        <div className='container mt-5'>
            <Pagination
                moviesPerPage={moviesPerPage}
                totalMovies={movies.length}
                currentPage={currentPage}
                paginate={paginate}
            />
            <Posters movies={currentMovies} isLoading={isLoading} rentNotifySuccess={rentNotifySuccess} rentNotifyError={rentNotifyError} />
            <ToastContainer />
        </div>
    )
}

export default Movies