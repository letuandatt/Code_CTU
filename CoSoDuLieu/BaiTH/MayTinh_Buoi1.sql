-- Câu 1
CREATE TABLE LOAI(
    idLoai CHAR(4) PRIMARY KEY,
    tenLoai VARCHAR(30) NOT NULL
);

CREATE TABLE KHUVUC(
    IP CHAR(10) PRIMARY KEY,
    tenKhuVuc CHAR(11) NOT NULL,
    tang SMALLINT
);

CREATE TABLE PHONG(
    MP CHAR(3) PRIMARY KEY,
    tenPhong CHAR(8) NOT NULL,
    somay SMALLINT,
    IP CHAR(10) REFERENCES KHUVUC(IP)
);

CREATE TABLE MAY(
    idMay CHAR(3) PRIMARY KEY,
    tenMay CHAR(8) NOT NULL,
    IP CHAR(10) REFERENCES KHUVUC(IP),
    ad SMALLINT CHECK(ad>=0 and ad<=255),
    idLoai CHAR(4) REFERENCES LOAI(idLoai),
    MP CHAR(3) REFERENCES PHONG(MP)
);

CREATE TABLE PHANMEM(
    idPM CHAR(4) PRIMARY KEY,
    tenPM VARCHAR(15) NOT NULL,
    ngaymua DATE,
    phienban CHAR(3),
    idLoai CHAR(4) REFERENCES LOAI(idLoai),
    gia INT CHECK(gia>=0)
);

CREATE TABLE CAIDAT(
    idCD INT PRIMARY KEY,
    idMay CHAR(3) REFERENCES MAY(idMay),
    idPM CHAR(4) REFERENCES PHANMEM(idPM),
    ngaycai DATE DEFAULT SYSDATE
);

-- Câu 2
insert into khuvuc values('130.120.80','Brin RDC',null);
insert into khuvuc values('130.120.81','Brin tang 1',null);
insert into khuvuc values('130.120.82','Brin tang 2',null);

insert into phong values('s01','salle 1',3,'130.120.80');
insert into phong values('s02','salle 2',2,'130.120.80');
insert into phong values('s03','salle 3',2,'130.120.80');
insert into phong values('s11','salle 11',2,'130.120.81');
insert into phong values('s12','salle 12',1,'130.120.81');
insert into phong values('s21','salle 21',2,'130.120.82');

insert into loai values('TX','Terminal X-Window');
insert into loai values('UNIX','Système Unix');
insert into loai values('PCNT','PC Windows NT');
insert into loai values('PCWS','PC Windows');
insert into loai values('NC','Network Computer');

insert into may values('p1','Poste 1','130.120.80',01,'TX','s01');
insert into may values('p2','Poste 2','130.120.80',02,'UNIX','s01');
insert into may values('p3','Poste 3','130.120.80',03,'TX','s01');
insert into may values('p4','Poste 4','130.120.80',04,'PCWS','s02');
insert into may values('p5','Poste 5','130.120.80',05,'PCWS','s02');
insert into may values('p6','Poste 6','130.120.80',06,'UNIX','s03');
insert into may values('p7','Poste 7','130.120.80',07,'TX','s03');
insert into may values('p8','Poste 8','130.120.81',01,'UNIX','s11');
insert into may values('p9','Poste 9','130.120.81',02,'TX','s11');
insert into may values('p10','Poste 10','130.120.81',03,'UNIX','s12');
insert into may values('p11','Poste 11','130.120.82',01,'PCNT','s21');
insert into may values('p12','Poste 12','130.120.82',02,'PCWS','s21');

insert into phanmem values('log1','Oracle 6','05/13/1995','6.2','UNIX',3000);
insert into phanmem values('log2','Oracle 8','09/15/1999','8i','UNIX',5600);
insert into phanmem values('log3','SQL Server','04/12/1998','7','PCNT',2700);
insert into phanmem values('log4','Front Page','06/03/1997','5','PCWS',500);
insert into phanmem values('log5','WinDev','05/12/1997','5','PCWS',750);
insert into phanmem values('log6','SQL*Net',null,'2.0','UNIX',500);
insert into phanmem values('log7','I.I.S.','04/12/2002','2','PCNT',810);

insert into caidat(idMay,idPM,idCD,ngaycai) values('p2','log1','1','05/15/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p2','log2','2','09/17/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p4','log5','3',null);
insert into caidat(idMay,idPM,idCD,ngaycai) values('p6','log6','4','05/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p6','log1','5','05/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p6','log2','15','05/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p8','log2','6','05/19/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p8','log1','12','05/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p8','log6','7','05/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p11','log3','8','04/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p12','log4','9','04/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p11','log7','10','04/20/2003');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p7','log7','11','04/01/2003');

-- Câu 3
UPDATE KHUVUC
SET tang=0
WHERE IP='130.120.80';

UPDATE KHUVUC
SET tang=1
WHERE IP='130.120.81';

UPDATE KHUVUC
SET tang=2
WHERE IP='130.120.82';

-- Câu 4
UPDATE PHANMEM
SET gia=(gia*0.9)
WHERE idLoai='PCNT';

-- Câu 5
ALTER TABLE MAY
ADD nbLog SMALLINT;

ALTER TABLE PHANMEM
ADD nbInstall SMALLINT;

UPDATE MAY SET nbLog=0 WHERE idMay='p1';
UPDATE MAY SET nbLog=2 WHERE idMay='p2';
UPDATE MAY SET nbLog=0 WHERE idMay='p3';
UPDATE MAY SET nbLog=1 WHERE idMay='p4';
UPDATE MAY SET nbLog=0 WHERE idMay='p5';
UPDATE MAY SET nbLog=2 WHERE idMay='p6';
UPDATE MAY SET nbLog=1 WHERE idMay='p7';
UPDATE MAY SET nbLog=2 WHERE idMay='p8';
UPDATE MAY SET nbLog=0 WHERE idMay='p9';
UPDATE MAY SET nbLog=0 WHERE idMay='p10';
UPDATE MAY SET nbLog=2 WHERE idMay='p11';
UPDATE MAY SET nbLog=1 WHERE idMay='p12';

UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log1';
UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log2';
UPDATE PHANMEM SET nbInstall=1 WHERE idPM='log3';
UPDATE PHANMEM SET nbInstall=1 WHERE idPM='log4';
UPDATE PHANMEM SET nbInstall=1 WHERE idPM='log5';
UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log6';
UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log7';

-- Câu 6
CREATE TABLE PHANMEMUNIX(
    idPM CHAR(4),
    tenPM VARCHAR(15) NOT NULL,
    ngaymua DATE,
    phienban CHAR(3)
);

-- Câu 7
ALTER TABLE PHANMEMUNIX ADD PRIMARY KEY (idPM);

-- Câu 8
ALTER TABLE PHANMEMUNIX ADD gia SMALLINT CHECK(gia>=0);

-- Câu 9
ALTER TABLE PHANMEMUNIX MODIFY phienban VARCHAR(15);

-- Câu 10
ALTER TABLE PHANMEMUNIX ADD UNIQUE (tenPM);

-- Câu 11
INSERT INTO PHANMEMUNIX
    SELECT idPM, tenPM, ngaymua, phienban, gia
    FROM PHANMEM;

-- Câu 12
ALTER TABLE PHANMEMUNIX DROP COLUMN phienban;

-- Câu 13
DELETE FROM PHANMEM WHERE gia>5000; -- K xóa ???c

-- Câu 14
DELETE FROM PHANMEMUNIX WHERE gia>5000; -- Xóa ???c

-- Câu 15
DROP TABLE PHANMEM; -- K xóa ???c

-- Câu 16
DROP TABLE PHANMEMUNIX;

-- Câu 17
ALTER TABLE PHANMEM DROP COLUMN nbInstall;
ALTER TABLE MAY DROP COLUMN nbLog;
