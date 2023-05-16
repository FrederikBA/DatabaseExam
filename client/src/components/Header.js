import { NavLink } from "react-router-dom";
import Logo from './Logo';



const Header = () => {
    return (
        <div>
            <nav>
                <ul className='header'>
                    <Logo />
                    <li><NavLink to='/'>Film</NavLink></li>
                    <li><NavLink to='/rent'>Lej en film</NavLink></li>
                    <li><NavLink to="/login">login</NavLink></li>
                    <li><NavLink to="/searchfilter">Søg Film</NavLink></li>
                    <li><NavLink to="/movielist">Film Liste</NavLink></li>
                    <li><NavLink to="/moviedetails">Film Detaljer</NavLink></li>
                    <li><NavLink to="/cart">Indkøbskurv</NavLink></li>
                </ul>
            </nav>
        </div >
    )
}

export default Header;
