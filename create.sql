CREATE TABLE Student(
	student_id serial PRIMARY KEY,
	student_name text NOT NULL,
	student_surname text,
	student_course int NOT NULL DEFAULT 1 CONSTRAINT student_course_valid CHECK (student_course > 0 and student_course < 7),
	student_studybook int NOT NULL
);

CREATE TABLE Lab_result(
	lab_result_id serial PRIMARY KEY,
	lab_id int,
	student_id int REFERENCES Student(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
	is_passed BOOL NOT NULL
);

CREATE TABLE Lab(
	lab_id serial PRIMARY KEY,
	subject_id int,
	lab_number int NOT NULL DEFAULT 1 CONSTRAINT lab_number_valid CHECK (lab_number > 0)
);

ALTER TABLE Lab_result 
ADD CONSTRAINT Lab_result_lab_fk FOREIGN KEY (lab_id) REFERENCES Lab(lab_id) ON UPDATE CASCADE ON DELETE SET NULL;

CREATE TABLE Subject(
	subject_id serial PRIMARY KEY,
	subject_name text NOT NULL
);

ALTER TABLE Lab
ADD CONSTRAINT Lab_subject_fk FOREIGN KEY (subject_id) REFERENCES Subject(subject_id) ON UPDATE CASCADE ON DELETE SET NULL;

CREATE TABLE Skill(
	skill_id serial PRIMARY KEY,
	subject_id int REFERENCES Subject(subject_id) ON UPDATE CASCADE ON DELETE SET NULL,
	skill_grade VARCHAR(3)
);

CREATE TABLE Student_skill(
	student_id int REFERENCES Student(student_id) ON UPDATE CASCADE ON DELETE CASCADE,
	skill_id int REFERENCES Skill(skill_id) ON UPDATE CASCADE ON DELETE CASCADE,
	CONSTRAINT student_skill_id PRIMARY KEY (student_id, skill_id)
);