import { useState, useEffect } from "react"
import apiUtils from "../utils/apiUtils";

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faRemove } from '@fortawesome/free-solid-svg-icons'

const Cart = () => {
    const [cartItems, setCartItems] = useState([]);
    const [totalPrice, setTotalPrice] = useState(0);

    const trashIcon = <FontAwesomeIcon icon={faRemove} size="2x" />

    const URL = apiUtils.getUrl()
    const userId = localStorage.getItem('userId')

    const getCart = async () => {
        const response = await apiUtils.getAxios().get(URL + `/get_cart?user_id=${userId}`)
        setCartItems(response.data.cartItems.movies);
        setTotalPrice(response.data.cartItems.totalPrice)
    }
    useEffect(() => {
        getCart();
    }, []);

    const handleRemove = async (itemId) => {
        await apiUtils.getAxios().post(`${apiUtils.getUrl()}/removefromcart`, {
            user_id: userId,
            movie_id: itemId,
        });
        getCart();
    };


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
                                <h3 className="cart-title">{item.title}</h3>
                                <div className="cart-loan"><span className="cart-date"><strong>Lejes til:</strong> {formattedDate}</span></div>
                            </div>
                            <div className="col cart-col">
                                <div onClick={() => handleRemove(item.movie_id)} className="cart-remove cart-item-details">{trashIcon}</div>
                                <div className="cart-price cart-item-details"><strong>{item.price} kr</strong></div>
                            </div>
                        </div>
                    </div>
                </div >
            ))}
            <div className="checkout-total-price">I alt: <strong>{totalPrice} kr</strong></div>
            <br></br>
            <br></br>
            <button className="btn btn-primary checkout-button">Lej film</button>
        </div>

    )
}

export default Cart