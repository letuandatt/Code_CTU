-- C�u 1
CREATE TABLE KHOAHOC(
    MAKH CHAR(4) PRIMARY KEY,
    TENKH CHAR(6) NOT NULL,
    NGAYBD DATE,
    NGAYKT DATE
);

ALTER TABLE KHOAHOC ADD CHECK(NGAYKT > NGAYBD);

CREATE TABLE CHUONGTRINH(
    MACT CHAR(5) PRIMARY KEY,
    TENCT VARCHAR(50) NOT NULL
);

CREATE TABLE LOAILOP(
    MALOAI CHAR(5) PRIMARY KEY,
    MACT CHAR(5) REFERENCES CHUONGTRINH(MACT),
    TENLOAI VARCHAR(30) NOT NULL
);

CREATE TABLE LOP(
    MALOP CHAR(4) PRIMARY KEY,
    MALOAI CHAR(5) REFERENCES LOAILOP(MALOAI),
    TENLOP CHAR(7) NOT NULL,
    SISO SMALLINT CHECK(SISO>12),
    MAKH CHAR(4) REFERENCES KHOAHOC(MAKH)
);

CREATE TABLE HOCVIEN(
    MAHV CHAR(6) PRIMARY KEY,
    TENHV VARCHAR(25) NOT NULL,
    GIOITINH SMALLINT CHECK(GIOITINH=0 OR GIOITINH=1),
    NGAYSINH DATE,
    SDT CHAR(9),
    DIACHI VARCHAR(50)
);

CREATE TABLE PHIEUTHU(
    SOPT CHAR(8) PRIMARY KEY,
    MAHV CHAR(6) REFERENCES HOCVIEN(MAHV),
    MALOP CHAR(4) REFERENCES LOP(MALOP),
    NGAYLAPPHIEU DATE,
    THANHTIEN INT CHECK(THANHTIEN>0)
);

CREATE TABLE MONHOC(
    MAMH CHAR(5) PRIMARY KEY,
    TENMH VARCHAR(30) NOT NULL
);

CREATE TABLE DIEM(
    MAMH CHAR(5) REFERENCES MONHOC(MAMH),
    MAHV CHAR(6) REFERENCES HOCVIEN(MAHV),
    MALOP CHAR(4) REFERENCES LOP(MALOP),
    DIEM SMALLINT CHECK(DIEM>=0 AND DIEM <=10)
);

-- C�u 2
INSERT INTO KHOAHOC VALUES('K001','Khoa 1','01/10/2020','03/20/2020');
INSERT INTO KHOAHOC VALUES('K002','Khoa 2','02/28/2020','05/28/2020');
INSERT INTO KHOAHOC VALUES('K003','Khoa 3','04/10/2020','07/20/2020');
INSERT INTO KHOAHOC VALUES('K004','Khoa 4','06/15/2020','09/20/2020');

INSERT INTO CHUONGTRINH VALUES('CT007','Ch?ng ch? Ti?ng Anh 6 B?c(A1,B1,B2,C1)');
INSERT INTO CHUONGTRINH VALUES('CT006','Ch??ng tr�nh CamBrigde');
INSERT INTO CHUONGTRINH VALUES('CT005','Ti?ng Anh IELTS');
INSERT INTO CHUONGTRINH VALUES('CT004','Ch??ng tr�nh TOEIC');
INSERT INTO CHUONGTRINH VALUES('CT003','Ti?ng Anh Luy?n K? N?ng');
INSERT INTO CHUONGTRINH VALUES('CT002','Ti?ng Anh Tr? Em');
INSERT INTO CHUONGTRINH VALUES('CT001','Ti?ng Anh T?ng Qu�t');

INSERT INTO LOAILOP VALUES('LL001','CT001','Ti?ng Anh C?n B?n');
INSERT INTO LOAILOP VALUES('LL002','CT001','Ti?ng Anh A1');
INSERT INTO LOAILOP VALUES('LL003','CT001','Ti?ng Anh A2');
INSERT INTO LOAILOP VALUES('LL004','CT001','Ti?ng Anh B1');
INSERT INTO LOAILOP VALUES('LL005','CT001','Ti?ng Anh B2');
INSERT INTO LOAILOP VALUES('LL006','CT001','Ti?ng Anh C1');

INSERT INTO LOP VALUES('L001','LL001','L?p 1','30','K001');
INSERT INTO LOP VALUES('L002','LL001','L?p 2','30','K001');
INSERT INTO LOP VALUES('L003','LL002','L?p 1','25','K001');

INSERT INTO HOCVIEN VALUES('HV0001','?? B�nh An','1','11/02/2000','917217036','C? ?? - C?n Th?');
INSERT INTO HOCVIEN VALUES('HV0002','?? Gia B?o','1','12/02/2000','917217036','� M�n - C?n Th?');
INSERT INTO HOCVIEN VALUES('HV0003','?? Ph�c Vinh','1','11/02/2000','917217036','C� Lao Dung - S�c Tr?ng');
INSERT INTO HOCVIEN VALUES('HV0004','Th?ch Ch� T�m','1','01/02/2000','917217036','Ch�u Th�nh - An Giang');
INSERT INTO HOCVIEN VALUES('HV0005','L� C?m Giao','0','11/05/2000','917217036','Phong ?i?n - C?n Th?');
INSERT INTO HOCVIEN VALUES('HV0006','Hu?nh Gia B?o','1','11/02/2000','917217036','Phong ?i?n - C?n Th?');
INSERT INTO HOCVIEN VALUES('HV0007','L� Th? B','0','01/02/2001','917217036','Ninh Ki?u - C?n Th?');

INSERT INTO PHIEUTHU VALUES('PT000001','HV0001','L001','06/01/2021',1350000);
INSERT INTO PHIEUTHU VALUES('PT000002','HV0002','L001','06/01/2021',1350000);
INSERT INTO PHIEUTHU VALUES('PT000003','HV0003','L001','06/01/2021',1350000);
INSERT INTO PHIEUTHU VALUES('PT000004','HV0004','L001','06/01/2021',1350000);
INSERT INTO PHIEUTHU VALUES('PT000005','HV0005','L001','06/01/2021',1350000);
INSERT INTO PHIEUTHU VALUES('PT000006','HV0006','L001','06/01/2021',1350000);
INSERT INTO PHIEUTHU VALUES('PT000007','HV0007','L001','06/01/2021',1350000);

-- C�u 3
INSERT INTO PHIEUTHU VALUES('PT00008','HV0012','L001','06/02/2021',1350000); -- B?ng cha ch?a c� d? li?u

-- C�u 4
INSERT INTO LOP VALUES('L004','LL002','L?p 4',10,'K001'); -- Vi ph?m ?i?u ki?n siso>12

-- C�u 5
DELETE FROM KHOAHOC WHERE MAKH='K001'; -- C� d? li?u ? b?ng con

-- C�u 6
DELETE FROM KHOAHOC WHERE MAKH='K002'; -- Kh�ng c� d? li?u ? b?ng con

-- C�u 7
UPDATE PHIEUTHU SET THANHTIEN=(THANHTIEN*0.9) WHERE SOPT='PT000001';

-- C�u 8
ALTER TABLE LOP ADD hocphi INT;

UPDATE LOP SET HOCPHI=1350000 WHERE MALOAI='LL001';
UPDATE LOP SET HOCPHI=1650000 WHERE MALOAI='LL002';

-- C�u 9 + 10
CREATE TABLE HOCVIEN_NAM AS
SELECT *
FROM HOCVIEN
WHERE GIOITINH = 1;

-- C�u 11
DROP TABLE KHOAHOC; -- K th? x�a b?ng cha

-- C�u 12
DROP TABLE HOCVIEN_NAM; -- B?ng n�y k c� con

-- C�u 13
ALTER TABLE MONHOC MODIFY TENMH VARCHAR(100);