import { BrowserRouter, Routes, Route, useHistory } from "react-router-dom";
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { useState } from "react";

//Views
import LandingPage from "./views/LandingPage";
import Frontpage from './views/Frontpage';
import Login from "./views/Login";

//Components
import Header from './components/Header';
import MovieList from "./components/MovieList";
import MovieDetails from "./components/MovieDetails";
import Cart from "./components/Cart";
import SearchFilter from "./components/SearchFilter";
import Posters from "./components/Posters";


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
        <Route path="/searchfilter" element={<SearchFilter />} />
        <Route path="/moviedetails" element={<MovieDetails />} />
        <Route path="/movielist" element={<MovieList />} />
        <Route path="/" element={<Posters />} />
        <Route path="/movies/:movieId" element={<MovieDetails />} />
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