import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faArrowCircleUp, faArrowCircleDown } from '@fortawesome/free-solid-svg-icons'

const Sorting = ({ sortMovies }) => {
    const arrowUp = <FontAwesomeIcon icon={faArrowCircleUp} size="2x" />
    const arrowDown = <FontAwesomeIcon icon={faArrowCircleDown} size="2x" />

    return (
        <div className="sort-container container center">
            <div className="row">
                <div className="sort-item col"><span className="sort-title">Udgivelsesår</span><button onClick={() => sortMovies("ReleaseYear", "DESC")} className="btn sort-arrow">{arrowUp}</button> <button onClick={() => sortMovies("ReleaseYear", "ASC")} className="btn sort-arrow">{arrowDown}</button></div>
                <div className="sort-item col"><span className="sort-title">Bedømmelser</span><button onClick={() => sortMovies("Rating", "DESC")} className="btn sort-arrow">{arrowUp}</button> <button onClick={() => sortMovies("Rating", "ASC")} className="btn sort-arrow">{arrowDown}</button></div>
                <div className="sort-item col"><span className="sort-title">Filmlængde</span><button onClick={() => sortMovies("Runtime", "DESC")} className="btn sort-arrow">{arrowUp}</button> <button onClick={() => sortMovies("Runtime", "ASC")} className="btn sort-arrow">{arrowDown}</button></div>
                <div className="sort-item col"><span className="sort-title">Pris</span><button onClick={() => sortMovies("Price", "DESC")} className="btn sort-arrow">{arrowUp}</button> <button onClick={() => sortMovies("Price", "ASC")} className="btn sort-arrow">{arrowDown}</button></div>
            </div>
        </div>
    )
}

export default Sorting