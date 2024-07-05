DROP TABLE thamgia;
DROP TABLE thietke;
DROP TABLE congtrinh;
DROP TABLE chunhan;
DROP TABLE chuthau;
DROP TABLE congnhan;
DROP TABLE kientrucsu;

CREATE TABLE chunhan(
	msch	VARCHAR2(3)	NOT NULL PRIMARY KEY,
	tenchu	VARCHAR2(30),
	diachichu	VARCHAR2(30),
	phai	VARCHAR2(3)
);

INSERT INTO chunhan VALUES ('001',	'Huynh Huu Tran',	'54 Xo Viet Nghe Tinh',	'Nam');
INSERT INTO chunhan VALUES ('002',	'Nguyen Chi Thinh',	'101 Hai Ba Trung',		'Nam');
INSERT INTO chunhan VALUES ('003',	'Le Hong Vu',		'29 Hai Ba Trung',	'Nam');
INSERT INTO chunhan VALUES ('004',	'Nguyen Thanh Ky',	'56 Vo Thi Sau',		'Nam');
INSERT INTO chunhan VALUES ('005',	'Nguyen Thi Phuong','29 Phan Dinh Phung',	'Nu');
INSERT INTO chunhan VALUES ('006',	'Nguyen Thanh Ha',	'45 De Tham',			'Nu');
INSERT INTO chunhan VALUES ('007',	'Phan Thanh Liem',	'150 Huynh Thuc Khang',	'Nam');
INSERT INTO chunhan VALUES ('008',	'Nguyen Cong Thao',	'10 Hai Ba Trung',		'Nam');
INSERT INTO chunhan VALUES ('009',	'Huynh Huu Truc',	'85 Mau Than',			'Nam');
INSERT INTO chunhan VALUES ('010',	'Huynh Huu Tam',	'45 Nguyen Trai',		'Nam');
INSERT INTO chunhan VALUES ('011',	'Nguyen Ngoc Long',	'20 Ly Thuong Kiet',	'Nam');
INSERT INTO chunhan VALUES ('012',	'Vo Thi Tu',		'30 Tran Hung Dao',		'Nu');
INSERT INTO chunhan VALUES ('013',	'Tran Thi Ngoc',	'100 Chau Van Liem',	'Nu');
INSERT INTO chunhan VALUES ('014',	'Vo Thanh Tung',	'130 Dinh Cong Trang',	'Nam');
INSERT INTO chunhan VALUES ('015',	'Le Thanh Phuong',	'55 Tran Phu',			'Nam');

CREATE TABLE chuthau(
    msct    VARCHAR2(3) NOT NULL PRIMARY KEY,
    tenthau  VARCHAR2(30),
    dienthoai   VARCHAR2(11),
    diachithau  VARCHAR2(30)
);

INSERT INTO chuthau VALUES ('001',	'Hong Xuan Truong',	    '09135674565',	'5 Phan Chu Trinh');
INSERT INTO chuthau VALUES ('002',	'Hoang Cong Binh',	    '09132064812',	'2 Le Van Sy');
INSERT INTO chuthau VALUES ('003',	'Le Van Son',	        '09170283740',	'12 Tran Nhan Ton');
INSERT INTO chuthau VALUES ('004',	'Tran Khai Hoan',	    '09186584326',	'20 Nguyen Thai Hoc');
INSERT INTO chuthau VALUES ('005',	'Nguyen Ky Lap',	    '09191515154',	'115 Nguyen Cong Tru');
INSERT INTO chuthau VALUES ('006',	'Huynh Thanh Tri',	    '09812020203',	'20 Phan Boi Chau');
INSERT INTO chuthau VALUES ('007',	'Huynh Thanh Tinh',	    '09822323235',	'23 Vo Thi Sau');
INSERT INTO chuthau VALUES ('008',	'Le Van Mai',	        '09835151518',	'50 Tran Hoang Na');
INSERT INTO chuthau VALUES ('009',	'Nguyen Truong Giang',	'09840101017',	'29 Cao Thang');
INSERT INTO chuthau VALUES ('010',	'Nguyen Bao Ngoc',	    '09857070707',	'33 Dinh Cong Trang');
INSERT INTO chuthau VALUES ('011',	'Le Tri Dung',	        '09861458962',	'112 Nguyen Hue');
INSERT INTO chuthau VALUES ('012',	'Tran Van Chin',	    '09873598425',	'27 Tam Vu');
INSERT INTO chuthau VALUES ('013',	'Tran Cong Minh',	    '09883366552',	'78 Nguyen Trai');
INSERT INTO chuthau VALUES ('014',	'Nguyen Cong Khe',	    '09891122334',	'456 Tran Hoang Na');
INSERT INTO chuthau VALUES ('015',	'Le Van Luu',	        '09824568521',	'100 Nguyen Viet Hong');

CREATE TABLE congnhan(
    mscn    VARCHAR2(3) NOT NULL PRIMARY KEY,
    hotencn VARCHAR2(30),
    ngaysinh    DATE,
    phai    VARCHAR2(3),
    chuyenmon   VARCHAR2(10)
);

INSERT INTO congnhan VALUES ('001',	'Nguyen Thi Suu',		'OCT-30-1940',	'Nu',	'ho');
INSERT INTO congnhan VALUES ('002',	'Vi Chi A',				'MAY-21-1975',	'Nu',	'han');
INSERT INTO congnhan VALUES ('003',	'Le Manh Quoc',			'MAR-13-1955',	'Nam',	'moc');
INSERT INTO congnhan VALUES ('004',	'Vo Van Chin',			'APR-25-1957',	'Nam',	'son');
INSERT INTO congnhan VALUES ('005',	'Le Quyet Thang',		'SEP-09-1956',	'Nam',	'son');
INSERT INTO congnhan VALUES ('006',	'Nguyen Hong Van',		'MAY-10-1960',	'Nam',	'dien');
INSERT INTO congnhan VALUES ('007',	'Dang Van Son',			'JUL-03-1950',	'Nam',	'dien');
INSERT INTO congnhan VALUES ('008',	'Tran Van Tam',			'NOV-10-1960',	'Nam',	'moc');
INSERT INTO congnhan VALUES ('009',	'Phan Tan Tai',			'AUG-28-1970',	'Nam',	'ho');
INSERT INTO congnhan VALUES ('010',	'Nguyen Minh Khiem',	'JUN-14-1980',	'Nam',	'han');
INSERT INTO congnhan VALUES ('011',	'Phan Phuong Lan',		'MAY=28-1990',	'Nu',	'moc');
INSERT INTO congnhan VALUES ('012',	'Bui Minh Quan',		'JUN-08-1988',	'Nam',	'son');
INSERT INTO congnhan VALUES ('013',	'Nguyen Minh Trung',	'FEB-27-1978',	'Nam',	'son');
INSERT INTO congnhan VALUES ('014',	'Le Phuong Dung',		'JUN-10-1990',	'Nu',	'dien');
INSERT INTO congnhan VALUES ('015',	'Nguyen Thanh Tuan',	'FEB-04-1993',	'Nam',	'dien');

CREATE TABLE congtrinh(
    sttct   VARCHAR2(3)  NOT NULL PRIMARY KEY,
    tenct   VARCHAR2(30),
    diachict    VARCHAR2(30),
    tinhthanh   VARCHAR2(15),
    kinhphi NUMBER(8,2),
    msch    VARCHAR2(3) NOT NULL REFERENCES chunhan(msch),
    msct    VARCHAR2(3) NOT NULL REFERENCES chuthau(msct),
    ngaybd  DATE
);

INSERT INTO congtrinh VALUES ('001',	'Khach san Quoc Te',	    '5 Nguyen An Ninh',	    'TPCT',	        450,	'001',	'001',	'MAY-08-1994');
INSERT INTO congtrinh VALUES ('002',	'Cong Vien Thieu Nhi',	    '100 Nguyen Thai Hoc',	'TPCT',	        200,	'002',	'001',	'MAY-10-1994');
INSERT INTO congtrinh VALUES ('003',	'Hoi cho nong nghiep',	    '33 Le Loi',	        'Vinh Long',	1000,	'003',	'002',	'JUN-10-1994');
INSERT INTO congtrinh VALUES ('004',	'Truong mau giao Mang Non',	'48 Tan Trao',	        'TPCT',	        300,	'003',	'003',	'JUN-03-1994');
INSERT INTO congtrinh VALUES ('005',	'Cau lac bo huu tri',	    '28 Mau Than',	        'TPCT',	        3000,	'004',	'003',	'AUG-08-1994');
INSERT INTO congtrinh VALUES ('006',	'Van Phong BITIS',	        '25 Phan Dinh Phung',	'Ha Noi',	    4000,	'005',	'003',	'SEP-09-1994');
INSERT INTO congtrinh VALUES ('007',	'Trung Tam Ngoai Ngu',	    '124 Nguyen Trai',	    'TP HCM',	    650,	'006',	'002',	'OCT-09-1994');
INSERT INTO congtrinh VALUES ('008',	'Nha hang Sao Mai',	        '76 Chau Van Liem',	    'Ha Noi',	    100,	'007',	'004',	'NOV-10-1994');
INSERT INTO congtrinh VALUES ('009',	'Khoa CNTT va TT',	        '01 Ly Tu Trong',       'TPCT',	        3100,	'005',	'002',	'DEC-12-1994');
INSERT INTO congtrinh VALUES ('010',	'Khach san Muong Thanh',	'5 Nguyen An Ninh',	    'Vinh Long',	450,	'007',	'003',	'DEC-25-1994');
INSERT INTO congtrinh VALUES ('011',	'Nha hat Tay Do',	        '12 Tran Huynh',	    'Bac Lieu',	    2800,	'010',	'001',	'NOV-05-2015');
INSERT INTO congtrinh VALUES ('012',	'Truong CDCD',	            '47 Tran Phu',	        'Ca Mau',    	2000,	'003',  '009',	'JUN-10-2015');
INSERT INTO congtrinh VALUES ('013',	'Trung Tam GDTX',	        '250 Nguyen Trung Truc','Kien Giang',	1000,	'009',	'007',	'SEP-20-2016');
INSERT INTO congtrinh VALUES ('014',	'Khach san Bac Lieu',	    '1 Hung Vuong',	        'Bac Lieu',	    1200,	'006',	'007',	'FEB-20-2016');
INSERT INTO congtrinh VALUES ('015',	'Nha nghi Cong Doan',	    '100 Nguyen Hue',	    'TPCT',     	2800,	'008',	'010',	'MAR-27-2017');
INSERT INTO congtrinh VALUES ('016',	'Nha thi dau Da Nang',	    '10 Nguyen Cong Tru',	'Vinh Long',	4000,	'007',	'009',	'OCT-10-2016');
INSERT INTO congtrinh VALUES ('017',	'Khach san An Huy',	        '125 Dong Khoi',	    'TPCT',	        3000,	'004',	'005',	'AUG-12-2015');
INSERT INTO congtrinh VALUES ('018',	'Truong mau giao Than Dong','26 Tran Hoang Na',	    'Kien Giang',	450,	'011',	'011',	'MAR-01-2018');
INSERT INTO congtrinh VALUES ('019',	'Van phong Viettel',	    '100 Hoa Binh',	        'Bac Lieu',	    5100,	'008',	'010',	'APR-01-2018');
INSERT INTO congtrinh VALUES ('020',	'So TTTT',	                '78 Hoang Quoc Viet',	'TPCT',	        4000,	'003',	'012',	'OCT-15-2017');

CREATE TABLE kientrucsu(
    mskts   VARCHAR2(3) NOT NULL    PRIMARY KEY,
    hotenkts    VARCHAR2(30),
    ngaysinh    DATE,
    phai    VARCHAR2(3),
    noitn   VARCHAR2(15),
    diachikts   VARCHAR(30)
);

INSERT INTO kientrucsu VALUES ('001',	'Le Thanh Tung',	    'MAY-11-1975',	'Nam','TP HCM',	'25 Hung Vuong- TP Bien Hoa');
INSERT INTO kientrucsu VALUES ('002',	'Le Kim Dung',	        'JUL-07-1982',	'Nu','Ha Noi',	'18 Phan Van Tri- TP Can Tho');
INSERT INTO kientrucsu VALUES ('003',	'Nguyen Anh Thu',	    'SEP-25-1988',	'Nu','Hoa Ky',	'10 Tran Hung Dao- An Giang');
INSERT INTO kientrucsu VALUES ('004',	'Nguyen Song Do Quyen',	'MAY-25-1970',	'Nu','TP HCM',	'73 Tran Hung Dao- TP HCM');
INSERT INTO kientrucsu VALUES ('005',	'Truong Minh Thai',	    'MAY-24-1990',	'Nam','Phap',	'12 Tran Phu- Ha Noi');
INSERT INTO kientrucsu VALUES ('006',	'Tran Van Hung',	    'OCT-28-1965',	'Nam','DHCT',	'01 Dinh Cong Trang- TP Can Tho');
INSERT INTO kientrucsu VALUES ('007',	'Nguyen Van Kien',	    'JUN-04-1978',	'Nam','TP HCM',	'16 Nguyen Trai- Hau Giang');
INSERT INTO kientrucsu VALUES ('008',	'Le Thi Truc',	        'AUG-02-1973',	'Nu','DHCT',	'115 Nguyen Hue- Vinh long');
INSERT INTO kientrucsu VALUES ('009',	'Nguyen Van Su',	    'DEC-20-1980',	'Nam','Ha Noi',	'23 Ly Thai To- Vinh Long');
INSERT INTO kientrucsu VALUES ('010',	'Tran Thanh Cao',	    'MAY-15-1978',	'Nam','DHCT',	'14 Tran Phu- TPCT');

CREATE TABLE thamgia (
    mscn    VARCHAR2(3) NOT NULL REFERENCES congnhan(mscn),
    sttct   VARCHAR2(3) NOT NULL REFERENCES congtrinh(sttct),
    ngaytg  DATE,
    songay  NUMBER
);

INSERT INTO thamgia VALUES('001',	'001',	'MAY-08-1994',	20);
INSERT INTO thamgia VALUES('001',	'004',	'SEP-09-1994',	20);
INSERT INTO thamgia VALUES('001',	'014',	'FEB-20-2016',	8);
INSERT INTO thamgia VALUES('003',	'001',	'DEC-18-1994',	6);
INSERT INTO thamgia VALUES('004',	'002',	'MAY-10-1994',	10);
INSERT INTO thamgia VALUES('004',	'003',	'JUN-10-1994',	10);
INSERT INTO thamgia VALUES('004',	'001',	'OCT-01-1994',	8);
INSERT INTO thamgia VALUES('004',	'004',	'JUL-03-1994',	7);
INSERT INTO thamgia VALUES('004',	'005',	'AUG-08-1994',	7);
INSERT INTO thamgia VALUES('004',	'006',	'SEP-09-1994',	7);
INSERT INTO thamgia VALUES('004',	'007',	'OCT-09-1994',	7);
INSERT INTO thamgia VALUES('004',	'008',	'NOV-10-1994',	5);
INSERT INTO thamgia VALUES('004',	'009',	'DEC-12-1994',	10);
INSERT INTO thamgia VALUES('004',	'010',	'DEC-25-1994',	5);
INSERT INTO thamgia VALUES('004',	'011',	'NOV-05-2015',	8);
INSERT INTO thamgia VALUES('004',	'012',	'JUL-10-2015',	12);
INSERT INTO thamgia VALUES('004',	'013',	'SEP-20-2016',	5);
INSERT INTO thamgia VALUES('004',	'014',	'FEB-25-2016',	10);
INSERT INTO thamgia VALUES('004',	'015',	'MAR-27-2017',	6);
INSERT INTO thamgia VALUES('005',	'015',	'MAY-20-2017',	6);
INSERT INTO thamgia VALUES('005',	'002',	'MAY-12-1994',	5);
INSERT INTO thamgia VALUES('006',	'001',	'DEC-15-1994',	5);
INSERT INTO thamgia VALUES('006',	'004',	'SEP-14-1994',	7);
INSERT INTO thamgia VALUES('007',	'003',	'JUN-10-1994',	18);
INSERT INTO thamgia VALUES('008',	'001',	'DEC-16-1994',	7);
INSERT INTO thamgia VALUES('009',	'005',	'OCT-10-2000',	12);
INSERT INTO thamgia VALUES('011',	'003',	'JUL-01-1994',	10);
INSERT INTO thamgia VALUES('012',	'006',	'FEB-18-1995',	4);
INSERT INTO thamgia VALUES('013',	'007',	'DEC-01-1995',	9);
INSERT INTO thamgia VALUES('015',	'002',	'OCT-25-1995',	5);
INSERT INTO thamgia VALUES('004',	'016',	'OCT-10-2016',	7);
INSERT INTO thamgia VALUES('004',	'017',	'AUG-12-2015',	10);

CREATE TABLE thietke(
  mskts VARCHAR2(3) NOT NULL  REFERENCES kientrucsu(mskts),
  sttct VARCHAR2(3) NOT NULL  REFERENCES  congtrinh(sttct),
  thulao  NUMBER(8,2)
);

INSERT INTO thietke VALUES ('001',	'001',	25);
INSERT INTO thietke VALUES ('001',	'007',	10);
INSERT INTO thietke VALUES ('001',	'004',	25);
INSERT INTO thietke VALUES ('001',	'003',	20);
INSERT INTO thietke VALUES ('002',	'015',	12);
INSERT INTO thietke VALUES ('002',	'004',	20);
INSERT INTO thietke VALUES ('002',	'005',	30);
INSERT INTO thietke VALUES ('002',	'006',	40);
INSERT INTO thietke VALUES ('003',	'003',	12);
INSERT INTO thietke VALUES ('004',	'002',	6);
INSERT INTO thietke VALUES ('005',	'001',	12);
INSERT INTO thietke VALUES ('005',	'006',	27);
INSERT INTO thietke VALUES ('005',	'008',	18);
INSERT INTO thietke VALUES ('006',	'010',	15);
INSERT INTO thietke VALUES ('007',	'012',	20);
INSERT INTO thietke VALUES ('007',	'011',	15);
INSERT INTO thietke VALUES ('008',	'014',	13);
INSERT INTO thietke VALUES ('010',	'015',	21);


