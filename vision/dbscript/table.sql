drop table VISION CASCADE CONSTRAINTS;

create table vision (
    name varchar2(100) NOT NULL,
    tel varchar2(25) NOT NULL
);

comment on column vision.name is '��ȣ��';
comment on column vision.tel is '��ȭ��ȣ';

commit;