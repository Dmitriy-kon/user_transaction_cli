CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    hashed_password VARCHAR(255) NOT NULL
);
-- foreign key (name) references transactions(name)