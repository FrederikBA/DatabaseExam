import { NavLink } from "react-router-dom";

import Logo from './Logo';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUser, faSearch } from '@fortawesome/free-solid-svg-icons'

const Header = ({ isLoggedIn, onLogout }) => {
    const userIcon = <FontAwesomeIcon icon={faUser} />
    const searchIcon = <FontAwesomeIcon icon={faSearch} />

    const onClick = () => {
        onLogout()
    }

    return (
        <div>
            <nav>
                <ul className='header'>
                    <NavLink className="none" to="/"><Logo /></NavLink>
                    <li className="frontpage-nav"><NavLink to='/'>Film</NavLink></li>
                    <li><NavLink to="/search">Søg {searchIcon}</NavLink></li>
                    <li><NavLink to="/cart">Indkøbskurv</NavLink></li>
                    {!isLoggedIn && <li className="align-right login-nav"><NavLink to="/login">Log ind</NavLink></li>}
                    {isLoggedIn && <div><li onClick={onClick} className='align-right login-nav'><NavLink to="/landing-page">Log ud</NavLink></li><li className="align-right"><span className="user-nav">{localStorage.getItem('user')} {userIcon}</span></li></div>}
                </ul>
            </nav>
        </div >
    )
}

export default Header;
