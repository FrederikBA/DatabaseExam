USE BockBluster;

CREATE TABLE movie (
  movie_id VARCHAR(255) PRIMARY KEY,
  price_id INT,
  title VARCHAR(255),
  release_year INT,
  rating FLOAT,
  poster VARCHAR(255)
);

CREATE TABLE price (
  price_id INT PRIMARY KEY,
  price FLOAT
);

CREATE TABLE member (
  member_id VARCHAR(255) PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  join_date DATE
);

CREATE TABLE user_login (
  user_id INT PRIMARY KEY,
  member_id VARCHAR(255),
  username VARCHAR(255),
  password VARCHAR(255),
  FOREIGN KEY (member_id) REFERENCES member (member_id)
);

CREATE TABLE orders (
  order_id VARCHAR(255) PRIMARY KEY,
  member_id VARCHAR(255),
  total_price FLOAT,
  FOREIGN KEY (member_id) REFERENCES member (member_id)
)

CREATE TABLE loan (
  loan_id VARCHAR(255) PRIMARY KEY,
  order_id VARCHAR(255),
  movie_id VARCHAR(255),
  loan_date DATE,
  return_date DATE,
  FOREIGN KEY (order_id) REFERENCES orders (order_id),
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
);

ALTER TABLE user_login ADD CONSTRAINT FK_user_login_member
  FOREIGN KEY (member_id) REFERENCES member (member_id);

ALTER TABLE movie ADD CONSTRAINT FK_movie_price
  FOREIGN KEY (price_id) REFERENCES price (price_id);

ALTER TABLE loan ADD CONSTRAINT FK_loan_orders
  FOREIGN KEY (order_id) REFERENCES orders (order_id);

ALTER TABLE loan ADD CONSTRAINT FK_loan_movie
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id);

ALTER TABLE orders ADD CONSTRAINT FK_orders_member
  FOREIGN KEY (member_id) REFERENCES member (member_id);

