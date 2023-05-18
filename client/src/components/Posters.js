import React from 'react';

const Posters = ({ movies, isLoading }) => {
    if (isLoading) {
        return <h2>Loading...</h2>;
    }

    return (
        <div className="poster row row-cols-5">
            {movies.map((movie) => (
                <div key={movie.movie_id} className="col mb-4">
                    <div className="">
                        <img src={movie.poster} className="card-img-top" alt={movie.title} />
                        <div className="card-body center">
                            <p className="card-title">{movie.title}</p>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    );
};

export default Posters;
