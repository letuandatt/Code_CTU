

create table NGUOI_AN(ten VARCHAR(30) NOT NULL , tuoi int, phai VARCHAR(6));
create table LUI_TOI(ten VARCHAR(30)NOT NULL, quanPizza VARCHAR(30) NOT NULL);
create table AN(ten VARCHAR(30)NOT NULL, pizza VARCHAR(30) NOT NULL);
create table PHUC_VU(quanPizza VARCHAR(30)NOT NULL, pizza VARCHAR(30)NOT NULL, gia numeric (6,3));


insert into NGUOI_AN values('Amy', 16, 'female');
insert into NGUOI_AN values('Ben', 21, 'male');
insert into NGUOI_AN values('Cal', 33, 'male');
insert into NGUOI_AN values('Dan', 13, 'male');
insert into NGUOI_AN values('Eli', 45, 'male');
insert into NGUOI_AN values('Fay', 21, 'female');
insert into NGUOI_AN values('Gus', 24, 'male');
insert into NGUOI_AN values('Hil', 30, 'female');
insert into NGUOI_AN values('Ian', 18, 'male');

insert into LUI_TOI values('Amy', 'Pizza Hut');
insert into LUI_TOI values('Ben', 'Pizza Hut');
insert into LUI_TOI values('Ben', 'Chicago Pizza');
insert into LUI_TOI values('Cal', 'Straw Hat');
insert into LUI_TOI values('Cal', 'New York Pizza');
insert into LUI_TOI values('Dan', 'Straw Hat');
insert into LUI_TOI values('Dan', 'New York Pizza');
insert into LUI_TOI values('Eli', 'Straw Hat');
insert into LUI_TOI values('Eli', 'Chicago Pizza');
insert into LUI_TOI values('Fay', 'Dominos');
insert into LUI_TOI values('Fay', 'Little Caesars');
insert into LUI_TOI values('Gus', 'Chicago Pizza');
insert into LUI_TOI values('Gus', 'Pizza Hut');
insert into LUI_TOI values('Hil', 'Dominos');
insert into LUI_TOI values('Hil', 'Straw Hat');
insert into LUI_TOI values('Hil', 'Pizza Hut');
insert into LUI_TOI values('Ian', 'New York Pizza');
insert into LUI_TOI values('Ian', 'Straw Hat');
insert into LUI_TOI values('Ian', 'Dominos');

insert into AN values('Amy', 'pepperoni');
insert into AN values('Amy', 'mushroom');
insert into AN values('Ben', 'pepperoni');
insert into AN values('Ben', 'cheese');
insert into AN values('Cal', 'supreme');
insert into AN values('Dan', 'pepperoni');
insert into AN values('Dan', 'cheese');
insert into AN values('Dan', 'sausage');
insert into AN values('Dan', 'supreme');
insert into AN values('Dan', 'mushroom');
insert into AN values('Eli', 'supreme');
insert into AN values('Eli', 'cheese');
insert into AN values('Fay', 'mushroom');
insert into AN values('Gus', 'mushroom');
insert into AN values('Gus', 'supreme');
insert into AN values('Gus', 'cheese');
insert into AN values('Hil', 'supreme');
insert into AN values('Hil', 'cheese');
insert into AN values('Ian', 'supreme');
insert into AN values('Ian', 'pepperoni');

insert into PHUC_VU values('Pizza Hut', 'pepperoni', 12);
insert into PHUC_VU values('Pizza Hut', 'sausage', 12);
insert into PHUC_VU values('Pizza Hut', 'cheese', 9);
insert into PHUC_VU values('Pizza Hut', 'supreme', 12);
insert into PHUC_VU values('Little Caesars', 'pepperoni', 9.75);
insert into PHUC_VU values('Little Caesars', 'sausage', 9.5);
insert into PHUC_VU values('Little Caesars', 'cheese', 7);
insert into PHUC_VU values('Little Caesars', 'mushroom', 9.25);
insert into PHUC_VU values('Little Caesars', 'supreme', 9);
insert into PHUC_VU values('Dominos', 'cheese', 9.75);
insert into PHUC_VU values('Dominos', 'mushroom', 11);
insert into PHUC_VU values('Straw Hat', 'pepperoni', 8);
insert into PHUC_VU values('Straw Hat', 'cheese', 9.25);
insert into PHUC_VU values('Straw Hat', 'sausage', 9.75);
insert into PHUC_VU values('New York Pizza', 'pepperoni', 8);
insert into PHUC_VU values('New York Pizza', 'cheese', 7);
insert into PHUC_VU values('New York Pizza', 'supreme', 8.5);
insert into PHUC_VU values('Chicago Pizza', 'cheese', 7.75);
insert into PHUC_VU values('Chicago Pizza', 'supreme', 8.5);

