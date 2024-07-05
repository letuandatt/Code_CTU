---- Truy v?n
-- C�u 1
SELECT TENLOAI
FROM LOAI l JOIN MAY m
    ON l.idLoai = m.idLoai
WHERE idMay='p8';

-- C�u 2
SELECT tenPM
FROM PHANMEM
WHERE idLoai='UNIX';

-- C�u 3
SELECT DISTINCT p.tenphong, p.IP, p.MP
FROM PHONG p JOIN MAY m
ON p.MP = m.MP
WHERE idLoai='UNIX' or idLoai='PCWS';

-- C�u 4
SELECT DISTINCT p.tenphong, p.IP, p.MP
FROM PHONG p JOIN MAY m
ON p.MP = m.MP
WHERE (idLoai='UNIX' or idLoai='PCWS') and p.IP='130.120.80'
ORDER BY p.MP;

-- C�u 5
SELECT COUNT(*) SOPHANMEMP6
FROM CAIDAT
WHERE idMay='p6';

-- C�u 6
SELECT COUNT(*) SOMAYLOG1
FROM CAIDAT
WHERE idPM='log1';

-- C�u 7
SELECT tenmay, IP
FROM MAY
WHERE idloai = 'TX';

-- C�u 8
SELECT idMay, COUNT(idPM) SOPHANMEM
FROM CAIDAT
GROUP BY idMay;

-- C�u 9
SELECT TENPHONG, SUM(SOMAY) SOMAYMOIPHONG
FROM PHONG
GROUP BY TENPHONG;

-- C�u 10
SELECT idPM, idMay, COUNT(idCD) SOLANCAIDAT
FROM CAIDAT
GROUP BY idPM, idMay
ORDER BY idPM;

-- C�u 11
SELECT AVG(gia) GIATRUNGBINHUNIX
FROM PHANMEM
WHERE idLoai='UNIX';

-- C�u 12
SELECT MAX(ngaymua) NGAYMUAGANNHAT
FROM PHANMEM;

-- C�u 13
SELECT idmay, COUNT (*) SOMAY
FROM Caidat
GROUP BY idMay
HAVING COUNT (*) >= 2;

-- C�u 14
SELECT COUNT (*) SOMAY
FROM (
    SELECT idmay, COUNT (*) SO_MAY
    FROM Caidat
    GROUP BY idmay
    HAVING COUNT (*) >= 2
);

-- C�u 15
SELECT idLoai, tenLoai
FROM LOAI
WHERE idLoai NOT IN (SELECT idLoai FROM MAY); -- C�ch 1

SELECT idLoai
FROM LOAI
MINUS
SELECT idLoai
FROM MAY; -- C�ch 2

SELECT DISTINCT l.idLoai, l.tenLoai
FROM LOAI l LEFT JOIN MAY m ON l.idLoai=m.idLoai
WHERE m.idMay IS NULL;

-- C�u 16
SELECT idLoai, tenLoai
FROM LOAI
WHERE idLoai IN (SELECT idLoai FROM MAY WHERE idLoai IN (SELECT idLoai FROM PHANMEM)); -- C�ch 1

SELECT idLoai
FROM May
INTERSECT
SELECT idLoai
FROM Phanmem; -- C�ch 2

SELECT DISTINCT l.idLoai, l.tenLoai
FROM LOAI l LEFT JOIN MAY m ON l.idLoai=m.idLoai
            LEFT JOIN PHANMEM p ON l.idLoai=p.idLoai
WHERE m.idMay IS NOT NULL and p.idPM IS NOT NULL;

-- C�u 17
SELECT idLoai, tenLoai
FROM LOAI
WHERE idLoai NOT IN (SELECT idLoai FROM PHANMEM); -- C�ch 1

SELECT idLoai
FROM LOAI
MINUS
SELECT idLoai
FROM PHANMEM; -- C�ch 2

SELECT DISTINCT l.idLoai, l.tenLoai
FROM LOAI l LEFT JOIN PHANMEM p ON l.idLoai=p.idLoai
WHERE p.idPM IS NULL;

-- C�u 18
SELECT DISTINCT IP
FROM MAY
WHERE idMay IN (
    SELECT idMay
    FROM CAIDAT
    WHERE idPM='log6'
);

-- C�u 19
SELECT DISTINCT IP
FROM MAY
WHERE idMay IN (
    SELECT idMay
    FROM CAIDAT
    WHERE idPM IN (
        SELECT idPM
        FROM PHANMEM
        WHERE tenPM='Oracle 8'
    )
); -- Select

SELECT DISTINCT m.IP
FROM MAY m JOIN CAIDAT cd ON m.idMay = cd.idMay
            JOIN PHANMEM pm ON cd.idPM = pm.idPM
WHERE pm.tenPM='Oracle 8'; -- JOIN

-- C�u 20
SELECT tenKhuvuc, IP
FROM KHUVUC
WHERE IP IN (
    SELECT IP
    FROM MAY
    WHERE (idLoai='TX')
    GROUP BY IP
    HAVING COUNT(*) = 3
); -- Select l?ng nhau

SELECT DISTINCT k.TENKHUVUC, k.IP
FROM KHUVUC k JOIN MAY m ON k.IP = m.IP
                JOIN PHONG p ON k.IP = p.IP
WHERE m.idLoai='TX' AND p.somay = 3; -- JOIN

-- C�u 21
SELECT tenphong
FROM PHONG
WHERE MP IN (
    SELECT MP
    FROM MAY
    WHERE idMay IN (
        SELECT idMay
        FROM CAIDAT
        WHERE idPM IN (
            SELECT idPM
            FROM PHANMEM
            WHERE tenPM='Oracle 6'
        )
        GROUP BY idMay
        HAVING COUNT(*) >= 1
    )
); -- Select l?ng nhau

SELECT DISTINCT P.tenphong
FROM PHONG P JOIN MAY M ON P.MP = M.MP
            JOIN CAIDAT C ON M.idMay = C.idMay
            JOIN PHANMEM PM ON C.idPM = PM.idPM
WHERE PM.tenPM = 'Oracle 6'; -- JOIN

-- C�u 22
SELECT tenPM
FROM PHANMEM
WHERE ngaymua = (
    SELECT MAX(ngaymua) NGAYMUAGANNHAT
    FROM PHANMEM
);

-- C�u 23
SELECT tenMay
FROM MAY
WHERE idMay IN (
    SELECT idMay
    FROM Caidat
    WHERE idMay != 'p6' AND idPM IN (
        SELECT idPM
        FROM caidat
        WHERE idMay = 'p6'
    )
); -- Ch?a fix, thi?u p1 -- Data b?ng CAIDAT kh�ng c� p1

-- C�u 24
SELECT tenPM, gia
FROM PHANMEM
WHERE (idloai = 'PCNT' AND gia > ANY (
        SELECT gia
        FROM PHANMEM
        WHERE idloai = 'UNIX'
    )
);

-- C�u 25
SELECT tenPM, gia
FROM PHANMEM
WHERE (idloai = 'UNIX' AND gia > ALL (
        SELECT gia
        FROM PHANMEM
        WHERE idloai = 'PCNT'
    )
);

-- C�u 26
SELECT tenMay
FROM MAY
WHERE idMay IN (
    SELECT idMay
    FROM Caidat
    WHERE idMay != 'p6' AND idPM IN (
        SELECT idPM
        FROM caidat
        WHERE idMay = 'p6'
    )
);

-- C�u 27
SELECT tenMay
FROM MAY
WHERE idMay IN (
    SELECT idMay
    FROM Caidat
    WHERE idMay != 'p2' AND idPM IN (
        SELECT idPM
        FROM caidat
        WHERE idMay = 'p2'
    )
); -- Ch?a fix

---- ??nh d?ng ng�y trong file: MM/DD/YYYY (APEX)