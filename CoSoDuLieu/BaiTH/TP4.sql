CREATE TABLE KTRUCSU(
    HOTEN_KTS VARCHAR(20) PRIMARY KEY,
    NAMS_KTS INT NULL,
    PHAI CHAR(2) NULL,
    NOI_TN VARCHAR(15) NULL,
    DCHI_LL_KTS VARCHAR(30) NULL
);

CREATE TABLE CHUTHAU(
    TEN_THAU VARCHAR(20) PRIMARY KEY,
    TEL CHAR(7) NULL,
    DCHI_THAU VARCHAR(20) NULL
);

CREATE TABLE CHUNHAN(
    TEN_CHU VARCHAR(20) PRIMARY KEY,
    DCHI_CHU VARCHAR(20) NULL
);

CREATE TABLE CONGNHAN(
    HOTEN_CN VARCHAR(30) PRIMARY KEY,
    NAMS_CN INT NULL,
    NAM_VAO_N INT NULL,
    CH_MON VARCHAR(10) NULL
);

CREATE TABLE CGTRINH(
    STT_CTR SMALLINT PRIMARY KEY,
    TEN_CTR VARCHAR(20) NULL,
    DIACHI_CTR VARCHAR(20) NULL,
    TINH_THANH VARCHAR(15) NULL,
    KINH_PHI INT NULL,
    TEN_CHU VARCHAR(20) REFERENCES CHUNHAN(TEN_CHU),
    TEN_THAU VARCHAR(20) REFERENCES CHUTHAU(TEN_THAU),
    NGAY_BD DATE NULL
);

CREATE TABLE THAMGIA(
    HOTEN_CN VARCHAR(30) REFERENCES CONGNHAN(HOTEN_CN),
    STT_CTR SMALLINT REFERENCES CGTRINH(STT_CTR),
    NGAY_TGIA DATE NULL,
    SO_NGAY INT NULL
);

ALTER TABLE THAMGIA ADD PRIMARY KEY(HOTEN_CN, STT_CTR);

CREATE TABLE THIETKE(
    HOTEN_KTS VARCHAR(20) REFERENCES KTRUCSU(HOTEN_KTS),
    STT_CTR SMALLINT REFERENCES CGTRINH(STT_CTR),
    THU_LAO INT NULL,
    PRIMARY KEY (HOTEN_KTS, STT_CTR)
);

insert into  chunhan values ('so t mai du lich','54 xo viet nghe tinh');
insert into  chunhan values ('so van hoa thong tin','101 hai ba trung');
insert into  chunhan values ('so giao duc','29 duong 3/2');
insert into  chunhan values ('dai hoc can tho','56 duong 30/4');
insert into  chunhan values ('cty bitis','29 phan dinh phung');
insert into  chunhan values ('nguyen thanh ha','45 de tham');
insert into  chunhan values ('phan thanh liem','48/6 huynh thuc khan');

insert into  chuthau values ('cty xd so 6','567456','5 phan chu trinh');
insert into  chuthau values ('phong dich vu so xd','206481','2 le van sy');
insert into  chuthau values ('le van son','028374','12 tran nhan ton');
insert into  chuthau values ('tran khai hoan','658432','20 nguyen thai hoc');

insert into  congnhan values ('nguyen thi suu',   45 ,    60  ,'ho');
insert into  congnhan values ('vi chi a',   66  ,    87  ,'han');
insert into  congnhan values ('le manh quoc',   56  ,    71 ,'moc');
insert into  congnhan values ('vo van chin',   40 ,    52  ,'son');
insert into  congnhan values ('le quyet thang',   54  ,    74 ,'son');
insert into  congnhan values ('nguyen hong van',   50  ,    70   ,'dien');
insert into  congnhan values ('dang van son',   48,    65 ,'dien');

insert into  ktrucsu values ('le thanh tung',   1956          ,'1','tp hcm','25 duong 3/2 tp bien hoa');
insert into  ktrucsu values ('le kim dung',   1952          ,'0','ha noi','18/5 phan van tri tp can tho');
insert into  ktrucsu values ('nguyen anh thu',   1970          ,'0','new york usa','khu i dhct tp can tho');
insert into  ktrucsu values ('nguyen song do quyen',   1970          ,'0','tp hcm','73 tran hung dao tp hcm');
insert into  ktrucsu values ('truong minh thai',   1950          ,'1','paris france','12/2/5 tran phu tp hanoi');

insert into  cgtrinh values 
( 1       ,'khach san quoc te','5 nguyen an ninh','can tho',450 ,'so t mai du lich','cty xd so 6','dec-13-1994'); 
insert into  cgtrinh values 
( 2       ,'cong vien thieu nhi','100 nguyen thai hoc','can tho',   200         ,'so van hoa thong tin','cty xd so 6','may-08-1994'); 
insert into  cgtrinh values 
( 3       ,'hoi cho nong nghiep','bai cat','vinh long',   1000        ,'so t mai du lich','phong dich vu so xd','jun-10-1994'); 
insert into  cgtrinh values 
( 4       ,'truong mg mang non','48 cm thang 8','can tho',   30          ,'so giao duc','le van son','jun-10-1994'); 
insert into  cgtrinh values 
( 5       ,'khoa trong trot dhct','khu ii dhct','can tho',   3000        ,'dai hoc can tho','le van son','jun-10-1994'); 
insert into  cgtrinh values 
( 6       ,'van phong bitis','25 phan dinh phung','ha noi',   40          ,'cty bitis','le van son','oct-05-1994'); 
insert into  cgtrinh values 
( 7       ,'nha rieng 1','124/5 nguyen trai','tp hcm',   65          ,'nguyen thanh ha','phong dich vu so xd','nov-15-1994'); 
insert into  cgtrinh values 
( 8       ,'nha rieng 2','76 chau van liem','ha noi',   100         ,'phan thanh liem','tran khai hoan','sep-06-1994'); 

insert into  thamgia values ('nguyen thi suu',   2       ,'may-08-1994',   20          );
insert into  thamgia values ('nguyen thi suu',   4       ,'sep-07-1994',   20          );
insert into  thamgia values ('nguyen thi suu',   1       ,'dec-15-1994',   5           );
insert into  thamgia values ('le manh quoc',   1       ,'dec-18-1994',   6           );
insert into  thamgia values ('vo van chin',   2       ,'may-10-1994',   10          );
insert into  thamgia values ('le quyet thang',   2       ,'may-12-1994',   5           );
insert into  thamgia values ('nguyen hong van',   1       ,'dec-16-1994',   7           );
insert into  thamgia values ('nguyen hong van',   4       ,'sep-14-1994',   7           );
insert into  thamgia values ('dang van son',   3       ,'jun-10-1994',   18          );
insert into  thamgia values ('vo van chin',   3       ,'jun-10-1994',   10          );

insert into  thietke values ('le thanh tung',   1       ,    25          );
insert into  thietke values ('le kim dung',   5       ,    30          );
insert into  thietke values ('truong minh thai',   8       ,    18          );
insert into  thietke values ('le kim dung',   6       ,    40          );
insert into  thietke values ('nguyen anh thu',   3       ,    12          );
insert into  thietke values ('le thanh tung',   7       ,    10          );
insert into  thietke values ('nguyen song do quyen',   2       ,    6           );
insert into  thietke values ('truong minh thai',   6       ,    27          );
insert into  thietke values ('le kim dung',   4       ,    20          );
insert into  thietke values ('truong minh thai',   1       ,    12          );

-- Câu 2
SELECT * FROM CHUNHAN;
SELECT * FROM CHUTHAU;
SELECT * FROM CONGNHAN;
SELECT * FROM KTRUCSU;
SELECT * FROM CGTRINH;
SELECT * FROM THAMGIA;
SELECT * FROM CGTRINH;
SELECT * FROM THIETKE;

-- Câu 3
SELECT *
FROM KTRUCSU
WHERE hoten_kts LIKE 'le%' AND NAMS_KTS = 1956;

-- Câu 4
SELECT TEN_CTR
FROM CGTRINH
WHERE NGAY_BD BETWEEN 'SEP-01-1994' AND 'OCT-20-1994';

-- Câu 5
SELECT TEN_CTR, DIACHI_CTR
FROM CGTRINH
WHERE TEN_THAU = 'cty xd so 6';

-- Câu 6
SELECT DISTINCT ct.TEN_THAU, ct.DCHI_THAU
FROM CHUTHAU ct JOIN CGTRINH c ON ct.ten_thau = c.ten_thau
                JOIN THIETKE t ON c.stt_ctr = t.stt_ctr
WHERE t.hoten_kts='le kim dung';

-- Câu 7
SELECT DISTINCT k.NOI_TN
FROM KTRUCSU k JOIN THIETKE t ON k.HOTEN_KTS = t.HOTEN_KTS
              JOIN CGTRINH c ON t.STT_CTR = c.STT_CTR
WHERE c.ten_ctr='khach san quoc te';

-- Câu 8
SELECT cn.HOTEN_CN, cn.NAMS_CN, cn.NAM_VAO_N
FROM CONGNHAN cn JOIN THAMGIA tg ON cn.hoten_cn = tg.hoten_cn
                 JOIN CGTRINH ct ON tg.stt_ctr = ct.stt_ctr
WHERE (cn.ch_mon='han' or cn.ch_mon='dien') and ct.TEN_THAU='le van son';

-- Câu 9
SELECT tg.HOTEN_CN
FROM THAMGIA tg JOIN CGTRINH ct ON tg.stt_ctr = ct.stt_ctr
WHERE tg.NGAY_TGIA BETWEEN 'DEC-15-1994' AND 'DEC-31-1994'
        AND ct.TEN_CTR = 'khach san quoc te' AND ct.TINH_THANH = 'can tho';

-- Câu 10
SELECT k.HOTEN_KTS
FROM KTRUCSU k JOIN THIETKE tk ON k.hoten_kts = tk.hoten_kts
                JOIN CGTRINH ct ON tk.stt_ctr = ct.stt_ctr
WHERE k.NOI_TN = 'tp hcm' AND ct.KINH_PHI > 400;

-- Câu 11
SELECT DISTINCT cn.HOTEN_CN, cn.CH_MON
FROM CONGNHAN cn JOIN THAMGIA tg ON cn.hoten_cn = tg.hoten_cn
                 JOIN THIETKE tk ON tg.stt_ctr = tk.stt_ctr
WHERE tk.HOTEN_KTS = 'le thanh tung';

-- Câu 12
SELECT TEN_CTR
FROM (
    SELECT TEN_CTR, KINH_PHI
    FROM CGTRINH
    GROUP BY TEN_CTR, KINH_PHI
    HAVING KINH_PHI = (SELECT MAX(KINH_PHI) FROM CGTRINH) 
);

-- Câu 13
SELECT HOTEN_KTS
FROM (
    SELECT HOTEN_KTS, NAMS_KTS
    FROM KTRUCSU
    GROUP BY HOTEN_KTS, NAMS_KTS
    HAVING NAMS_KTS = (SELECT MAX(NAMS_KTS) FROM KTRUCSU) );

-- Câu 14
SELECT TEN_THAU, SUM(KINH_PHI) TONGKINHPHI
FROM CGTRINH
GROUP BY TEN_THAU;

-- Câu 15
SELECT TEN_THAU, DCHI_THAU
FROM (
    SELECT ct.TEN_THAU, ct.DCHI_THAU, ctr.KINH_PHI
    FROM CHUTHAU ct JOIN CGTRINH ctr ON ct.ten_thau = ctr.ten_thau
    GROUP BY ct.TEN_THAU, ct.DCHI_THAU, ctr.KINH_PHI
    HAVING ctr.KINH_PHI = (SELECT MIN(KINH_PHI) FROM CGTRINH) );

-- Câu 16
SELECT HOTEN_KTS
FROM (
    SELECT HOTEN_KTS, SUM(THU_LAO) TONGTHULAO
    FROM THIETKE
    GROUP BY HOTEN_KTS )
WHERE TONGTHULAO > 25;

-- Câu 17
SELECT COUNT(*) SOKIENTRUCSU
FROM (
    SELECT HOTEN_KTS, SUM(THU_LAO) TONGTHULAO
    FROM THIETKE
    GROUP BY HOTEN_KTS )
WHERE TONGTHULAO > 25;

-- Câu 18
SELECT HOTEN_KTS, COUNT(*) SOCONGTRINH
FROM THIETKE
GROUP BY HOTEN_KTS;

-- Câu 19
CREATE TABLE CAU19 AS
SELECT STT_CTR, COUNT(*) SOCONGNHAN
FROM THAMGIA
GROUP BY STT_CTR;

-- Câu 20
SELECT DISTINCT TEN_CTR, DIACHI_CTR
FROM CGTRINH ct JOIN THAMGIA tg ON ct.STT_CTR = tg.STT_CTR
GROUP BY TEN_CTR, DIACHI_CTR
HAVING COUNT(*) = (SELECT MAX(SOCONGNHAN) FROM CAU19);

-- Câu 21
SELECT TINH_THANH, AVG(KINH_PHI) KINHPHITRUNGBINH
FROM CGTRINH
GROUP BY TINH_THANH;

-- Câu 22
SELECT ct.TEN_CTR, ct.DIACHI_CTR
FROM CGTRINH ct JOIN THAMGIA tg ON ct.STT_CTR = tg.STT_CTR
WHERE 'DEC-18-1994' BETWEEN tg.NGAY_TGIA AND (tg.NGAY_TGIA + SO_NGAY) AND tg.HOTEN_CN = 'nguyen hong van';

-- Câu 23
SELECT tk.HOTEN_KTS
FROM THIETKE tk JOIN CGTRINH ct ON tk.STT_CTR = ct.STT_CTR
WHERE ct.TEN_THAU='phong dich vu so xd'
INTERSECT
SELECT tk.HOTEN_KTS
FROM THIETKE tk JOIN CGTRINH ct ON tk.STT_CTR = ct.STT_CTR
WHERE ct.TEN_THAU='cty xd so 6';

-- Câu 24
SELECT DISTINCT tg.HOTEN_CN
FROM THAMGIA tg JOIN CGTRINH ct ON tg.STT_CTR = ct.STT_CTR
WHERE ct.TINH_THANH = 'can tho'
MINUS
SELECT DISTINCT tg.HOTEN_CN
FROM THAMGIA tg JOIN CGTRINH ct ON tg.STT_CTR = ct.STT_CTR
WHERE ct.TINH_THANH = 'vinh long';

-- Câu 25
SELECT TEN_THAU, KINH_PHI
FROM CGTRINH
WHERE KINH_PHI > ALL (
                        SELECT KINH_PHI
                        FROM CGTRINH
                        WHERE TEN_THAU = 'phong dich vu so xd' );

-- Câu 26
SELECT DISTINCT HOTEN_KTS
FROM THIETKE
WHERE THU_LAO < (SELECT AVG(THU_LAO) FROM THIETKE); 

-- Câu 27
SELECT HOTEN_CN, SUM(SO_NGAY)
FROM THAMGIA
GROUP BY HOTEN_CN
HAVING SUM(SO_NGAY) > (SELECT SUM(SO_NGAY)
                 FROM THAMGIA
                 WHERE HOTEN_CN = 'nguyen hong van') ;
                 
-- Câu 28
SELECT HOTEN_CN
FROM THAMGIA
GROUP BY HOTEN_CN
HAVING COUNT(*) = (SELECT COUNT(*) FROM CGTRINH);

-- Câu 29
SELECT DISTINCT a.TEN_THAU, b.TEN_THAU
FROM CGTRINH a JOIN CGTRINH b ON a.TINH_THANH = b.TINH_THANH
WHERE a.TEN_THAU < b.TEN_THAU;

-- Câu 30
SELECT DISTINCT a.HOTEN_CN, b.HOTEN_CN
FROM THAMGIA a JOIN THAMGIA b ON a.STT_CTR = b.STT_CTR
WHERE a.HOTEN_CN > b.HOTEN_CN
GROUP BY a.HOTEN_CN, b.HOTEN_CN
HAVING COUNT(*) > 1
ORDER BY a.HOTEN_CN, b.HOTEN_CN;

-- H? tên KTS có t?ng thù lao > c?a 'le thanh tung'
SELECT HOTEN_KTS, SUM(THU_LAO) TONGTHULAO
FROM THIETKE
GROUP BY HOTEN_KTS
HAVING SUM(THU_LAO) > (SELECT SUM(THU_LAO) FROM THIETKE WHERE HOTEN_KTS='le thanh tung');

-- H? tên KTS có thi?t k? s? công trình b?ng vs s? công trình c?a 'truong minh thai'
SELECT HOTEN_KTS, COUNT(STT_CTR) SOCONGTRINH
FROM THIETKE
GROUP BY HOTEN_KTS
HAVING COUNT(STT_CTR) = (SELECT COUNT(STT_CTR) FROM THIETKE WHERE HOTEN_KTS = 'truong minh thai');


