DROP TABLE bookings;
DROP TABLE members;
DROP TABLE lessons;

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    date DATE,
    time TIME,
    description VARCHAR (255),
    duration INT,
    capacity INT,
    booked INT
);

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    last VARCHAR,
    first VARCHAR, 
    type VARCHAR
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    lesson_id INT REFERENCES lessons(id) ON DELETE CASCADE,
    member_id INT REFERENCES members(id) ON DELETE CASCADE, 
    UNIQUE (member_id, lesson_id)
);