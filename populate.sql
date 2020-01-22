DELETE FROM Student;
INSERT INTO Student (student_id, student_name, student_surname, student_course, student_studybook)
VALUES (1, 'Ivan', 'Ivanov', 2, 222);
INSERT INTO Student (student_id, student_name, student_surname, student_course, student_studybook)
VALUES (2, 'Oleg', 'Nebamzurov', 4, 123);
INSERT INTO Student (student_id, student_name, student_surname, student_course, student_studybook)
VALUES (3, 'Petro', 'Petrov', 4, 999);
SELECT * FROM Student;

DELETE FROM Subject;
INSERT INTO Subject (subject_id, subject_name)
VALUES (1, 'Physics');
INSERT INTO Subject (subject_id, subject_name)
VALUES (2, 'Math');
INSERT INTO Subject (subject_id, subject_name)
VALUES (3, 'Biology');
SELECT * FROM Subject;

DELETE FROM Lab;
INSERT INTO Lab (lab_id, subject_id, lab_number)
VALUES (1, 1, 1);
INSERT INTO Lab (lab_id, subject_id, lab_number)
VALUES (2, 1, 2);
INSERT INTO Lab (lab_id, subject_id, lab_number)
VALUES (3, 1, 3);
SELECT * FROM Lab;

DELETE FROM Lab_result;
INSERT INTO Lab_result (lab_result_id, lab_id, student_id, is_passed)
VALUES (1, 1, 1, true);
INSERT INTO Lab_result (lab_result_id, lab_id, student_id, is_passed)
VALUES (2, 2, 1, true);
INSERT INTO Lab_result (lab_result_id, lab_id, student_id, is_passed)
VALUES (3, 3, 1, true);
SELECT * FROM Lab_result;

DELETE FROM Skill;
INSERT INTO Skill (skill_id, subject_id, skill_grade)
VALUES (1, 1, 'A++');
INSERT INTO Skill (skill_id, subject_id, skill_grade)
VALUES (2, 2, 'B');
INSERT INTO Skill (skill_id, subject_id, skill_grade)
VALUES (3, 3, 'C');
SELECT * FROM Skill;

DELETE FROM Student_skill;
INSERT INTO Student_skill (student_id, skill_id)
VALUES (1, 1);
INSERT INTO Student_skill (student_id, skill_id)
VALUES (1, 2);
INSERT INTO Student_skill (student_id, skill_id)
VALUES (1, 3);
SELECT * FROM Student_skill;