import { NavLink } from "react-router-dom";

const Header = () => {
  return (
    <div>
      <nav>
        <ul className="header">
          <li>
            <NavLink to="/login">login</NavLink>
          </li>
          <li>
            <NavLink to="/searchfilter">search filter</NavLink>
          </li>
          <li>
            <NavLink to="/movielist">movie list</NavLink>
          </li>
          <li>
            <NavLink to="/moviedetails">movie details</NavLink>
          </li>
          <li>
            <NavLink to="/cart">cart</NavLink>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Header;
