create table if not exists edbuser.users (
	username varchar(10) not null,
	admin bool not null
);

alter table edbuser.users add constraint pk_users primary key (username);

insert into edbuser.users (username, admin) values ('edenflo', true);
insert into edbuser.users (username, admin) values ('mimi', false);
insert into edbuser.users (username, admin) values ('chaid', false);
