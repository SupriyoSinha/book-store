INSERT INTO users (name, email)
VALUES
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com'),
('Charlie Brown', 'charlie@example.com'),
('Diana Prince', 'diana@example.com'),
('Ethan Hunt', 'ethan@example.com')
ON CONFLICT (email) DO NOTHING;

INSERT INTO users (id, name, email)
SELECT 
    gen_random_uuid(),
    name,
    lower(replace(name, ' ', '')) || '@gmail.com'
FROM (VALUES
('Amit Sharma'), ('Priya Verma'), ('Rahul Singh'), ('Sneha Iyer'),
('Arjun Mehta'), ('Neha Kapoor'), ('Rohit Gupta'), ('Pooja Nair'),
('Karan Malhotra'), ('Anjali Das'), ('Vikram Joshi'), ('Meera Pillai'),
('Suresh Reddy'), ('Kavita Mishra'), ('Nitin Agarwal'),
('Deepak Yadav'), ('Shalini Roy'), ('Rakesh Jain'),
('Sunita Patil'), ('Manoj Tiwari'), ('Aakash Bansal'),
('Divya Khanna'), ('Gaurav Saxena'), ('Anita Kulkarni'),
('Varun Chatterjee'), ('Isha Arora'), ('Tarun Sinha'),
('Nidhi Srivastava'), ('Harish Shetty'), ('Komal Batra')
) AS t(name);