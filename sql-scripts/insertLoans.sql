
CREATE TABLE loans (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    book_id UUID NOT NULL,
    borrowed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    due_date TIMESTAMP NOT NULL,
    returned_at TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);


INSERT INTO loans (id, user_id, book_id, borrowed_at, due_date, returned_at)
SELECT
    gen_random_uuid(),
    u.id,
    b.id,
    NOW() - (random() * INTERVAL '7 days'),
    NOW() + INTERVAL '14 days',
    CASE 
        WHEN random() > 0.6 THEN NOW() - (random() * INTERVAL '3 days')
        ELSE NULL
    END
FROM users u
JOIN books b ON true
LIMIT 30;