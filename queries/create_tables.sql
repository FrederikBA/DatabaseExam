CREATE TABLE movie (
  movie_id INT PRIMARY KEY,
  title VARCHAR(255),
  isan VARCHAR(255),
  release_date DATE,
);

CREATE TABLE actor (
  actor_id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE director (
  director_id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE publisher (
  publisher_id INT PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE movie_author (
  movie_id INT,
  director_id INT,
  PRIMARY KEY (movie_id, director_id),
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
  FOREIGN KEY (director_id) REFERENCES director (director_id)
);

CREATE TABLE movie_actor (
  movie_id INT,
  actor_id INT,
  PRIMARY KEY (movie_id, actor_id),
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
  FOREIGN KEY (actor_id) REFERENCES actor (actor_id)
);

CREATE TABLE genre (
  genre_id INT PRIMARY KEY,
  genre_name VARCHAR(255)
);

CREATE TABLE movie_genre (
  movie_id INT,
  genre_id INT,
  PRIMARY KEY (movie_id, genre_id),
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
  FOREIGN KEY (genre_id) REFERENCES genre (genre_id)
);

CREATE TABLE member (
  member_id INT PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  address VARCHAR(255),
  phone_number VARCHAR(255),
  join_date DATE
);

CREATE TABLE user_login (
  user_id INT PRIMARY KEY,
  member_id INT,
  username VARCHAR(255),
  password VARCHAR(255),
  FOREIGN KEY (member_id) REFERENCES member (member_id)
);

CREATE TABLE loan (
  loan_movie_id INT PRIMARY KEY,
  movie_id INT,
  member_id INT,
  loan_date DATE,
  return_date DATE,
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
  FOREIGN KEY (member_id) REFERENCES member (member_id)
);

CREATE TABLE movie_publishers (
  movie_id INT,
  publisher_id INT,
  PRIMARY KEY (movie_id, publisher_id),
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id),
  FOREIGN KEY (publisher_id) REFERENCES publisher (publisher_id)
);

ALTER TABLE movie ADD CONSTRAINT FK_movie_publisher
  FOREIGN KEY (publisher_id) REFERENCES publisher (publisher_id);

ALTER TABLE user_login ADD CONSTRAINT FK_user_login_member
  FOREIGN KEY (member_id) REFERENCES member (member_id);

ALTER TABLE movie_author ADD CONSTRAINT FK_movie_author_movie
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id);

ALTER TABLE movie_author ADD CONSTRAINT FK_movie_author_director
  FOREIGN KEY (director_id) REFERENCES director (director_id);

ALTER TABLE movie_actor ADD CONSTRAINT FK_movie_actor_movie
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id);

ALTER TABLE movie_actor ADD CONSTRAINT FK_movie_actor_actor
  FOREIGN KEY (actor_id) REFERENCES actor (actor_id);

ALTER TABLE movie_genre ADD CONSTRAINT FK_movie_genre_movie
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id);

ALTER TABLE movie_genre ADD CONSTRAINT FK_movie_genre_genre
  FOREIGN KEY (genre_id) REFERENCES genre (genre_id);

ALTER TABLE loan ADD CONSTRAINT FK_loan_movie
  FOREIGN KEY (movie_id) REFERENCES movie (movie_id);

ALTER TABLE loan ADD CONSTRAINT FK_loan_member
  FOREIGN KEY (member_id) REFERENCES member (member_id);