create table category_stage
(catid smallint default 0,
catgroup varchar(10) default 'General',
catname varchar(10) default 'General',
catdesc varchar(50) default 'General');


insert into category_stage values
(12, 'Concerts', 'Comedy', 'All stand-up comedy performances'),
(13, 'Concerts', 'Other', default),
(14, 'Concerts', 'Sertanejo', default),
(15, 'Concerts', 'Rock', default),
(16, 'Theater', 'Drama', default)
;