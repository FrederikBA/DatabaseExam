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
                </ul>
            </nav>
        </div >
    )
}

export default Header;