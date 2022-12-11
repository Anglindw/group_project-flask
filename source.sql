CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(250),
    password VARCHAR(500),
    admin BOOLEAN
); 

CREATE TABLE cart (
    user_id INT REFERENCES users(id),
    items JSON
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100),
    item_icon VARCHAR(250),
    item_description VARCHAR(5000),
    item_price FLOAT
);

