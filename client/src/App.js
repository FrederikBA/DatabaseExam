import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './components/Header';
import Movies from './views/Movies';
import Rent from './views/Rent';


const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Movies />} />
        <Route path="/rent" element={<Rent />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;