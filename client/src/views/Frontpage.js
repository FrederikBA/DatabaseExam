import React, { useState, useEffect } from 'react';
import apiUtils from '../utils/apiUtils';

import Posters from '../components/Posters';
import Pagination from '../components/Pagination';

import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowCircleUp, faArrowCircleDown, faCircleChevronDown } from '@fortawesome/free-solid-svg-icons'


const Movies = () => {
    const [movies, setMovies] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const arrowUp = <FontAwesomeIcon icon={faArrowCircleUp} size="2x" />
    const arrowDown = <FontAwesomeIcon icon={faArrowCircleDown} size="2x" />
    const dropDown = <FontAwesomeIcon icon={faCircleChevronDown} size="2x" />

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
    const rentNotifySuccess = () => {
        toast.success('Din film er tilføjet til kurven', { position: toast.POSITION.BOTTOM_RIGHT });
    };

    const rentNotifyError = () => {
        toast.error('Der opstod en fejl, din film blev ikke tilføjet', { position: toast.POSITION.BOTTOM_RIGHT });
    };

    const rentNotifyLogin = () => {
        toast.error('Du skal logge ind for at leje en film', { position: toast.POSITION.BOTTOM_RIGHT });
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
            <div className="sort-container container">
                <div className="row">
                    <div className="sort-item col"><span className="sort-title">Sort by release date</span><button className="btn sort-arrow">{arrowUp}</button> <button className="btn sort-arrow">{arrowDown}</button></div>
                    <div className="sort-item col"><span className="sort-title">Sort by rating </span><button className="btn sort-arrow">{arrowUp}</button> <button className="btn sort-arrow">{arrowDown}</button></div>
                    <div className="sort-item col"><span className="sort-title">Sort by runtime</span><button className="btn sort-arrow">{arrowUp}</button> <button className="btn sort-arrow">{arrowDown}</button></div>
                    <div className="sort-item col"><span className="sort-title">Sort by price</span><button className="btn sort-arrow">{arrowUp}</button> <button className="btn sort-arrow">{arrowDown}</button></div>
                    <div className="sort-item col"><span className="sort-title">Sort by genre</span><button className="btn sort-arrow">{dropDown}</button></div>
                </div>
            </div>
            <Posters movies={currentMovies} isLoading={isLoading} rentNotifySuccess={rentNotifySuccess} rentNotifyError={rentNotifyError} rentNotifyLogin={rentNotifyLogin} />
            <ToastContainer />
        </div>
    )
}

export default Movies