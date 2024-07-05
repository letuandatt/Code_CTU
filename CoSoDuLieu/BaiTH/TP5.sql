CREATE TABLE LOAI(
    IDLOAI CHAR(4) PRIMARY KEY,
    TENLOAI VARCHAR(3) NOT NULL
);

CREATE TABLE KHUVUC(
    IP CHAR(10) PRIMARY KEY,
    TENKHUVUC CHAR(11) NOT NULL,
    TANG SMALLINT
);

CREATE TABLE PHONG(
    MP CHAR(3) PRIMARY KEY,
    TENPHONG CHAR(8) NOT NULL,
    SPMAY SMALLINT,
    IP CHAR(10) REFERENCES KHUVUC(IP)
);

CREATE TABLE MAY(
    IDMAY CHAR(3) PRIMARY KEY,
    TENMAY CHAR(8) NOT NULL,
    IP CHAR(10) REFERENCES KHUVUC(IP),
    AD SMALLINT CHECK(AD>=0 AND AD<=255),
    IDLOAI CHAR(4) REFERENCES LOAI(IDLOAI),
    MP CHAR(3) REFERENCES PHONG(MP)
);

CREATE TABLE PHANMEM(
    IDPM CHAR(4) PRIMARY KEY,
    TENPM VARCHAR(15) NOT NULL,
    NGAYMUA DATE,
    PHIENBAN CHAR(3),
    IDLOAI CHAR(4) REFERENCES LOAI(IDLOAI),
    GIA INT CHECK(GIA >= 0)
);

CREATE TABLE CAIDAT(
    IDCD VARCHAR(20) PRIMARY KEY,
    IDMAY CHAR(3) REFERENCES MAY(IDMAY),
    IDPM CHAR(4) REFERENCES PHANMEM(IDPM),
    NGAYCAI DATE DEFAULT SYSDATE
);

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
insert into loai values('UNIX','System Unix');
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

insert into phanmem values('log1','Oracle 6','05-13-1995','6.2','UNIX',3000);
insert into phanmem values('log2','Oracle 8','09-15-1999','8i','UNIX',5600);
insert into phanmem values('log3','SQL Server','04-12-1998','7','PCNT',2700);
insert into phanmem values('log4','Front Page','06-03-1997','5','PCWS',500);
insert into phanmem values('log5','WinDev','05-12-1997','5','PCWS',750);
insert into phanmem values('log6','SQL*Net',null,'2.0','UNIX',500);
insert into phanmem values('log7','I.I.S.','04-12-2002','2','PCNT',810);

insert into caidat(idMay,idPM,idcd,ngaycai) values('p1','log1','13','08-10-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p1','log2','14','08-11-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p2','log1','1','05-15-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p2','log2','2','09-17-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p4','log5','3',null);
insert into caidat(idMay,idPM,idcd,ngaycai) values('p6','log6','4','05-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p6','log1','5','05-2-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p8','log2','6','05-19-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p8','log6','7','05-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p8','log1','12','06-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p11','log3','8','04-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p12','log4','9','04-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p11','log7','10','04-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p7','log7','11','04-01-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p12','log6','15','07-25-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p12','log1','16','03-20-2003');
insert into caidat(idMay,idPM,idcd,ngaycai) values('p3','log1','17','03-20-2003');

-- Câu 2
SELECT l.TENLOAI
FROM LOAI l JOIN MAY m ON l.IDLOAI = m.IDLOAI
WHERE m.IDMAY='p8';

-- Câu 3
SELECT TENPM
FROM PHANMEM
WHERE IDLOAI='UNIX';

-- Câu 4
SELECT DISTINCT p.MP, p.TENPHONG, p.IP
FROM KHUVUC k JOIN PHONG p ON k.IP = p.IP
              JOIN MAY m ON p.MP = m.MP
WHERE m.IDLOAI = 'UNIX' OR m.IDLOAI = 'PCWS';

-- Câu 5
SELECT DISTINCT p.MP, p.TENPHONG, p.IP
FROM KHUVUC k JOIN PHONG p ON k.IP = p.IP
              JOIN MAY m ON p.MP = m.MP
WHERE (m.IDLOAI = 'UNIX' OR m.IDLOAI = 'PCWS') AND k.IP = '130.120.80'
ORDER BY p.MP;

-- Câu 6
SELECT COUNT(*) SOPHANMEM
FROM CAIDAT
WHERE IDMAY = 'p6';

-- Câu 7
SELECT COUNT(*) SOMAY
FROM CAIDAT
WHERE IDPM = 'log1';

-- Câu 8
SELECT TENMAY, IP || '.' || AD AS FULL_IP
FROM MAY
WHERE IDLOAI = 'TX'
ORDER BY TENMAY;

-- Câu 9
SELECT IDPM, COUNT(*) SOPHANMEM
FROM CAIDAT
GROUP BY IDPM
ORDER BY IDPM;

-- Câu 10
SELECT MP, COUNT(*) SOMAY
FROM MAY
GROUP BY MP;

-- Câu 11
SELECT IDMAY, IDPM, COUNT(*) SOPHANMEM
FROM CAIDAT
GROUP BY IDMAY, IDPM
ORDER BY IDMAY, IDPM;

-- Câu 12
SELECT AVG(GIA) GIATRUNGBINHUNIX
FROM PHANMEM
WHERE IDLOAI = 'UNIX';

-- Câu 13
SELECT MAX(NGAYMUA) NGAYMUAGANNHAT
FROM PHANMEM;

-- Câu 14
SELECT COUNT(*) SOMAY
FROM (
    SELECT IDMAY, COUNT(*) SOMAY
    FROM CAIDAT
    GROUP BY IDMAY
    HAVING COUNT(*) >= 2
);

-- Câu 15
SELECT IDLOAI
FROM LOAI
MINUS
SELECT IDLOAI
FROM MAY;

SELECT l.IDLOAI
FROM LOAI l LEFT JOIN MAY m ON l.IDLOAI = m.IDLOAI
WHERE m.IDLOAI IS NULL;

-- Câu 16
SELECT IDLOAI
FROM MAY
INTERSECT
SELECT IDLOAI
FROM PHANMEM;

-- Câu 17
SELECT IDLOAI
FROM LOAI
MINUS
SELECT IDLOAI
FROM PHANMEM;

SELECT l.IDLOAI
FROM LOAI l LEFT JOIN PHANMEM p ON l.IDLOAI = p.IDLOAI
WHERE p.IDLOAI IS NULL;

-- Câu 18
SELECT DISTINCT m.IP || '.' || m.AD AS FULLIP
FROM MAY m JOIN CAIDAT c ON m.IDMAY = c.IDMAY
WHERE c.IDPM = 'log6';

-- Câu 19
SELECT DISTINCT m.IP || '.' || m.AD AS FULLIP
FROM MAY m JOIN CAIDAT c ON m.IDMAY = c.IDMAY
            JOIN PHANMEM p ON c.IDPM = p.IDPM
WHERE p.TENPM = 'Oracle 8'; 

-- Câu 20
SELECT k.TENKHUVUC
FROM KHUVUC k JOIN MAY m ON k.IP = m.IP
WHERE m.IDLOAI = 'TX'
GROUP BY k.TENKHUVUC
HAVING COUNT(*) = 3;

-- Câu 21
SELECT DISTINCT p.TENPHONG
FROM PHONG p JOIN MAY m ON p.MP = m.MP
                JOIN CAIDAT c ON m.IDMAY = c.IDMAY
                JOIN PHANMEM pm ON c.IDPM = pm.IDPM
WHERE pm.TENPM = 'Oracle 6'
ORDER BY p.TENPHONG;

-- Câu 22
SELECT TENPM
FROM PHANMEM
WHERE NGAYMUA = (SELECT MAX(NGAYMUA) FROM PHANMEM);

-- Câu 23
SELECT TENPM, GIA
FROM PHANMEM
WHERE IDLOAI = 'PCNT'
GROUP BY TENPM, GIA
HAVING GIA > ANY (
    SELECT GIA
    FROM PHANMEM
    WHERE IDLOAI = 'UNIX'
);

-- Câu 24
SELECT TENPM, GIA
FROM PHANMEM
WHERE IDLOAI = 'UNIX'
GROUP BY TENPM, GIA
HAVING GIA > ALL (
    SELECT GIA
    FROM PHANMEM
    WHERE IDLOAI = 'PCNT'
);

-- Câu 25


-- Câu 26


-- Câu 27


-- 
SELECT * FROM KHUVUC;
SELECT * FROM PHONG;
SELECT * FROM LOAI;
SELECT * FROM MAY;
SELECT * FROM PHANMEM;
SELECT * FROM CAIDAT;
