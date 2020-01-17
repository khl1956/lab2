/*==============================================================*/
/* DBMS name:      PostgreSQL 12.1                               */
/* Created on:     17.01.2020 19:13:45                          */
/*==============================================================*/

-- drop index Group_PK;
--
-- drop table "Group";
--
-- drop index "Groups have Subjects2_FK";
--
-- drop index "Groups have Subjects_FK";
--
-- drop index "Groups have Subjects_PK";
--
-- drop table "Groups have Subjects";
--
-- drop index "Statement has Ratings_FK";
--
-- drop index "User has Marks_FK";
--
-- drop index Rating_PK;
--
-- drop table Rating;
--
-- drop index "Subject has Statements_FK";
--
-- drop index Statement_PK;
--
-- drop table Statement;
--
-- drop index Subject_PK;
--
-- drop table Subject;
--
-- drop index "Subject has Tasks_FK";
--
-- drop index Task_PK;
--
-- drop table Task;
--
-- drop index "Group has Students_FK";
--
-- drop index User_PK;
--
-- drop table "User";

/*==============================================================*/
/* Table: "Group"                                               */
/*==============================================================*/
create table "Group" (
   group_name           VARCHAR(10)          not null,
   group_year           INT4                 not null,
   constraint PK_GROUP primary key (group_name, group_year)
);

/*==============================================================*/
/* Index: Group_PK                                              */
/*==============================================================*/
create unique index Group_PK on "Group" (
group_name,
group_year
);

/*==============================================================*/
/* Table: "Groups have Subjects"                                */
/*==============================================================*/
create table "Groups have Subjects" (
   group_name           VARCHAR(10)          not null,
   group_year           INT4                 not null,
   subject_name         VARCHAR(200)         not null,
   constraint "PK_GROUPS HAVE SUBJECTS" primary key (group_name, group_year, subject_name)
);

/*==============================================================*/
/* Index: "Groups have Subjects_PK"                             */
/*==============================================================*/
create unique index "Groups have Subjects_PK" on "Groups have Subjects" (
group_name,
group_year,
subject_name
);

/*==============================================================*/
/* Index: "Groups have Subjects_FK"                             */
/*==============================================================*/
create  index "Groups have Subjects_FK" on "Groups have Subjects" (
group_name,
group_year
);

/*==============================================================*/
/* Index: "Groups have Subjects2_FK"                            */
/*==============================================================*/
create  index "Groups have Subjects2_FK" on "Groups have Subjects" (
subject_name
);

/*==============================================================*/
/* Table: Rating                                                */
/*==============================================================*/
create table Rating (
   email                VARCHAR(32)          not null,
   subject_name         VARCHAR(200)         not null,
   statement_number     INT4                 not null,
   mark                 INT4                 not null,
   constraint PK_RATING primary key (email, subject_name, statement_number, mark)
);

/*==============================================================*/
/* Index: Rating_PK                                             */
/*==============================================================*/
create unique index Rating_PK on Rating (
email,
subject_name,
statement_number,
mark
);

/*==============================================================*/
/* Index: "User has Marks_FK"                                   */
/*==============================================================*/
create  index "User has Marks_FK" on Rating (
email
);

/*==============================================================*/
/* Index: "Statement has Ratings_FK"                            */
/*==============================================================*/
create  index "Statement has Ratings_FK" on Rating (
subject_name,
statement_number
);

/*==============================================================*/
/* Table: Statement                                             */
/*==============================================================*/
create table Statement (
   subject_name         VARCHAR(200)         not null,
   statement_number     INT4                 not null,
   statement_date       DATE                 null,
   constraint PK_STATEMENT primary key (subject_name, statement_number)
);

/*==============================================================*/
/* Index: Statement_PK                                          */
/*==============================================================*/
create unique index Statement_PK on Statement (
subject_name,
statement_number
);

/*==============================================================*/
/* Index: "Subject has Statements_FK"                           */
/*==============================================================*/
create  index "Subject has Statements_FK" on Statement (
subject_name
);

/*==============================================================*/
/* Table: Subject                                               */
/*==============================================================*/
create table Subject (
   subject_name         VARCHAR(200)         not null,
   constraint PK_SUBJECT primary key (subject_name)
);

/*==============================================================*/
/* Index: Subject_PK                                            */
/*==============================================================*/
create unique index Subject_PK on Subject (
subject_name
);

/*==============================================================*/
/* Table: Task                                                  */
/*==============================================================*/
create table Task (
   subject_name         VARCHAR(200)         not null,
   task_name            VARCHAR(200)         not null,
   task_description     TEXT                 null,
   task_deadline        DATE                 null,
   constraint PK_TASK primary key (subject_name, task_name)
);

/*==============================================================*/
/* Index: Task_PK                                               */
/*==============================================================*/
create unique index Task_PK on Task (
subject_name,
task_name
);

/*==============================================================*/
/* Index: "Subject has Tasks_FK"                                */
/*==============================================================*/
create  index "Subject has Tasks_FK" on Task (
subject_name
);

/*==============================================================*/
/* Table: "User"                                                */
/*==============================================================*/
create table "User" (
   email                VARCHAR(32)          not null,
   group_name           VARCHAR(10)          null,
   group_year           INT4                 null,
   password             VARCHAR(100)         not null,
   full_name            VARCHAR(200)         not null,
   role                 VARCHAR(64)          not null,
   constraint PK_USER primary key (email)
);

/*==============================================================*/
/* Index: User_PK                                               */
/*==============================================================*/
create unique index User_PK on "User" (
email
);

/*==============================================================*/
/* Index: "Group has Students_FK"                               */
/*==============================================================*/
create  index "Group has Students_FK" on "User" (
group_name,
group_year
);

alter table "Groups have Subjects"
   add constraint "FK_GROUPS H_GROUPS HA_GROUP" foreign key (group_name, group_year)
      references "Group" (group_name, group_year)
      on delete restrict on update restrict;

alter table "Groups have Subjects"
   add constraint "FK_GROUPS H_GROUPS HA_SUBJECT" foreign key (subject_name)
      references Subject (subject_name)
      on delete restrict on update restrict;

alter table Rating
   add constraint FK_RATING_STATEMENT_STATEMEN foreign key (subject_name, statement_number)
      references Statement (subject_name, statement_number)
      on delete restrict on update restrict;

alter table Rating
   add constraint "FK_RATING_USER HAS _USER" foreign key (email)
      references "User" (email)
      on delete restrict on update restrict;

alter table Statement
   add constraint "FK_STATEMEN_SUBJECT H_SUBJECT" foreign key (subject_name)
      references Subject (subject_name)
      on delete restrict on update restrict;

alter table Task
   add constraint "FK_TASK_SUBJECT H_SUBJECT" foreign key (subject_name)
      references Subject (subject_name)
      on delete restrict on update restrict;

alter table "User"
   add constraint "FK_USER_GROUP HAS_GROUP" foreign key (group_name, group_year)
      references "Group" (group_name, group_year)
      on delete restrict on update restrict;

