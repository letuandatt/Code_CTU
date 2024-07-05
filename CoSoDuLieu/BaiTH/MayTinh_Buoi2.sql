---- Truy v?n
-- Câu 1
SELECT TENLOAI
FROM LOAI l JOIN MAY m
    ON l.idLoai = m.idLoai
WHERE idMay='p8';

-- Câu 2
SELECT tenPM
FROM PHANMEM
WHERE idLoai='UNIX';

-- Câu 3
SELECT DISTINCT p.tenphong, p.IP, p.MP
FROM PHONG p JOIN MAY m
ON p.MP = m.MP
WHERE idLoai='UNIX' or idLoai='PCWS';

-- Câu 4
SELECT DISTINCT p.tenphong, p.IP, p.MP
FROM PHONG p JOIN MAY m
ON p.MP = m.MP
WHERE (idLoai='UNIX' or idLoai='PCWS') and p.IP='130.120.80'
ORDER BY p.MP;

-- Câu 5
SELECT COUNT(*) SOPHANMEMP6
FROM CAIDAT
WHERE idMay='p6';

-- Câu 6
SELECT COUNT(*) SOMAYLOG1
FROM CAIDAT
WHERE idPM='log1';

-- Câu 7
SELECT tenmay, IP
FROM MAY
WHERE idloai = 'TX';

-- Câu 8
SELECT idMay, COUNT(idPM) SOPHANMEM
FROM CAIDAT
GROUP BY idMay;

-- Câu 9
SELECT TENPHONG, SUM(SOMAY) SOMAYMOIPHONG
FROM PHONG
GROUP BY TENPHONG;

-- Câu 10
SELECT idPM, idMay, COUNT(idCD) SOLANCAIDAT
FROM CAIDAT
GROUP BY idPM, idMay
ORDER BY idPM;

-- Câu 11
SELECT AVG(gia) GIATRUNGBINHUNIX
FROM PHANMEM
WHERE idLoai='UNIX';

-- Câu 12
SELECT MAX(ngaymua) NGAYMUAGANNHAT
FROM PHANMEM;

-- Câu 13
SELECT idmay, COUNT (*) SOMAY
FROM Caidat
GROUP BY idMay
HAVING COUNT (*) >= 2;

-- Câu 14
SELECT COUNT (*) SOMAY
FROM (
    SELECT idmay, COUNT (*) SO_MAY
    FROM Caidat
    GROUP BY idmay
    HAVING COUNT (*) >= 2
);

-- Câu 15
SELECT idLoai, tenLoai
FROM LOAI
WHERE idLoai NOT IN (SELECT idLoai FROM MAY); -- Cách 1

SELECT idLoai
FROM LOAI
MINUS
SELECT idLoai
FROM MAY; -- Cách 2

SELECT DISTINCT l.idLoai, l.tenLoai
FROM LOAI l LEFT JOIN MAY m ON l.idLoai=m.idLoai
WHERE m.idMay IS NULL;

-- Câu 16
SELECT idLoai, tenLoai
FROM LOAI
WHERE idLoai IN (SELECT idLoai FROM MAY WHERE idLoai IN (SELECT idLoai FROM PHANMEM)); -- Cách 1

SELECT idLoai
FROM May
INTERSECT
SELECT idLoai
FROM Phanmem; -- Cách 2

SELECT DISTINCT l.idLoai, l.tenLoai
FROM LOAI l LEFT JOIN MAY m ON l.idLoai=m.idLoai
            LEFT JOIN PHANMEM p ON l.idLoai=p.idLoai
WHERE m.idMay IS NOT NULL and p.idPM IS NOT NULL;

-- Câu 17
SELECT idLoai, tenLoai
FROM LOAI
WHERE idLoai NOT IN (SELECT idLoai FROM PHANMEM); -- Cách 1

SELECT idLoai
FROM LOAI
MINUS
SELECT idLoai
FROM PHANMEM; -- Cách 2

SELECT DISTINCT l.idLoai, l.tenLoai
FROM LOAI l LEFT JOIN PHANMEM p ON l.idLoai=p.idLoai
WHERE p.idPM IS NULL;

-- Câu 18
SELECT DISTINCT IP
FROM MAY
WHERE idMay IN (
    SELECT idMay
    FROM CAIDAT
    WHERE idPM='log6'
);

-- Câu 19
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

-- Câu 20
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

-- Câu 21
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

-- Câu 22
SELECT tenPM
FROM PHANMEM
WHERE ngaymua = (
    SELECT MAX(ngaymua) NGAYMUAGANNHAT
    FROM PHANMEM
);

-- Câu 23
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
); -- Ch?a fix, thi?u p1 -- Data b?ng CAIDAT không có p1

-- Câu 24
SELECT tenPM, gia
FROM PHANMEM
WHERE (idloai = 'PCNT' AND gia > ANY (
        SELECT gia
        FROM PHANMEM
        WHERE idloai = 'UNIX'
    )
);

-- Câu 25
SELECT tenPM, gia
FROM PHANMEM
WHERE (idloai = 'UNIX' AND gia > ALL (
        SELECT gia
        FROM PHANMEM
        WHERE idloai = 'PCNT'
    )
);

-- Câu 26
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

-- Câu 27
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

---- ??nh d?ng ngày trong file: MM/DD/YYYY (APEX)