from dao.orm.model import *


# очистка всех таблиц
db.session.query(association).delete()
db.session.query(Topic).delete()
db.session.query(Presentation).delete()
db.session.query(User).delete()
db.session.query(Hotel).delete()
db.session.query(Participant).delete()

## User

Maria = User(user_email = 'maria@gmail.com',
             user_name = 'Maria',
             user_phone = '+380669983855',
             user_birthday = "1999-4-7"
             )

Bob = User(user_email = 'bob@gmail.com',
             user_name = 'Bob',
             user_phone = '+380123456789',
             user_birthday = '2000-1-20'
             )

Kate = User(user_email = 'kate@gmail.com',
             user_name = 'Kate',
             user_phone = '+123456789011',
             user_birthday = '1998-2-25'
            )

Alex = User(user_email = 'alex@gmail.com',
             user_name = 'Alex',
             user_phone = '+380999999999',
             user_birthday = '1997-2-25'
            )

Sam = User(user_email = 'sam@gmail.com',
             user_name = 'Sam',
             user_phone = '+380777777777',
             user_birthday = '1999-2-1'
            )

#  Hotel

Hilton = Hotel(hotel_name = 'Hilton',
               hotel_opened = 2012,
               hotel_stars = 5,
               hotel_type = 'hotel'
               )

Intercontinental = Hotel(hotel_name = 'Intercontinental',
                         hotel_opened = 2010,
                         hotel_stars = 5,
                         hotel_type = 'hotel'
                         )

Kyiv = Hotel(hotel_name = 'Kyiv',
             hotel_opened = 2000,
             hotel_stars = 3,
             hotel_type = 'appartments'
             )

Youth = Hotel(hotel_name = 'Youth',
              hotel_opened = 2019,
              hotel_stars = 3,
              hotel_type = 'hostel'
              )

Kolos = Hotel(hotel_name = 'Kolos',
              hotel_opened = 2003,
              hotel_stars = 2,
              hotel_type = 'hostel'
              )

#class Hotel(db.Model):
#    tablename = 'Hotel'
 #   hotel_name = db.Column(db.String(20), primary_key=True)
  #  hotel_opened = db.Column(db.Date)
   # hotel_stars = db.Column(db.String(20))
    #hotel_type = db.Column(db.String(20))


# Presentation

Sales = presentation(presentation_name = 'Sales',
           user_email = 'alex@gmail.com',
           presentation_date = '2020-1-4')

DataBase = presentation(presentation_name = 'DataBase',
                  user_email = 'bob@gmail.com',
                  presentation_date = '2020-1-8'
                  )

Music = presentation(presentation_name = 'Music',
                 user_email = 'maria@gmail.com',
                 presentation_date = '2020-1-12'
                 )

Maths = presentation(presentation_name = 'Maths',
                    user_email = 'alex@gmail.com',
                    presentation_date = '2020-1-29'
                    )

Sports = presentation(presentation_name = 'Sports',
                 user_email = 'alex@gmail.com',
                 presentation_date = '2020-2-1'
                 )


# Participant

Science_Maths = Participant(participant_list = 'Science_Maths',
               participant_name = 'Alex, Bob'
               )

Art_Music = Participant(participant_list = 'Art_Music',
             participant_name = 'Maria'
             )

Computer_DataBase = Participant(participant_list = 'Computer_DataBase',
                   participant_name = 'Alex, Bob, Sam'
                   )

Business_Sales = Participant(participant_list = 'Business_Sales',
                participant_name = 'Maria'
                )

Math_Maths = Participant(participant_list = 'Math_Maths',
                participant_name = 'Bob, Sam')


# insert into Topic (topic_name, presentation_name) values ('Art', 'Music');
#
# insert into Topic (topic_name, presentation_name) values ('Science', 'Maths');
#
# insert into Topic (topic_name, presentation_name) values ('Math', 'Maths');
#
# insert into Topic (topic_name, presentation_name) values ('Computer', 'DataBase');
#
# insert into Topic (topic_name, presentation_name) values ('Business', 'Sales');

Art = topic(topic_name = 'Art',
               presentation_name = 'Music'
               )

Science = topic(topic_name = 'Science',
                  presentation_name = 'Maths'
                  )

Math = topic(topic_name = 'Math',
                presentation_name = 'Maths'
                )

Computer = topic(topic_name = 'Computer',
                         presentation_name = 'DataBase'
                         )

Business = topic(topic_name = 'Business',
                   presentation_name = 'Sales'
                   )


Alex.user_presentation.append(Sales)
Bob.user_presentation.append(DataBase)
Maria.user_presentation.append(Music)
Alex.user_presentation.append(Maths)
Alex.user_presentation.append(Sports)

Music.presentation_topic.append(Art)
Maths.presentation_topic.append(Science)
Maths.presentation_topic.append(Math)
Database.presentation_topic.append(Computer)
Sales.presentation_topic.append(Business)

Maths.participant_list_fk.append(Science_Maths)
Music.participant_list_fk.append(Art_Music)
DataBase.participant_list_fk.append(Computer_DataBase)
Sales.participant_list_fk.append(Business_Sales)
Maths.participant_list_fk.append(Math_Maths)


db.session.add_all([Maria, Bob, Kate, Alex, Sam,
                    Hilton, Intercontinental, Kyiv, Youth, Kolos,
                    Sales, DataBase, Music, Maths, Sports,
                    Science_Maths, Art_Music, Computer_DataBase, Business_Sales, Math_Maths,
                    Art, Science, Math, Computer, Business
])

db.session.commit()
