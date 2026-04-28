-- USERS TABLE
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- BOOKS TABLE
CREATE TABLE books (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(255) NOT NULL,
    author VARCHAR(150) NOT NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


    CONSTRAINT fk_user
        FOREIGN KEY(user_id) REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_book
        FOREIGN KEY(book_id) REFERENCES books(id)
        ON DELETE CASCADE
);

ALTER TABLE books
ADD COLUMN total_copies INT DEFAULT 1,
ADD COLUMN available_copies INT DEFAULT 1;
-- PURCHASES TABLE
