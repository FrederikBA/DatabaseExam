import React, { useState, useEffect } from 'react';
import apiUtils from '../utils/apiUtils'; // Import apiUtils

const Cart = () => {
  const [cartItems, setCartItems] = useState([]);




  const fetchCartItems = async () => {
    const userId = 1; // This we need to get from the browsers storage.
    const response = await apiUtils.getAxios().get(`${apiUtils.getUrl()}/get_cart?user_id=${userId}`);
    const cartItemsObject = response.data.cartItems;
    const cartItemsArray = Object.keys(cartItemsObject).map((key) => {
      return { id: key, duration: cartItemsObject[key] };
    });
    setCartItems(cartItemsArray || []);

  };

  useEffect(() => {
    fetchCartItems();
  }, []);

  const handleRemove = async (itemId) => {
    const userId = 1; // This we need to get from the browsers storage.
    await apiUtils.getAxios().post(`${apiUtils.getUrl()}/removefromcart`, {
      user_id: userId,
      movie_id: itemId,
    });
    fetchCartItems(); // updating the state with the new cart
  };

  const handleDurationChange = async (itemId, duration) => {
    const userId = 1; // This we need to get from the browsers storage.
    await apiUtils.getAxios().post(`${apiUtils.getUrl()}/addtocart`, {
      user_id: userId,
      movie_id: itemId,
      duration: parseInt(duration, 10),
    });
    fetchCartItems(); // updating the state with the new cart
  };

  return (
    <div>
      <h1>Cart</h1>
      {cartItems.length === 0 ? (
        <p>No items in the cart</p>
      ) : (
        <ul>
          {cartItems.map((item) => (
            <li key={item.id}>
              <h3>{item.title}</h3>
              <p>Rental Duration: {item.duration} days</p>
              <p>Price: ${item.price}</p>
              <button onClick={() => handleRemove(item.id)}>Remove</button>
              <input
                type="number"
                min="1"
                value={item.duration}
                onChange={(e) => handleDurationChange(item.id, e.target.value)}
              />
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default Cart;
