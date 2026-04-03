CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    src VARCHAR(50),
    dst VARCHAR(50),
    amount NUMERIC,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    label INT
);
