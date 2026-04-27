-- Alice buys Clean Code
INSERT INTO purchases (user_id, book_id, quantity, total_price)
SELECT u.id, b.id, 1, b.price
FROM users u, books b
WHERE u.email = 'alice@example.com'
AND b.title = 'Clean Code';

-- Bob buys 2 copies of Design Patterns
INSERT INTO purchases (user_id, book_id, quantity, total_price)
SELECT u.id, b.id, 2, b.price * 2
FROM users u, books b
WHERE u.email = 'bob@example.com'
AND b.title = 'Design Patterns';

-- Diana buys Refactoring
INSERT INTO purchases (user_id, book_id, quantity, total_price)
SELECT u.id, b.id, 1, b.price
FROM users u, books b
WHERE u.email = 'diana@example.com'
AND b.title = 'Refactoring';

-- Ethan buys Pragmatic Programmer
INSERT INTO purchases (user_id, book_id, quantity, total_price)
SELECT u.id, b.id, 1, b.price
FROM users u, books b
WHERE u.email = 'ethan@example.com'
AND b.title = 'The Pragmatic Programmer';