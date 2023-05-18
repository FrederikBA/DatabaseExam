import React from 'react';

const Pagination = ({ moviesPerPage, totalMovies, currentPage, paginate }) => {
    const pageNumbers = [];
    const totalPages = Math.ceil(totalMovies / moviesPerPage);

    const maxPageLinks = 5;

    let startPage = Math.max(1, currentPage - Math.floor(maxPageLinks / 2));
    let endPage = Math.min(startPage + maxPageLinks - 1, totalPages);

    startPage = Math.max(1, endPage - maxPageLinks + 1);

    for (let i = startPage; i <= endPage; i++) {
        pageNumbers.push(i);
    }

    return (
        <div className="pagination-container">
            <nav>
                <ul className="pagination">
                    {currentPage !== 1 && (
                        <li className="page-item">
                            <button onClick={() => paginate(currentPage - 1)} className="page-link">
                                <span>&#8249;</span>
                            </button>
                        </li>
                    )}

                    {startPage !== 1 && (
                        <li className="page-item">
                            <button onClick={() => paginate(1)} className="page-link">
                                1
                            </button>
                        </li>
                    )}

                    {pageNumbers.map((number) => (
                        <li key={number} className={`page-item ${number === currentPage ? 'active' : ''}`}>
                            <button onClick={() => paginate(number)} className="page-link">
                                {number}
                            </button>
                        </li>
                    ))}
                    {endPage !== totalPages && (
                        <li className="page-item">
                            <button onClick={() => paginate(totalPages)} className="page-link">
                                {totalPages}
                            </button>
                        </li>
                    )}

                    {currentPage !== totalPages && (
                        <li className="page-item">
                            <button onClick={() => paginate(currentPage + 1)} className="page-link">
                                <span>&#8250;</span>
                            </button>
                        </li>
                    )}
                </ul>
            </nav>
        </div>
    );
};

export default Pagination;
