-- Tao bang
CREATE TABLE LOAI(
    idLoai CHAR(4) PRIMARY KEY,
    tenLoai VARCHAR(30) NOT NULL
);

CREATE TABLE KHUVUC(
    IP CHAR(11) PRIMARY KEY,
    tenKhuvuc VARCHAR(30) NOT NULL,
    tang SMALLINT
);

CREATE TABLE PHONG(
    MP CHAR(3) PRIMARY KEY,
    tenPhong VARCHAR(30) NOT NULL,
    somay SMALLINT,
    IP CHAR(11) REFERENCES KHUVUC(IP)
);

CREATE TABLE MAY(
    idMay CHAR(3) PRIMARY KEY,
    tenMay VARCHAR(30) NOT NULL,
    IP CHAR(11) REFERENCES KHUVUC(IP),
    ad SMALLINT CHECK(ad>=0 and ad<=255),
    idLoai CHAR(4) REFERENCES LOAI(idLoai),
    MP CHAR(3) REFERENCES PHONG(MP)
);

CREATE TABLE PHANMEM(
    idPM CHAR(4) PRIMARY KEY,
    tenPM VARCHAR(30) NOT NULL,
    ngaymua VARCHAR(10),
    phienban CHAR(3),
    idLoai CHAR(4) REFERENCES LOAI(idLoai),
    gia INT CHECK(gia>=0)
);

CREATE TABLE CAIDAT(
    idCD CHAR(2) PRIMARY KEY,
    idMay CHAR(3) REFERENCES MAY(idMay),
    idPM CHAR(4) REFERENCES PHANMEM(idPM),
    ngaycai DATE DEFAULT SYSDATE
);

-- Them du lieu
insert into loai values('TX','Terminal X-Window');
insert into loai values('UNIX','Système Unix');
insert into loai values('PCNT','PC Windows NT');
insert into loai values('PCWS','PC Windows');
insert into loai values('NC','Network Computer');

SELECT * FROM LOAI;

insert into khuvuc values('130.120.80','Brin RDC',null);
insert into khuvuc values('130.120.81','Brin tang 1',null);
insert into khuvuc values('130.120.82','Brin tang 2',null);

SELECT * FROM KHUVUC;

insert into phong values('s01','salle 1',3,'130.120.80');
insert into phong values('s02','salle 2',2,'130.120.80');
insert into phong values('s03','salle 3',2,'130.120.80');
insert into phong values('s11','salle 11',2,'130.120.81');
insert into phong values('s12','salle 12',1,'130.120.81');
insert into phong values('s21','salle 21',2,'130.120.82');
--insert into phong values('s22','salle 22',0,'130.120.83'); Bang KHUVUC chua co gia tri nay
--insert into phong values('s23','salle 23',0,'130.120.83'); Nhu tren

SELECT * FROM PHONG;

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

SELECT * FROM MAY;

insert into phanmem values('log1','Oracle 6','1995-05-13','6.2','UNIX',3000);
insert into phanmem values('log2','Oracle 8','1999-09-15','8i','UNIX',5600);
insert into phanmem values('log3','SQL Server','1998-04-12','7','PCNT',2700);
insert into phanmem values('log4','Front Page','1997-06-03','5','PCWS',500);
insert into phanmem values('log5','WinDev','1997-05-12','5','PCWS',750);
insert into phanmem values('log6','SQL*Net',null,'2.0','UNIX',500);
insert into phanmem values('log7','I.I.S.','2002-04-12','2','PCNT',810);
--insert into phanmem values('log8','Dreamweaver','2003-09-21','2.0','BeOS',1400); Bang LOAI chua co BeOS

SELECT * FROM PHANMEM;

insert into caidat(idMay,idPM,idCD,ngaycai) values('p2','log1','1','2003-05-15');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p2','log2','2','2003-09-17');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p4','log5','3',null);
insert into caidat(idMay,idPM,idCD,ngaycai) values('p6','log6','4','2003-05-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p6','log1','5','2003-05-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p6','log2','15','2003-05-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p8','log2','6','2003-05-19');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p8','log1','12','2003-05-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p8','log6','7','2003-05-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p11','log3','8','2003-04-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p12','log4','9','2003-04-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p11','log7','10','2003-04-20');
insert into caidat(idMay,idPM,idCD,ngaycai) values('p7','log7','11','2003-04-01');

SELECT * FROM CAIDAT;

-- Sua doi du lieu cot tang of KHUVUC
UPDATE KHUVUC SET tang=0 WHERE ip='130.120.80';
UPDATE KHUVUC SET tang=1 WHERE ip='130.120.81';
UPDATE KHUVUC SET tang=2 WHERE ip='130.120.82';
SELECT * FROM KHUVUC;

-- Giam 10% gia cua cac PHANMEM kieu 'PCNT'
UPDATE PHANMEM SET gia=(gia-gia*10/100) WHERE idloai='PCNT';
SELECT * FROM PHANMEM;

-- Them va cap nhat du lieu cot nbLog vao MAY va nbInstall vao PHANMEM
ALTER TABLE MAY ADD nbLog SMALLINT;
SELECT * FROM MAY;
ALTER TABLE PHANMEM ADD nbInstall SMALLINT;
SELECT * FROM PHANMEM;

UPDATE MAY SET nbLog=0 WHERE idmay='p1';
UPDATE MAY SET nbLog=2 WHERE idmay='p2';
UPDATE MAY SET nbLog=0 WHERE idmay='p3';
UPDATE MAY SET nbLog=1 WHERE idmay='p4';
UPDATE MAY SET nbLog=0 WHERE idmay='p5';
UPDATE MAY SET nbLog=2 WHERE idmay='p6';
UPDATE MAY SET nbLog=1 WHERE idmay='p7';
UPDATE MAY SET nbLog=2 WHERE idmay='p8';
UPDATE MAY SET nbLog=0 WHERE idmay='p9';
UPDATE MAY SET nbLog=0 WHERE idmay='p10';
UPDATE MAY SET nbLog=2 WHERE idmay='p11';
UPDATE MAY SET nbLog=1 WHERE idmay='p12';
SELECT * FROM MAY;

UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log1';
UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log2';
UPDATE PHANMEM SET nbInstall=1 WHERE idPM='log3';
UPDATE PHANMEM SET nbInstall=1 WHERE idPM='log4';
UPDATE PHANMEM SET nbInstall=1 WHERE idPM='log5';
UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log6';
UPDATE PHANMEM SET nbInstall=2 WHERE idPM='log7';
SELECT * FROM PHANMEM;

-- Tao bang PHANMEMUNIX
CREATE TABLE PHANMEMUNIX(
    idPM CHAR(4),
    tenPM VARCHAR(30) NOT NULL,
    ngaymua VARCHAR(10),
    phienban CHAR(3)
);

-- Them khoa chinh cho PHANMEMUNIX
ALTER TABLE PHANMEMUNIX ADD PRIMARY KEY (idPM);

-- Them cot gia cho PHANMEMUNIX
ALTER TABLE PHANMEMUNIX ADD gia INT CHECK(gia>=0);

-- Thay doi datatype cot phienban
ALTER TABLE PHANMEMUNIX MODIFY phienban VARCHAR(15);

-- Them rang buoc duy nhat cho cot tenPM
ALTER TABLE PHANMEMUNIX ADD UNIQUE (tenPM);

-- Them du lieu cho bang PHANMEMUNIX tu bang PHANMEM
insert into PHANMEMUNIX values('log1','Oracle 6','1995-05-13','6.2', 3000);
insert into PHANMEMUNIX values('log2','Oracle 8','1999-09-15','8i', 5600);
insert into PHANMEMUNIX values('log3','SQL Server','1998-04-12','7', 2700);
insert into PHANMEMUNIX values('log4','Front Page','1997-06-03','5', 500);
insert into PHANMEMUNIX values('log5','WinDev','1997-05-12','5', 750);
insert into PHANMEMUNIX values('log6','SQL*Net',null,'2.0', 500);
insert into PHANMEMUNIX values('log7','I.I.S.','2002-04-12','2', 810);

-- Xoa cot phienban trong PHANMEMUNIX
ALTER TABLE PHANMEMUNIX DROP COLUMN phienban;

-- Xoa dulieu o bang PHANMEM co gia > 5000
DELETE FROM PHANMEM WHERE gia>5000; -- Khong the xoa du lieu tu bang cha(PHANMEM -> CAIDAT: idPM)

-- Xoa dulieu o bang PHANMEMUNIX co gia > 5000
DELETE FROM PHANMEMUNIX WHERE gia>5000; -- Khong xoa duoc

-- Xoa bang PHANMEM
DROP TABLE PHANMEM; -- Cac bang khac co chua du lieu cua PHANMEM

-- Xoa dulieu o bang PHANMEMUNIX co gia > 5000
DROP TABLE PHANMEMUNIX; -- Xoa duoc do bang nay khong chua khoa ngoai (khong co con)

-- Xoa cot nbLog va nbInstall
ALTER TABLE MAY DROP COLUMN nbLog;
SELECT * FROM MAY;

ALTER TABLE PHANMEM DROP COLUMN nbInstall;
SELECT * FROM PHANMEM;