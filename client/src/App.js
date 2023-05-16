import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './components/Header';
import Login from "./components/Login";
import MovieList from "./components/MovieList";
import One from './views/One';
import Two from './views/Two';
import MovieDetails from "./components/MovieDetails";
import Cart from "./components/Cart";
import SearchFilter from "./components/SearchFilter";

const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<One />} />
        <Route path="/two" element={<Two />} />
        <Route path="/moviedetails" element={<MovieDetails />} />
        <Route path="/movielist" element={<MovieList />} />
        <Route path="/login" element={<Login />} />
        <Route path="/cart" element={<Cart />} />
        <Route path="/searchfilter" element={<SearchFilter />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;