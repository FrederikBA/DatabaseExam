import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Helmet, HelmetProvider } from 'react-helmet-async';

//Views
import Header from './components/Header';
import Login from "./views/Login";
import LandingPage from "./views/LandingPage";
import Movies from './views/Movies';
import Rent from './views/Rent';

//Components
import MovieList from "./components/MovieList";
import MovieDetails from "./components/MovieDetails";
import Cart from "./components/Cart";
import SearchFilter from "./components/SearchFilter";



const App = () => {

  return (

    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Movies />} />
        <Route path="/rent" element={<Rent />} />
        <Route path="/login" element={<Login />} />
        <Route path="/landing-page" element={<LandingPage />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/searchfilter" element={<SearchFilter />} />
        <Route path="/moviedetails" element={<MovieDetails />} />
        <Route path="/movielist" element={<MovieList />} />
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