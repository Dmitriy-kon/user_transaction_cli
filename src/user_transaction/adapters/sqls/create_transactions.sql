CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    amount BIGINT NOT NULL,
    type VARCHAR(10) NOT NULL,
    
    foreign key (name) 
    references users(name) 
    ON DELETE CASCADE
);