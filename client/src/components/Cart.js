import React from 'react';

const Cart = () => {
  const cartItems = [
    {
      id: 1,
      title: 'Movie 1',
      duration: 7,
      price: 9.99,
    },
    {
      id: 2,
      title: 'Movie 2',
      duration: 3,
      price: 4.99,
    },
    // Add more cart items as needed
  ];

  const handleRemove = (itemId) => {
    // Logic to remove the item from the cart
  };

  const handleDurationChange = (itemId, duration) => {
    // Logic to update the rental duration for the item
  };

  return (
    <div >
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
