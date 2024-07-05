CREATE TABLE NGUOI_AN(
    TEN VARCHAR(30) NOT NULL,
    TUOI INT,
    PHAI VARCHAR(6)
);

CREATE TABLE LUI_TOI(
    TEN VARCHAR(30) NOT NULL,
    QUANPIZZA VARCHAR(30) NOT NULL
);

CREATE TABLE AN(
    TEN VARCHAR(30) NOT NULL,
    PIZZA VARCHAR(30) NOT NULL
);

CREATE TABLE PHUC_VU(
    QUANPIZZA VARCHAR(30) NOT NULL,
    PIZZA VARCHAR(30) NOT NULL,
    GIA NUMERIC(6, 3)
);

-- Câu 1
ALTER TABLE NGUOI_AN ADD PRIMARY KEY (TEN);

ALTER TABLE LUI_TOI
ADD CONSTRAINT fk_nguoi_an
FOREIGN KEY (TEN)
REFERENCES NGUOI_AN(TEN);

ALTER TABLE AN
ADD CONSTRAINT fk_an
FOREIGN KEY (TEN)
REFERENCES NGUOI_AN(TEN);

ALTER TABLE PHUC_VU ADD CHECK(GIA > 0);

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

-- Câu 2
SELECT PIZZA
FROM PHUC_VU
WHERE QUANPIZZA = 'Pizza Hut';

-- Câu 3
SELECT DISTINCT PIZZA
FROM PHUC_VU;

-- Câu 4
SELECT DISTINCT QUANPIZZA
FROM PHUC_VU
WHERE QUANPIZZA LIKE '%m%';

-- Câu 5
SELECT n.TEN, n.TUOI
FROM NGUOI_AN n JOIN LUI_TOI l ON n.TEN = l.TEN
WHERE l.QUANPIZZA = 'Dominos'
ORDER BY n.TUOI DESC;

-- Câu 6
SELECT QUANPIZZA, COUNT(*) SOBANHPIZZA
FROM PHUC_VU
GROUP BY QUANPIZZA;

-- Câu 7
SELECT QUANPIZZA, GIA
FROM PHUC_VU
GROUP BY QUANPIZZA, GIA
HAVING GIA = (SELECT MAX(GIA) FROM PHUC_VU);

-- Câu 8
SELECT DISTINCT p.QUANPIZZA
FROM PHUC_VU p JOIN AN a ON p.PIZZA = a.PIZZA
                JOIN NGUOI_AN n ON a.TEN = n.TEN
WHERE n.TEN = 'Ian';

-- Câu 9
SELECT DISTINCT p.PIZZA
FROM PHUC_VU p JOIN AN a ON p.PIZZA = a.PIZZA
                JOIN NGUOI_AN n ON a.TEN = n.TEN
WHERE p.PIZZA NOT IN (
                SELECT DISTINCT p.PIZZA
                FROM PHUC_VU p JOIN AN a ON p.PIZZA = a.PIZZA
                                JOIN NGUOI_AN n ON a.TEN = n.TEN
                WHERE n.TEN = 'Eli'
);

-- Câu 10
SELECT DISTINCT p.PIZZA
FROM PHUC_VU p JOIN AN a ON p.PIZZA = a.PIZZA
                JOIN NGUOI_AN n ON a.TEN = n.TEN
WHERE n.TEN = 'Eli';

-- Câu 11
SELECT QUANPIZZA, GIA
FROM PHUC_VU
GROUP BY QUANPIZZA, GIA
HAVING GIA > ALL (
        SELECT GIA
        FROM PHUC_VU
        WHERE QUANPIZZA = 'New York Pizza'
);

-- Câu 12
SELECT * FROM PHUC_VU;

SELECT DISTINCT p.QUANPIZZA
FROM PHUC_VU p JOIN AN a ON p.pizza = a.pizza
WHERE p.gia < 10 AND p.QUANPIZZA NOT IN (
      SELECT p2.QUANPIZZA
      FROM PHUC_VU p2 JOIN AN a2 ON p2.PIZZA = a2.PIZZA
      WHERE p2.GIA >= 10
);

-- Câu 13
SELECT PIZZA
FROM PHUC_VU
WHERE QUANPIZZA = 'New York Pizza'
INTERSECT
SELECT PIZZA
FROM PHUC_VU
WHERE QUANPIZZA = 'Dominos';

-- Câu 14
SELECT PIZZA
FROM PHUC_VU
WHERE QUANPIZZA = 'Little Caesars'
MINUS
SELECT PIZZA
FROM PHUC_VU
WHERE QUANPIZZA = 'Pizza Hut';

-- Câu 15
SELECT p.quanPizza
FROM PHUC_VU p JOIN AN a ON p.pizza = A.pizza
GROUP BY p.quanPizza
HAVING COUNT(DISTINCT a.pizza) = (SELECT COUNT(DISTINCT pizza) FROM AN);

-- Câu 16
SELECT DISTINCT p.QUANPIZZA, COUNT(p.PIZZA) SOBANH
FROM PHUC_VU p JOIN AN a ON p.PIZZA = a.PIZZA
                JOIN NGUOI_AN n ON a.TEN = n.TEN
WHERE n.TEN = 'Gus'
GROUP BY p.QUANPIZZA
HAVING COUNT(p.PIZZA) >= 2;

-- Câu 17
SELECT p.quanPizza
FROM PHUC_VU p JOIN AN a ON p.pizza = a.pizza
                JOIN NGUOI_AN n ON a.ten = n.ten
WHERE n.ten = 'Ian'
GROUP BY p.quanPizza
HAVING COUNT(DISTINCT a.pizza) = (SELECT COUNT(DISTINCT pizza) FROM AN WHERE ten = 'Ian');

-- Câu 18
SELECT TEN
FROM LUI_TOI
GROUP BY TEN
HAVING COUNT(*) >= 3;

-- Câu 19
SELECT QUANPIZZA, COUNT(*) SOBANHPIZZA
FROM PHUC_VU
GROUP BY QUANPIZZA;

-- Câu 20
SELECT NA.ten
FROM NGUOI_AN NA JOIN AN A1 ON NA.ten = A1.ten
WHERE A1.pizza IN (SELECT A2.pizza FROM AN A2 WHERE A2.ten = 'Hil')
GROUP BY NA.ten
HAVING COUNT(DISTINCT A1.pizza) >= (SELECT COUNT(DISTINCT A3.pizza) FROM AN A3 WHERE A3.ten = 'Hil');
