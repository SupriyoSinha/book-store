INSERT INTO books (title, author, price)
VALUES
('Clean Code', 'Robert C. Martin', 499.00),
('The Pragmatic Programmer', 'Andrew Hunt', 599.00),
('Design Patterns', 'Erich Gamma', 699.00),
('Refactoring', 'Martin Fowler', 650.00),
('Domain-Driven Design', 'Eric Evans', 800.00)
ON CONFLICT DO NOTHING;