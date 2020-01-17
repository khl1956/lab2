insert into Users (user_id, lesson_name, user_name, user_surname, user_email, user_groupe, user_faculty, user_course) values ('1','Matan', 'Andriy', 'Hladkiy', 'andriyha98@gmail.com', 'KM-63', 'FPM', '4');

insert into Users (user_id, lesson_name, user_name, user_surname, user_email, user_groupe, user_faculty, user_course) values ('2','DB', 'Michael', 'Evlentyev', 'Michael403@gmail.com', 'KM-62', 'FPM', '4');

insert into Users (user_id, lesson_name, user_name, user_surname, user_email, user_groupe, user_faculty, user_course) values ('3','Matan', 'Ihor', 'Ryasik', 'Ihor99@gmail.com', 'KM-63', 'FPM', '4');

insert into Users (user_id, lesson_name, user_name, user_surname, user_email, user_groupe, user_faculty, user_course) values ('4','SDA', 'David', 'Savickiy', 'david_228_420@gmail.com', 'KP-92', 'FPM', '4');

insert into Building (build_number, build_adress, floors_number) values ('15', 'Politehnicha 20', '5');

insert into Building (build_number, build_adress, floors_number) values ('21', 'Borchagivska 31', '7');

insert into Building (build_number, build_adress, floors_number) values ('14', 'Politehnicha 19', '5');

insert into Building (build_number, build_adress, floors_number) values ('7', 'yakas tam 50', '7');

insert into Classroom (classroom_number, lesson_name, build_number) values ('94', 'Matan', '15');

insert into Classroom (classroom_number, lesson_name, build_number) values ('720', 'DB', '21');

insert into Classroom (classroom_number, lesson_name, build_number) values ('96', 'SDA', '15');

insert into Classroom (classroom_number, lesson_name, build_number) values ('302', 'KNTMF', '7');

insert into Lesson (lesson_name, classroom_number, build_number) values ('Matan', '94', '15');

insert into Lesson (lesson_name, classroom_number, build_number) values ('DB', '720', '21');

insert into Lesson (lesson_name, classroom_number, build_number) values ('SDA', '96', '15');

insert into Lesson (lesson_name, classroom_number, build_number) values ('KNTMF', '302', '7');