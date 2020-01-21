insert into User (user_email, user_name, user_phone, user_birthday) values ('maria@gmail.com', 'Maria', '+380669983855', '1999-4-7');

insert into User (user_email, user_name, user_phone, user_birthday) values ('bob@gmail.com', 'Bob', '+380123456789', '2000-1-20');

insert into User (user_email, user_name, user_phone, user_birthday) values ('kate@gmail.com', 'Kate', '+123456789011', '1998-2-25');

insert into User (user_email, user_name, user_phone, user_birthday) values ('alex@gmail.com', 'Alex', '+380999999999', '1997-2-25');

insert into User (user_email, user_name, user_phone, user_birthday) values ('sam@gmail.com', 'Sam', '+380777777777', '1999-2-1');

insert into Presentation (presentation_name, user_email, presentation_date) values ('Sales', 'alex@gmail.com', '2020-1-4');

insert into Presentation (presentation_name, user_email, presentation_date) values ('DataBase', 'bob@gmail.com', '2020-1-8');

insert into Presentation (presentation_name, user_email, presentation_date) values ('Music', 'maria@gmail.com', '2020-1-12');

insert into Presentation (presentation_name, user_email, presentation_date) values ('Maths', 'alex@gmail.com', '2020-1-29');

insert into Presentation (presentation_name, user_email, presentation_date) values ('Sports', 'alex@gmail.com', '2020-2-1');

insert into Participant (participant_list, participant_name) values ('Science_Maths', 'Alex, Bob');

insert into Participant (participant_list, participant_name) values ('Art_Music', 'Maria');

insert into Participant (participant_list, participant_name) values ('Computer_DataBase', 'Alex, Bob, Sam');

insert into Participant (participant_list, participant_name) values ('Business_Sales', 'Maria');

insert into Participant (participant_list, participant_name) values ('Math_Maths', 'Bob, Sam');

insert into Topic (topic_name, presentation_name) values ('Art', 'Music');

insert into Topic (topic_name, presentation_name) values ('Science', 'Maths');

insert into Topic (topic_name, presentation_name) values ('Math', 'Maths');

insert into Topic (topic_name, presentation_name) values ('Computer', 'DataBase');

insert into Topic (topic_name, presentation_name) values ('Business', 'Sales');
