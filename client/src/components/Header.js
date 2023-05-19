import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import Logo from './Logo';



const Header = ({ isLoggedIn, onLogout }) => {
    const navigate = useNavigate();

    const onClick = () => {
        onLogout()
        navigate('/')
    }

    return (
        <div>
            <nav>
                <ul className='header'>
                    <NavLink className="none" to="/"><Logo /></NavLink>
                    <li className="frontpage-nav"><NavLink to='/'>Film</NavLink></li>
                    <li><NavLink to="/searchfilter">Søg Film</NavLink></li>
                    <li><NavLink to="/movielist">Film Liste</NavLink></li>
                    <li><NavLink to="/moviedetails">Film Detaljer</NavLink></li>
                    <li><NavLink to="/cart">Indkøbskurv</NavLink></li>
                    {!isLoggedIn && <li className="align-right login-nav"><NavLink to="/login">Log ind</NavLink></li>}
                    {isLoggedIn && <li onClick={onClick} className='align-right login-nav'><NavLink to="/">Log ud</NavLink></li>}
                </ul>
            </nav>
        </div >
    )
}

export default Header;
