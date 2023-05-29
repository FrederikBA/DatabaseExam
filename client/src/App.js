import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { useState } from "react";

//Views
import Frontpage from './views/Frontpage';
import LandingPage from "./views/LandingPage";
import MovieSearch from "./views/MovieSearch";
import Login from "./views/Login";
import Register from "./views/Register";
import OrderConfirmation from "./views/OrderConfirmation";
import MovieDetails from "./views/MovieDetails";
import Profile from "./views/Profile";
import Cart from "./views/Cart";


//Components
import Header from './components/Header';
import Posters from "./components/Posters";


const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (

    <BrowserRouter>
      <Header isLoggedIn={isLoggedIn} onLogout={() => { localStorage.clear(); setIsLoggedIn(false) }} />
      <Routes>
        <Route path="/" element={<Frontpage />} />
        <Route path="/login" element={<Login onLogin={() => setIsLoggedIn(true)} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/landing-page" element={<LandingPage />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/search" element={<MovieSearch />} />
        <Route path="/" element={<Posters />} />
        <Route path="/movies/id/:movieId" element={<MovieDetails />} />
        <Route path="/order/:orderId" element={<OrderConfirmation />} />
        <Route path="/profile/:userId" element={<Profile />} />
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