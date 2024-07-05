DROP TABLE tdonn;
DROP TABLE nhanvien;
DROP TABLE ngoaingu;
DROP TABLE phong;


CREATE TABLE phong(
    maphong  NUMBER NOT NULL PRIMARY KEY,
    tenphong  VARCHAR2(25),
    truongphong VARCHAR2(3)
);

INSERT INTO phong VALUES(10,	'Phong Hanh Chanh',	'001');
INSERT INTO phong VALUES(20,	'Phong To Chuc',	'006');
INSERT INTO phong VALUES(30,	'Phong Tai Vu',	null);
INSERT INTO phong VALUES(40,	'Phong Dao Tao',	'018');
INSERT INTO phong VALUES(50,	'Phong Thiet Bi',	'063');
INSERT INTO phong VALUES(60,	'Phong Hop Tac Quoc Te',	'064');
INSERT INTO phong VALUES(70,	'Phong Quan Ly Khoa Hoc',	'007');
INSERT INTO phong VALUES(80,	'Phong Cong Tac Sinh Vien',	'086');
INSERT INTO phong VALUES(90,	'Phong Quan Tri Thiet Bi',	'087');

CREATE TABLE nhanvien(
    manv        VARCHAR2(3) NOT NULL PRIMARY KEY,
    hoten       VARCHAR2(25),
    phai        VARCHAR2(3),
    ngaysinh    DATE,
    congviec    VARCHAR2(15)    NOT NULL,
    luong       NUMBER(8,2),
    phucap      NUMBER(8,2),
    maphong     NUMBER  NOT NULL    REFERENCES  phong(maphong)
);

INSERT INTO nhanvien VALUES ('001',	'Tran Thai Ngoc',	'Nam',	'MAY-03-1990',	'Chuyen vien'	,3100.00,	124.00,	10);
INSERT INTO nhanvien VALUES ('002',	'Pham Le Ngoc Han',	'Nu',	'AUG-03-1972',	'Thu ky'		,2800.00,	28.00,	20);
INSERT INTO nhanvien VALUES ('003',	'Le Anh Khoa',		'Nam',	'NOV-04-1980',	'Thu ky'		,3000.00,	30.00,	30);
INSERT INTO nhanvien VALUES ('004',	'Phan Tan Tai',		'Nam',	'JUN-03-1970',	'Chuyen vien'	,3200.00,	NULL,	50);
INSERT INTO nhanvien VALUES ('005',	'Tran Hoai Thanh',	'Nam',	'MAY-12-1987',	'Thu ky'		,	2600.00,	26.00,	10);


INSERT INTO nhanvien VALUES ('006',	'Bui Van Thien',		'Nam',	'OCT-09-1972',	'Chuyen vien',	3700.00,148.00, 20);
INSERT INTO nhanvien VALUES ('007',	'Nguyen Huynh Minh',	'Nam',	'JUL-07-1977',	'Chuyen vien',	2900.00,	116.00,	30);
INSERT INTO nhanvien VALUES ('008',	'Le Dong Binh',			'Nam',	'DEC-05-1984',	'Quan ly',	2900.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('009',	'Tran Thi Thuy Lan',	'Nu',	'OCT-20-1960',	'Quan ly',	2200.00,	NULL,	50);
INSERT INTO nhanvien VALUES ('010',	'Huynh Thi Kim Nguyen',	'Nu',	'MAY-15-1972',	'Tro ly',	3100.00,	NULL,	20);

INSERT INTO nhanvien VALUES ('011',	'Huynh Ho Phuong Thao',		'Nu',	'OCT-20-1983',	'Chuyen vien',	3100.00,	124.00,	30);
INSERT INTO nhanvien VALUES ('012',	'Pham Thanh Thao',			'Nu',	'AUG-08-1975',	'Tro ly',	2800.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('013',	'Lam Thi Hong Thu',			'Nu',	'APR-15-1993',	'Tro ly',	2400.00,	NULL,	50);
INSERT INTO nhanvien VALUES ('014',	'Than Minh Tinh',			'Nam',	'OCT-10-1990',	'Quan ly',	2500.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('015',	'Nguyen Tien Bach',			'Nam',	'SEP-23-1966',	'Chuyen vien',	2600.00,	NULL,	30);

INSERT INTO nhanvien VALUES ('016',	'Nguyen Thi Thuy Ai',	'Nu',	'APR-30-1968',	'Chuyen vien',	2900.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('017',	'Truong Thuy An	',	'Nu',	'OCT-04-1984',	'Tro ly',	2300.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('018',	'Nguyen Thi Van An',	'Nu',	'AUG-08-1980',	'Chuyen vien',	2200.00,	88.00,	40);
INSERT INTO nhanvien VALUES ('019',	'Ho Trong Can',	'Nam',	'NOV-05-1980',	'Chuyen vien',	3100.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('020',	'Thuong Cong Chanh',	'Nam',	'NOV-20-1990',	'Chuyen vien',	2700.00,	NULL,	40);

INSERT INTO nhanvien VALUES ('021',	'Le Dinh Chien',	'Nam',	'FEB-11-1980',	'Chuyen vien',	2500.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('022',	'Lenh Minh Co',	'Nam',	'APR-05-1987',	'Chuyen vien',	3100.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('023',	'Do Van Cuong',	'Nam',	'MAY-23-1970',	'Chuyen vien',	2500.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('024',	'Huynh Hoang Duy',	'Nam',	'JUL-04-1992',	'Chuyen vien',	2100.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('025',	'Nguyen Thai Duong',	'Nam',	'JUN-03-1970',	'Chuyen vien',	2500.00,	NULL,	10);

INSERT INTO nhanvien VALUES ('026',	'Nguyen Tan Dat',	'Nam',	'OCT-06-1977',	'Chuyen vien',	2900.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('027',	'Le Thi Dam',	'Nu',	'OCT-24-1980',	'Tro ly',	2500.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('028',	'Nguyen Van Do',	'Nam',	'JUN-07-1967',	'Chuyen vien',	3200.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('029',	'Nguyen Tri Duc',	'Nam',	'MAY-10-1982',	'Chuyen vien',	3200.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('030',	'Do Luong Thuy Hang',	'Nu',	'AUG-12-1987',	'Chuyen vien',	2400.00,	NULL,	20);

INSERT INTO nhanvien VALUES ('031',	'Ho Minh Hieu',	'Nam',	'NOV-10-1981',	'Chuyen vien',	2600.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('032',	'Chau Van Ho',	'Nam',	'SEP-13-1983',	'Chuyen vien',	4500.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('033',	'Duong Quoc Huy',	'Nam',	'APR-30-1980',	'Chuyen vien',	2200.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('034',	'Le Thi Kim Huong',	'Nu',	'JUN-05-1994',	'Chuyen vien',	2700.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('035',	'Phan Nhat Khang',	'Nu',	'DEC-06-1970',	'Chuyen vien',	2300.00,	NULL,	30);

INSERT INTO nhanvien VALUES ('036',	'Nguyen Minh Khanh',	'Nu',	'MAY-05-1965',	'Chuyen vien',	2700.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('037',	'Nguyen Khiem',	'Nam',	'SEP-13-1974',	'Chuyen vien',	3600.00,	NULL,	60);
INSERT INTO nhanvien VALUES ('038',	'Nguyen Van Khoa',	'Nam',	'DEC-12-1987',	'Chuyen vien',	2000.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('039',	'Duong Kim Lan',	'Nam',	'MAY-25-1987',	'Chuyen vien',	2700.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('040',	'Pham Thi Thanh Loan',	'Nu',	'FEB-21-1992',	'Chuyen vien',	2700.00,	NULL,	40);

INSERT INTO nhanvien VALUES ('041',	'Chau Thanh Long',	'Nu',	'OCT-26-1966',	'Tro ly',	2500.00,	NULL,	60);
INSERT INTO nhanvien VALUES ('042',	'Tong Thi Ngoc Mai',	'Nu',	'MAY-15-1986',	'Chuyen vien',	3100.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('043',	'Le Hoang Minh',	'Nam',	'MAR-03-1982',	'Chuyen vien',	2900.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('044',	'Ngo Huynh Ngoc Minh',	'Nam',	'JAN-28-1970',	'Chuyen vien',	4000.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('045',	'Tran Thi Thuy Lan',	'Nu',	'DEC-23-1990',	'Chuyen vien',	1900.00,	NULL,	10);

INSERT INTO nhanvien VALUES ('046',	'Chau Thi Yen Ngoc',	'Nu',	'OCT-11-1993',	'Chuyen vien',	2100.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('047',	'Nguyen Thi My Ngoc',	'Nu',	'MAY-04-1990',	'Chuyen vien',	2900.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('048',	'Huynh Thi Nguyet',	'Nu',	'APR-03-1973',	'Chuyen vien',	2700.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('049',	'Nguyen Thanh Phong',	'Nam',	'MAY-17-1968',	'Chuyen vien',	3100.00,	NULL,	50);
INSERT INTO nhanvien VALUES ('050',	'Pham Thuy Nhu Phuong',	'Nam',	'DEC-23-1990',	'Chuyen vien',	3000.00,	NULL,	20);

INSERT INTO nhanvien VALUES ('051',	'Le Duy Quang',	'Nam',	'NOV-07-1981',	'Chuyen vien',	4500.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('052',	'Nguyen Van Quoc',	'Nam',	'SEP-05-1975',	'Chuyen vien',	5000.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('053',	'Nguyen Be Sau',	'Nam',	'NOV-20-1978',	'Chuyen vien',	4500.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('054',	'Tran Tan Tai',	'Nam',	'JUL-23-1985',	'Chuyen vien',	3100.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('055',	'Tang Binh Tanh',	'Nam',	'MAY-06-1965',	'Chuyen vien',	2300.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('056',	'Luu Hoang Thach',	'Nam',	'NOV-26-1988',	'Chuyen vien',	3300.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('057',	'Nguyen Ngoc Bang Thanh',	'Nu',	'APR-04-1990',	'Chuyen vien',	3100.00,	NULL,	50);
INSERT INTO nhanvien VALUES ('058',	'Truong Ngoc Thanh',	'Nu',	'SEP-04-1975',	'Chuyen vien',	3100.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('059',	'Le Anh Thi',	'Nam',	'SEP-04-1970',	'Chuyen vien',	2400.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('060',	'Hoang Tu Thien',	'Nam',	'OCT-10-1972',	'Chuyen vien',	4000.00,	NULL,	40);

INSERT INTO nhanvien VALUES ('061',	'Nguyen Anh Thoai',	'Nam',	'JUL-30-1983',	'Chuyen vien',	3100.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('062',	'Nguyen Ngoc Thuan',	'Nam',	'FEB-12-1976',	'Chuyen vien',	2800.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('063',	'Ho Nhu Thuy',	'Nu',	'SEP-28-1987',	'Chuyen vien',	3000.00,	120.00,	50);
INSERT INTO nhanvien VALUES ('064',	'Dang Trung Tin',	'Nam',	'APR-17-1969',	'Chuyen vien',	3200.00,	128.00,	60);
INSERT INTO nhanvien VALUES ('065',	'Nguyen Van Toan',	'Nam',	'MAY-02-1993',	'Chuyen vien',	2600.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('066',	'Pham Thi Kim Trang',	'Nu',	'SEP-09-1990',	'Chuyen vien',	2700.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('067',	'Nguyen Thi Huyen Tran',	'Nu',	'DEC-04-1972',	'Chuyen vien',	2900.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('068',	'Nguyen Minh Tri',	'Nam',	'MAY-29-1981',	'Chuyen vien',	2900.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('069',	'Nguyen Thien Tri',	'Nam',	'AUG-06-1988',	'Chuyen vien',	2200.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('070',	'Vo Thi Phuong Trinh',	'Nu',	'MAY-11-1977',	'Chuyen vien',	3100.00,	NULL,	20);

INSERT INTO nhanvien VALUES ('071',	'Nguyen Thi Kieu Tuyen',	'Nu',	'JUN-06-1966',	'Chuyen vien',	2000.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('072',	'Le Ngoc Tuyen',	'Nu',	'MAY-04-1995',	'Thu ky',	2500.00,	25.00,	40);
INSERT INTO nhanvien VALUES ('073',	'Phan Thi Bich Tuyen',	'Nu',	'MAY-10-1960',	'Chuyen vien',	2400.00,	NULL,	50);
INSERT INTO nhanvien VALUES ('074',	'Tran Anh Tuyet',	'Nu',	'MAR-02-1974',	'Chuyen vien',	3100.00,	NULL,	20);
INSERT INTO nhanvien VALUES ('075',	'Nguyen Thi Ty',	'Nu',	'AUG-09-1992',	'Chuyen vien',	2600.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('076',	'Le Van Ut',	'Nam',	'NOV-28-1990',	'Chuyen vien',	2900.00,	NULL,	40);
INSERT INTO nhanvien VALUES ('077',	'Le Quynh Nhu',	'Nu',	'JAN-01-1990',	'Chuyen vien',	2300.00,	NULL,	10);
INSERT INTO nhanvien VALUES ('078',	'Nguyen Dang Quang Vinh',	'Nam',	'APR-03-1970',	'Chuyen vien',	2200.00,	NULL,	60);
INSERT INTO nhanvien VALUES ('079',	'Le Ngoc Vung',	'Nam',	'OCT-20-1992',	'Chuyen vien',	3100.00,	NULL,	30);
INSERT INTO nhanvien VALUES ('080',	'Cao Thi Nhu Y',	'Nu',	'AUG-18-1995',	'Chuyen vien',	2700.00,	NULL,	40);

INSERT INTO nhanvien VALUES ('081',	'Le Van',	'Nam','NOV-30-1970',	'Chuyen vien',	NULL,	30.00,	50);
INSERT INTO nhanvien VALUES ('082',	'Van Minh Thanh',	'Nam',	'FEB-02-1982',	'Quan ly',	NULL,	NULL,	60);
INSERT INTO nhanvien VALUES ('083',	'Nguyen Thanh Tam',	'Nu',	'NOV-08-1965',	'Chuyen vien',	2500.00,	NULL,	90);
INSERT INTO nhanvien VALUES ('084',	'Nguyen Quang Hai',	'Nam',	'NOV-10-1996',	'Chuyen vien',	2200.00,	NULL,	80);
INSERT INTO nhanvien VALUES ('085',	'Tran Thi Mai',	'Nu',	'NOV-08-1964',	'Chuyen vien',	2200.00,	NULL,	90);
INSERT INTO nhanvien VALUES ('086',	'Luong Van Tru',	'Nam',	'OCT-01-1996',	'Chuyen vien',	3100.00,	310.00,	80);
INSERT INTO nhanvien VALUES ('087',	'Doan Kim Chi',	'Nu',	'MAR-08-1964',	'Chuyen vien',	3100.00,	310.00,	90);
INSERT INTO nhanvien VALUES ('088',	'Van Van Tam',	'Nam',	'NOV-01-1995',	'Chuyen vien',	2700.00,	NULL,	80);
INSERT INTO nhanvien VALUES ('089',	'Do Thi Huong',	'Nu',	'MAR-03-1965',	'Chuyen vien',	2900.00,	NULL,	90);
INSERT INTO nhanvien VALUES ('090',	'Nguyen Thanh Luong',	'Nam',	'NOV-08-1995',	'Chuyen vien',	1900.00,	NULL,	80);


CREATE TABLE ngoaingu (
	mann	VarChar2(2)	NOT NULL	PRIMARY KEY,
	tennn	VarChar2(15)
);

INSERT INTO ngoaingu VALUES ('01',	'Anh van');
INSERT INTO ngoaingu VALUES ('02',	'Phap van');
INSERT INTO ngoaingu VALUES ('03',	'Nga van');
INSERT INTO ngoaingu VALUES ('04',	'Trung van');
INSERT INTO ngoaingu VALUES ('05',	'Tieng Thai');
INSERT INTO ngoaingu VALUES ('06',	'Tieng Nhat');
INSERT INTO ngoaingu VALUES ('07',	'Tieng Han');
INSERT INTO ngoaingu VALUES ('08',	'Tieng Duc');
INSERT INTO ngoaingu VALUES ('09',	'Tieng Lao');
INSERT INTO ngoaingu VALUES ('10',	'Tieng Len');

CREATE TABLE tdonn (
	manv	 VarChar2(3)	NOT NULL  REFERENCES nhanvien(manv),
	mann	 VarChar2(2)	NOT NULL  REFERENCES ngoaingu(mann),
	trinhdo VarChar2(1)	 
);

INSERT INTO tdonn VALUES ('001',	'01',	'C');
INSERT INTO tdonn VALUES ('001',	'02',	'B');
INSERT INTO tdonn VALUES ('002',	'03',	'C');
INSERT INTO tdonn VALUES ('002',	'08',	'D');
INSERT INTO tdonn VALUES ('003',	'06',	'B');

INSERT INTO tdonn VALUES ('003',	'08',	'A');
INSERT INTO tdonn VALUES ('004',	'01',	'C');
INSERT INTO tdonn VALUES ('004',	'02',	'D');
INSERT INTO tdonn VALUES ('005',	'01',	'B');
INSERT INTO tdonn VALUES ('005',	'03',	'A');

INSERT INTO tdonn VALUES ('006',	'06',	'D');
INSERT INTO tdonn VALUES ('006',	'08',	'C');
INSERT INTO tdonn VALUES ('007',	'01',	'C');
INSERT INTO tdonn VALUES ('007',	'02',	'B');
INSERT INTO tdonn VALUES ('008',	'03',	'C');

INSERT INTO tdonn VALUES ('008',	'04',	'D');
INSERT INTO tdonn VALUES ('009',	'04',	'A');
INSERT INTO tdonn VALUES ('009',	'06',	'B');
INSERT INTO tdonn VALUES ('010',	'01',	'C');
INSERT INTO tdonn VALUES ('010',	'02',	'D');

INSERT INTO tdonn VALUES ('011',	'02',	'A');
INSERT INTO tdonn VALUES ('011',	'03',	'A');
INSERT INTO tdonn VALUES ('011',	'04',	'B');
INSERT INTO tdonn VALUES ('012',	'06',	'D');
INSERT INTO tdonn VALUES ('012',	'08',	'C');

INSERT INTO tdonn VALUES ('013',	'01',	'C');
INSERT INTO tdonn VALUES ('013',	'02',	'B');
INSERT INTO tdonn VALUES ('014',	'03',	'C');
INSERT INTO tdonn VALUES ('014',	'04',	'D');
INSERT INTO tdonn VALUES ('015',	'04',	'A');

INSERT INTO tdonn VALUES ('015',	'06',	'B');
INSERT INTO tdonn VALUES ('016',	'01',	'C');
INSERT INTO tdonn VALUES ('016',	'02',	'D');
INSERT INTO tdonn VALUES ('017',	'03',	'A');
INSERT INTO tdonn VALUES ('017',	'04',	'B');

INSERT INTO tdonn VALUES ('018',	'06',	'D');
INSERT INTO tdonn VALUES ('018',	'08',	'C');
INSERT INTO tdonn VALUES ('019',	'01',	'C');
INSERT INTO tdonn VALUES ('019',	'02',	'B');
INSERT INTO tdonn VALUES ('020',	'01',	'A');

INSERT INTO tdonn VALUES ('020',	'03',	'C');
INSERT INTO tdonn VALUES ('020',	'04',	'D');
INSERT INTO tdonn VALUES ('022',	'01',	'C');
INSERT INTO tdonn VALUES ('022',	'02',	'D');
INSERT INTO tdonn VALUES ('022',	'08',	'B');

INSERT INTO tdonn VALUES ('023',	'03',	'A');
INSERT INTO tdonn VALUES ('023',	'04',	'B');
INSERT INTO tdonn VALUES ('024',	'04',	'C');
INSERT INTO tdonn VALUES ('024',	'06',	'D');
INSERT INTO tdonn VALUES ('025',	'01',	'C');

INSERT INTO tdonn VALUES ('025',	'02',	'B');
INSERT INTO tdonn VALUES ('026',	'03',	'C');
INSERT INTO tdonn VALUES ('026',	'04',	'D');
INSERT INTO tdonn VALUES ('027',	'06',	'B');
INSERT INTO tdonn VALUES ('027',	'08',	'A');

INSERT INTO tdonn VALUES ('028',	'01',	'C');
INSERT INTO tdonn VALUES ('028',	'02',	'D');
INSERT INTO tdonn VALUES ('029',	'03',	'A');
INSERT INTO tdonn VALUES ('029',	'04',	'B');
INSERT INTO tdonn VALUES ('030',	'04',	'C');

INSERT INTO tdonn VALUES ('030',	'06',	'D');
INSERT INTO tdonn VALUES ('031',	'01',	'A');
INSERT INTO tdonn VALUES ('031',	'02',	'B');
INSERT INTO tdonn VALUES ('032',	'03',	'C');
INSERT INTO tdonn VALUES ('032',	'04',	'D');

INSERT INTO tdonn VALUES ('033',	'01',	'A');
INSERT INTO tdonn VALUES ('033',	'04',	'A');
INSERT INTO tdonn VALUES ('033',	'06',	'B');
INSERT INTO tdonn VALUES ('034',	'01',	'C');
INSERT INTO tdonn VALUES ('034',	'02',	'D');

INSERT INTO tdonn VALUES ('035',	'03',	'A');
INSERT INTO tdonn VALUES ('035',	'04',	'B');
INSERT INTO tdonn VALUES ('036',	'04',	'C');
INSERT INTO tdonn VALUES ('036',	'06',	'D');
INSERT INTO tdonn VALUES ('037',	'01',	'A');

INSERT INTO tdonn VALUES ('037',	'02',	'B');
INSERT INTO tdonn VALUES ('038',	'01',	'C');
INSERT INTO tdonn VALUES ('038',	'04',	'D');
INSERT INTO tdonn VALUES ('039',	'04',	'A');
INSERT INTO tdonn VALUES ('039',	'06',	'B');

INSERT INTO tdonn VALUES ('040',	'01',	'C');
INSERT INTO tdonn VALUES ('040',	'02',	'D');
INSERT INTO tdonn VALUES ('042',	'01',	'C');
INSERT INTO tdonn VALUES ('042',	'06',	'D');
INSERT INTO tdonn VALUES ('043',	'01',	'A');

INSERT INTO tdonn VALUES ('043',	'02',	'D');
INSERT INTO tdonn VALUES ('044',	'03',	'C');
INSERT INTO tdonn VALUES ('044',	'04',	'D');
INSERT INTO tdonn VALUES ('045',	'04',	'A');
INSERT INTO tdonn VALUES ('045',	'06',	'B');

INSERT INTO tdonn VALUES ('046',	'01',	'C');
INSERT INTO tdonn VALUES ('046',	'02',	'D');
INSERT INTO tdonn VALUES ('048',	'01',	'C');
INSERT INTO tdonn VALUES ('048',	'06',	'D');
INSERT INTO tdonn VALUES ('049',	'01',	'A');

INSERT INTO tdonn VALUES ('049',	'02',	'B');
INSERT INTO tdonn VALUES ('050',	'03',	'C');
INSERT INTO tdonn VALUES ('050',	'04',	'D');
INSERT INTO tdonn VALUES ('051',	'04',	'A');
INSERT INTO tdonn VALUES ('052',	'06',	'B');

INSERT INTO tdonn VALUES ('053',	'01',	'C');
INSERT INTO tdonn VALUES ('054',	'02',	'D');
INSERT INTO tdonn VALUES ('055',	'03',	'A');
INSERT INTO tdonn VALUES ('056',	'04',	'B');
INSERT INTO tdonn VALUES ('057',	'01',	'C');

INSERT INTO tdonn VALUES ('058',	'06',	'D');
INSERT INTO tdonn VALUES ('059',	'01',	'A');
INSERT INTO tdonn VALUES ('060',	'02',	'B');
INSERT INTO tdonn VALUES ('061',	'01',	'C');
INSERT INTO tdonn VALUES ('062',	'04',	'D');

INSERT INTO tdonn VALUES ('063',	'04',	'A');
INSERT INTO tdonn VALUES ('064',	'06',	'B');
INSERT INTO tdonn VALUES ('065',	'01',	'C');
INSERT INTO tdonn VALUES ('066',	'02',	'D');
INSERT INTO tdonn VALUES ('067',	'03',	'A');

INSERT INTO tdonn VALUES ('068',	'04',	'B');
INSERT INTO tdonn VALUES ('069',	'04',	'C');
INSERT INTO tdonn VALUES ('070',	'06',	'D');
INSERT INTO tdonn VALUES ('071',	'01',	'A');
INSERT INTO tdonn VALUES ('072',	'02',	'B');

INSERT INTO tdonn VALUES ('073',	'03',	'C');
INSERT INTO tdonn VALUES ('074',	'04',	'D');
INSERT INTO tdonn VALUES ('075',	'04',	'A');
INSERT INTO tdonn VALUES ('076',	'06',	'B');
INSERT INTO tdonn VALUES ('077',	'01',	'C');
INSERT INTO tdonn VALUES ('078',	'02',	'D');
INSERT INTO tdonn VALUES ('079',	'03',	'A');
INSERT INTO tdonn VALUES ('080',	'01',	'C');
INSERT INTO tdonn VALUES ('083',	'01',	'C');
INSERT INTO tdonn VALUES ('083',	'03',	'B');
INSERT INTO tdonn VALUES ('084',	'01',	'A');
INSERT INTO tdonn VALUES ('087',	'01',	'A');
INSERT INTO tdonn VALUES ('087',	'03',	'A');
INSERT INTO tdonn VALUES ('090',	'02',	'B');
INSERT INTO tdonn VALUES ('090',	'03',	'B');


