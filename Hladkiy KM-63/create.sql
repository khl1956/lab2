CREATE TABLE Users
(
    user_id INTEGER PRIMARY KEY,
	lesson_name CHARACTER VARYING(30),
    user_name CHARACTER VARYING(30),
	user_surname CHARACTER VARYING(30),
	user_email CHARACTER VARYING(30),
	user_groupe CHARACTER VARYING(30),
	user_faculty CHARACTER VARYING(30),
    user_course INTEGER
);

CREATE TABLE Building
(
    build_number INTEGER PRIMARY KEY,
	build_adress CHARACTER VARYING(30),
	floors_number INTEGER
);

CREATE TABLE Classroom
(
	classroom_number INTEGER PRIMARY KEY,
	lesson_name CHARACTER VARYING(30),
	build_number INTEGER
);

CREATE TABLE Lesson
(
	lesson_name CHARACTER VARYING(30) PRIMARY KEY,
	classroom_number INTEGER,
	build_number INTEGER	
);