import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { useState } from "react";

//Views
import Frontpage from './views/Frontpage';
import LandingPage from "./views/LandingPage";
import MovieSearch from "./views/MovieSearch";
import Login from "./views/Login";
import MovieList from "./views/MovieList";

//Components
import Header from './components/Header';
import MovieDetails from "./components/MovieDetails";
import Cart from "./components/Cart";
import CartNew from "./components/Cart";
import Posters from "./components/Posters";
import GenreDropdown from "./components/GenreDropdown";


const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (

    <BrowserRouter>
      <Header isLoggedIn={isLoggedIn} onLogout={() => { localStorage.clear(); setIsLoggedIn(false) }} />
      <Routes>
        <Route path="/" element={<Frontpage />} />
        <Route path="/login" element={<Login onLogin={() => setIsLoggedIn(true)} />} />
        <Route path="/landing-page" element={<LandingPage />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/search" element={<MovieSearch />} />
        <Route path="/moviedetails" element={<MovieDetails />} />
        <Route path="/" element={<Posters />} />
        <Route path="/movies/:movieId" element={<MovieDetails />} />
        <Route path="/moviegenre" element={<MovieList />} />
      </Routes>
      <HelmetProvider>
        <Helmet
          bodyAttributes={{
            style: 'background: radial-gradient(circle, rgba(2,0,36,1) 0%, rgba(9,9,34,1) 35%, rgba(10,9,40,1) 100%); color: white;'
          }}
        />
      </HelmetProvider>
    </BrowserRouter>
  );
}

export default App;