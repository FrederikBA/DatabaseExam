import { useState, useEffect } from "react"
import apiUtils from "../utils/apiUtils"
import uuid from "react-uuid"

const Profile = () => {

    const URL = apiUtils.getUrl()
    const [movies, setMovies] = useState([]);
    const [hoveredMovieId, setHoveredMovieId] = useState(null);

    useEffect(() => {
        const getLoans = async () => {
            const response = await apiUtils.getAxios().get(URL + '/loans', {
                params: {
                    member_id: localStorage.getItem('memberId')
                }
            });
            const sorted = response.data.sort((a, b) => {
                const dateA = new Date(a.loan_date);
                const dateB = new Date(b.loan_date);
                return dateB - dateA;
            });

            setMovies(sorted);
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

    return (
        <div className='container mt-5'>
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
        </div>
    )
}

export default Profile