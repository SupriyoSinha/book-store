INSERT INTO books (title, author, price)
VALUES
('Clean Code', 'Robert C. Martin', 499.00),
('The Pragmatic Programmer', 'Andrew Hunt', 599.00),
('Design Patterns', 'Erich Gamma', 699.00),
('Refactoring', 'Martin Fowler', 650.00),
('Domain-Driven Design', 'Eric Evans', 800.00)
ON CONFLICT DO NOTHING;


INSERT INTO books (id, title, author, price, total_copies, available_copies)
VALUES
(gen_random_uuid(), 'The Alchemist', 'Paulo Coelho', 399, 5, 5),
(gen_random_uuid(), '1984', 'George Orwell', 299, 4, 4),
(gen_random_uuid(), 'To Kill a Mockingbird', 'Harper Lee', 349, 3, 3),
(gen_random_uuid(), 'The Great Gatsby', 'F. Scott Fitzgerald', 250, 4, 4),
(gen_random_uuid(), 'Moby Dick', 'Herman Melville', 450, 2, 2),
(gen_random_uuid(), 'War and Peace', 'Leo Tolstoy', 599, 2, 2),
(gen_random_uuid(), 'Pride and Prejudice', 'Jane Austen', 299, 5, 5),
(gen_random_uuid(), 'The Hobbit', 'J.R.R. Tolkien', 399, 6, 6),
(gen_random_uuid(), 'Harry Potter and the Sorcerer''s Stone', 'J.K. Rowling', 499, 7, 7),
(gen_random_uuid(), 'The Catcher in the Rye', 'J.D. Salinger', 320, 3, 3),
(gen_random_uuid(), 'The Lord of the Rings', 'J.R.R. Tolkien', 799, 4, 4),
(gen_random_uuid(), 'Brave New World', 'Aldous Huxley', 350, 3, 3),
(gen_random_uuid(), 'The Da Vinci Code', 'Dan Brown', 399, 6, 6),
(gen_random_uuid(), 'Angels and Demons', 'Dan Brown', 399, 5, 5),
(gen_random_uuid(), 'The Kite Runner', 'Khaled Hosseini', 450, 4, 4),
(gen_random_uuid(), 'A Thousand Splendid Suns', 'Khaled Hosseini', 420, 4, 4),
(gen_random_uuid(), 'The Book Thief', 'Markus Zusak', 380, 3, 3),
(gen_random_uuid(), 'Sapiens', 'Yuval Noah Harari', 550, 6, 6),
(gen_random_uuid(), 'Homo Deus', 'Yuval Noah Harari', 550, 5, 5),
(gen_random_uuid(), 'Atomic Habits', 'James Clear', 499, 7, 7),
(gen_random_uuid(), 'Think and Grow Rich', 'Napoleon Hill', 300, 5, 5),
(gen_random_uuid(), 'Rich Dad Poor Dad', 'Robert Kiyosaki', 350, 6, 6),
(gen_random_uuid(), 'The Power of Habit', 'Charles Duhigg', 420, 4, 4),
(gen_random_uuid(), 'Ikigai', 'Hector Garcia', 299, 5, 5),
(gen_random_uuid(), 'The Subtle Art of Not Giving a F*ck', 'Mark Manson', 399, 6, 6),
(gen_random_uuid(), 'Deep Work', 'Cal Newport', 450, 4, 4),
(gen_random_uuid(), 'Zero to One', 'Peter Thiel', 350, 3, 3),
(gen_random_uuid(), 'Start With Why', 'Simon Sinek', 399, 4, 4),
(gen_random_uuid(), 'The Lean Startup', 'Eric Ries', 420, 5, 5),
(gen_random_uuid(), 'Clean Code', 'Robert C. Martin', 699, 3, 3);