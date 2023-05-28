import { useState, useEffect } from "react"
import apiUtils from "../utils/apiUtils"
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

import Posters from '../components/Posters';

const Profile = () => {

    const URL = apiUtils.getUrl()
    const [movies, setMovies] = useState([]);
    const [movieIds, setMovieIds] = useState([]);
    const [recommendedMovies, setRecommendedMovies] = useState([]);
    const [hoveredMovieId, setHoveredMovieId] = useState(null);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const getLoans = async () => {
            const response = await apiUtils.getAxios().get(URL + '/loans', {
                params: {
                    member_id: localStorage.getItem('memberId')
                }
            });
            const sorted = response.data.loans.sort((a, b) => {
                const dateA = new Date(a.loan_date);
                const dateB = new Date(b.loan_date);
                return dateB - dateA;
            });

            setMovies(sorted);
            setRecommendedMovies(response.data.recommendations)
            setIsLoading(false)
        }
        getLoans()
    }, []);

    const handleMovieClick = (movieId) => {
        window.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1", "_blank");
    };

    const handleMouseEnter = (movieId) => {
        setHoveredMovieId(movieId);
    };

    const handleMouseLeave = () => {
        setHoveredMovieId(null);
    };

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        const monthNames = ["Januar", "Februar", "Marts", "April", "Maj", "Juni", "Juli", "August", "September", "Oktober", "November", "December"];
        const month = monthNames[date.getMonth()];
        const day = date.getDate();
        const year = date.getFullYear();

        const formattedDate = `${day} ${month}, ${year}`;
        return formattedDate;
    }

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

    return (
        <div className='container mt-5'>
            <h3>Dine film</h3>
            <div className="row row-cols-5">
                {movies.map((movie) => (
                    <div key={movie.loan_id} className="col mb-4 poster" onMouseEnter={() => handleMouseEnter(movie.loan_id)}
                        onMouseLeave={handleMouseLeave}>
                        <img src={movie.poster} className="card-img-top" alt={movie.title} />
                        {hoveredMovieId === movie.loan_id ? (
                            <>
                                <button onClick={() => handleMovieClick()} className="btn stream-movie">Stream film</button>
                            </>
                        ) : null}

                        <div className="card-body center">
                            <p className="card-title">{movie.title} ({movie.release_year})</p>
                            <div className="poster-text">Lejet den: {formatDate(movie.loan_date)}</div>
                            <div className="poster-text">Udløber den: {formatDate(movie.return_date)}</div>
                        </div>
                    </div>
                ))}
            </div>
            <h3>Mere som dette</h3>
            <Posters movies={recommendedMovies} isLoading={isLoading} rentNotifySuccess={rentNotifySuccess} rentNotifyError={rentNotifyError} rentNotifyLogin={rentNotifyLogin} />
            <ToastContainer />
        </div>
    )
}

export default Profile