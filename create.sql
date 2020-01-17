	/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     23.10.2019 21:44:16                          */
/*==============================================================*/

/*
drop index "One presentation Has Many topics_FK";

drop index topic_PK;

drop table Topic;

drop index "User Have Many presentations_FK";

drop index presentation_PK;

drop table presentation;

drop index "Presentation Have Participants2_FK";

drop index "Presentation Have Participants_FK";

drop index "Presentation Have Participants_PK";

drop table Presentation_have_Participants;

drop index user_PK;

drop table user;

drop index Participant_PK;

drop table Participant;
*/

/*==============================================================*/
/* Table: topic                                               */
/*==============================================================*/
create table topic (
   topic_name         VARCHAR(20)          not null,
   presentation_name           VARCHAR(20)          null,
   constraint PK_topic primary key (topic_name)
);

/*==============================================================*/
/* Index: topic_PK                                            */
/*==============================================================*/
create unique index topic_PK on topic (
topic_name
);

/*==============================================================*/
/* Index: "One presentation Has Many topics_FK"                      */
/*==============================================================*/
create  index "One presentation Has Many topics_FK" on topic (
presentation_name
);

/*==============================================================*/
/* Table: presentation                                                 */
/*==============================================================*/
create table presentation (
   presentation_name           VARCHAR(20)          not null,
   user_email         VARCHAR(20)          null,
   presentation_date           DATE                 null,
   constraint PK_presentation primary key (presentation_name)
);

/*==============================================================*/
/* Index: presentation_PK                                              */
/*==============================================================*/
create unique index presentation_PK on presentation (
presentation_name
);

/*==============================================================*/
/* Index: "user Have Many presentations_FK"                          */
/*==============================================================*/
create  index "user Have Many presentations_FK" on presentation (
user_email
);

/*==============================================================*/
/* Table: presentation_have_Participants                                     */
/*==============================================================*/
create table presentation_have_Participants (
   presentation_name           VARCHAR(20)          not null,
   participant_list           VARCHAR(30)          not null,
   constraint PK_presentation_HAVE_ParticipantS primary key (presentation_name, participant_list)
);

/*==============================================================*/
/* Index: "presentation Have Participants_PK"                                */
/*==============================================================*/
create unique index "presentation Have Participants_PK" on presentation_have_Participants (
presentation_name,
participant_list
);

/*==============================================================*/
/* Index: "presentation Have Participants_FK"                                */
/*==============================================================*/
create  index "presentation Have Participants_FK" on presentation_have_Participants (
presentation_name
);

/*==============================================================*/
/* Index: "presentation Have Participants2_FK"                               */
/*==============================================================*/
create  index "presentation Have Participants2_FK" on presentation_have_Participants (
participant_list
);

/*==============================================================*/
/* Table: user                                                */
/*==============================================================*/
create table user (
   user_email         VARCHAR(20)          not null,
   user_name          VARCHAR(20)          null,
   user_phone         VARCHAR(20)          null,
   user_birthday      DATE                 null,
   constraint PK_user primary key (user_email)
);

/*==============================================================*/
/* Index: user_PK                                             */
/*==============================================================*/
create unique index user_PK on user (
user_email
);

/*==============================================================*/
/* Table: Participant                                                 */
/*==============================================================*/
create table Participant (
   participant_list           VARCHAR(20)          not null,
   participant_name         VARCHAR(50)          null,
   constraint PK_Participant primary key (participant_list)
);

/*==============================================================*/
/* Index: Participant_PK                                              */
/*==============================================================*/
create unique index Participant_PK on Participant (
participant_list
);

alter table topic
   add constraint "FK_topic_ONE presentation_presentation" foreign key (presentation_name)
      references presentation (presentation_name)
      on delete restrict on update restrict;

alter table presentation
   add constraint "FK_presentation_ONE OF TH_user" foreign key (user_email)
      references user (user_email)
      on delete restrict on update restrict;

alter table presentation_have_Participants
   add constraint "FK_presentation_HA_ONE presentation_presentation" foreign key (presentation_name)
      references presentation (presentation_name)
      on delete restrict on update restrict;

alter table presentation_have_Participants
   add constraint "FK_presentation_HA_ONE presentation_Participant" foreign key (participant_list)
      references Participant (participant_list)
      on delete restrict on update restrict;
