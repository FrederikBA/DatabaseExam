import { useState, useEffect } from "react"
import { useNavigate } from "react-router-dom";
import apiUtils from "../utils/apiUtils";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faRemove } from '@fortawesome/free-solid-svg-icons'

const Cart = () => {
    const [cartItems, setCartItems] = useState([]);
    const [totalPrice, setTotalPrice] = useState(0);
    const [isLoading, setIsLoading] = useState(true);
    const [movies, setMovies] = useState([{}]);
    const [memberId, setMemberId] = useState("");

    const navigate = useNavigate();
    const URL = apiUtils.getUrl()
    const userId = localStorage.getItem('userId')

    const deleteIcon = <FontAwesomeIcon icon={faRemove} size="2x" />

    const getCart = async () => {
        const response = await apiUtils.getAxios().get(URL + `/get_cart?user_id=${userId}`)
        setCartItems(response.data.movies);
        setTotalPrice(response.data.totalPrice)
        setMovies(response.data.movies)
        setIsLoading(false)
    }

    const getMemberId = async () => {
        const response = await apiUtils.getAxios().get(URL + `/member/${userId}`)
        setMemberId(response.data)
    }

    useEffect(() => {
        getCart();
        getMemberId();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    const handleRemove = async (itemId) => {
        await apiUtils.getAxios().post(`${apiUtils.getUrl()}/removefromcart`, {
            user_id: userId,
            movie_id: itemId,
        });
        getCart();
    };

    const isEmpty = () => {
        if (cartItems.length === 0 && isLoading === false) {
            return true
        } else {
            return false
        }
    }

    const clearCart = async () => {
        await apiUtils.getAxios().post(`${URL}/clearcart?user_id=${userId}`)
    }

    const purchase = async () => {
        try {
            const response = await apiUtils.getAxios().post(URL + '/order', {
                "movies": movies,
                "member_id": memberId,
                "total_price": totalPrice
            })
            //Clear cart
            clearCart()
            navigate('/order/' + response.data)
        } catch (error) {
            console.log(error);
        }
    }



    // Date stuff
    const currentDate = new Date();
    currentDate.setDate(currentDate.getDate() + 7);

    const monthNames = ["Januar", "Februar", "Marts", "April", "Maj", "Juni", "Juli", "August", "September", "Oktober", "November", "December"];
    const month = monthNames[currentDate.getMonth()];
    const day = currentDate.getDate();
    const year = currentDate.getFullYear();

    const formattedDate = `${(day)} ${month}, ${year}`;

    return (
        <div className="container checkout-container">
            {cartItems.map((item) => (
                <div className="cart-container" key={item.movie_id}>
                    <div className="cart-item container">
                        <div className="row">
                            <div className="col-2 cart-col">
                                <img className="cart-poster" src={item.poster} alt="cart-poster"></img>
                            </div>
                            <div className="col cart-col">
                                <h3 className="cart-title">{item.title} ({item.release_year})</h3>
                                <div className="cart-loan"><span className="cart-date"><strong>Lejes til:</strong> {formattedDate}</span></div>
                            </div>
                            <div className="col cart-col">
                                <div onClick={() => handleRemove(item.movie_id)} className="cart-remove cart-item-details">{deleteIcon}</div>
                                <div className="cart-price cart-item-details"><strong>{item.price} kr</strong></div>
                            </div>
                        </div>
                    </div>
                </div >
            ))}
            {!isEmpty() ? <div>
                <div className="checkout-total-price">I alt: <strong>{totalPrice} kr</strong></div>
                <br></br>
                <br></br>
                <button onClick={purchase} className="loginButton checkout-button">Lej film</button>
            </div>
                : <div className="center"><h1>Kurven er tom</h1></div>}
        </div>
    )
}

export default Cart