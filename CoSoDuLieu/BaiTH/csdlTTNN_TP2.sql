create table KHOAHOC (
   MAKH                 char(4)              not null,
   TENKH                varchar(50)           not null,
   NGAYBD               date            not null,
   NGAYKT               date            not null ,
   constraint PK_KHOAHOC primary key  (MAKH),
   constraint CK_KHOAHOC  CHECK (NGAYKT>NGAYBD)
);


create table CHUONGTRINH (
   MACT                 char(5)              PRIMARY KEY,
   TENCT                varchar(100)          not null
);

create table LOAILOP (
   MALOAI               char(5)              not null  primary key,
   MACT                 char(5)              not null,
   TENLOAI              varchar(100)          not null,
   constraint FK_LOAILOP FOREIGN  key  (MACT) REFERENCES CHUONGTRINH(MACT)
);

create table LOP (
   MALOP                char(4)              not null PRIMARY KEY,
   MALOAI               char(5)              not null,
   TENLOP               varchar(50)          not null,
   SISO                 smallint             not null CHECK (SISO>12),
   MAKH   char(4)              not null,
   constraint FK1_LOP FOREIGN  key  (MALOAI) REFERENCES LOAILOP(MALOAI),
   constraint FK2_LOP FOREIGN  key  (MAKH) REFERENCES KHOAHOC(MAKH)
   
);

create table HOCVIEN (
   MAHV                 char(6)				primary key,
   TENHV                varchar(40)          not null,
   GIOITINH             smallint                  not null,
   NGAYSINH             date            not null,
   SDT                  char(10)                  not null,
   DIACHI               varchar(100)         not null
);

create table PHIEUTHU (
   SOPT                 CHAR(8)               PRIMARY KEY,
   MAHV                char(6)               not null,
   MALOP                char(4)              not null,
   NGAYLAPPHIEU         date	            not null,
   THANHTIEN        NUMERIC NOT NULL,
   constraint FK1_PT FOREIGN  key  (MAHV) REFERENCES HOCVIEN(MAHV),
   constraint FK2_PT FOREIGN  key  (MALOP) REFERENCES LOP(MALOP)
);

create table MONHOC (
   MAMH                 char(4)             PRIMARY KEY,
   TENMH                varchar(30)          not null
);



create table DIEM (
   MAMH                 char(4)              not null,
   MAHV                 char(6)                 not null,
   MALOP                char(4)              not null,
   DIEM                 float            not null CHECK(DIEM>=0),
   constraint PK_DIEM primary key  (MAMH, MAHV, MALOP),
    constraint FK1_DIEM FOREIGN  key  (MAHV) REFERENCES HOCVIEN(MAHV),
   constraint FK2_DIEM FOREIGN  key  (MALOP) REFERENCES LOP(MALOP),
   constraint FK3_DIEM FOREIGN  key  (MAMH) REFERENCES MONHOC(MAMH)
);


INSERT INTO KHOAHOC VALUES('K001','Khóa 1','2020-01-10','2020-03-20');
INSERT INTO KHOAHOC VALUES('K002','Khóa 2','2020-02-28','2020-05-28');
INSERT INTO KHOAHOC VALUES('K003','Khóa 3','2020-04-10','2020-07-20');
INSERT INTO KHOAHOC VALUES('K004','Khóa 4','2020-06-15','2020-09-20');


INSERT INTO CHUONGTRINH VALUES('CT001','Tiếng Anh Tổng Quát');
INSERT INTO CHUONGTRINH VALUES('CT002','Tiếng Anh Trẻ Em');
INSERT INTO CHUONGTRINH VALUES('CT003','Tiếng Anh Luyện Kỹ Năng');
INSERT INTO CHUONGTRINH VALUES('CT004','Chương Trình TOEIC');
INSERT INTO CHUONGTRINH VALUES('CT005','Tiếng Anh IELTS');
INSERT INTO CHUONGTRINH VALUES('CT006','Chương Trình CamBridge');
INSERT INTO CHUONGTRINH VALUES('CT007','Chứng Chỉ Tiếng Anh 6 Bậc(A1,B1,B2,C1)');



INSERT INTO LOAILOP VALUES('LL001','CT001','Tiếng Anh căn bản');
INSERT INTO LOAILOP VALUES('LL002','CT001','Tiếng Anh A1');
INSERT INTO LOAILOP VALUES('LL003','CT001','Tiếng Anh A2');
INSERT INTO LOAILOP VALUES('LL004','CT001','Tiếng Anh B1');
INSERT INTO LOAILOP VALUES('LL005','CT001','Tiếng Anh B2');
INSERT INTO LOAILOP VALUES('LL006','CT001','Tiếng Anh C1');
INSERT INTO LOAILOP VALUES('LL007','CT001','Tiếng Anh C2');
INSERT INTO LOAILOP VALUES('LL008','CT001','Tiếng Anh nâng cao');
--
INSERT INTO LOAILOP VALUES('LL009','CT002','Anh văn nhi đồng');
INSERT INTO LOAILOP VALUES('LL010','CT002','Anh văn thiếu nhi');
INSERT INTO LOAILOP VALUES('LL011','CT002','Anh văn thiếu niên');
INSERT INTO LOAILOP VALUES('LL012','CT002','Tiếng Anh tổng quát dành cho thiếu niên(B1)');
INSERT INTO LOAILOP VALUES('LL013','CT002','Tiếng Anh tổng quát dành cho thiếu niên(B1+)');
INSERT INTO LOAILOP VALUES('LL014','CT002','Tiếng Anh nâng cao');
INSERT INTO LOAILOP VALUES('LL015','CT002','IELTS');
--

INSERT INTO LOP VALUES ('L001','LL001','Lớp 1','30','K001');
INSERT INTO LOP VALUES ('L002','LL001','Lớp 2','30','K001');
INSERT INTO LOP VALUES ('L003','LL002','Lớp 1','25','K001');





INSERT INTO HOCVIEN VALUES('HV0001','Đỗ Bình An',1,'2000-11-02','0917217036','Cờ Đỏ - Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0002','Đỗ Gia Bảo',1,'2001-12-02','0917217036','Ôn Môn- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0003','Đỗ Phúc Vinh',1,'2002-11-02','0917217036','Cù Lao Dung - Sóc Trăng');
INSERT INTO HOCVIEN VALUES('HV0004','Thạch Chí Tâm',1,'2000-01-02','0917217036','Châu Thành- An Giang');


INSERT INTO HOCVIEN VALUES('HV0005','Lê Cẩm Giao','0',to_date('2000-11-05','yyyy-mm-dd'),'0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0006','Huỳnh Gia Bảo','1',to_date('2000-11-02','yyyy-mm-dd'),'0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0007','Đỗ An Nhiên','0',to_date('2001-01-02','yyyy-mm-dd'),'0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0008','Trần Hoàng Uyên Anh',0,'2002-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0009','Trấn Thành',1,'1998-07-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0010','Trịnh Giai Nhân',1,'2000-11-02','0917217036','Châu Thành- An Giang');
INSERT INTO HOCVIEN VALUES('HV0011','Lê Thanh Hoàng',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0014','Lê Thanh Tâm',1,'2002-01-17','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0015','Huỳnh Ngọc Minh',1,'2007-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0016','Ngũ Hoàng Gia Bảo',1,'2005-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0017','Trịnh Ngọc Gia Bảo',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0018','Bùi Bảo Ngọc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0019','Lê Ngọc Kim Khánh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0020','Lê Huỳnh My',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0021','Trần Ngọc Tuyết',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0022','Trần Ngọc Khánh Minh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0023','Trần Ngọc Minh Anh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0024','Trần Lê Kim Ngân',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0025','Lê Thanh Trân',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0026','Lê Thanh Tâm',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0027','Trần Ngọc Tuyền',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0028','Trần Huỳnh Gia Nhi',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0029','Trần Lê Kim Thoa',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0030','Bùi Mộng Cầm',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0031','Trần Mộng Điệp',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0032','Trần Kim Quyên',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0033','Trần Lê Anh Thư',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0034','Trần Thanh Nghi',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0035','Trần Bùi Tố Nga',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0036','Trần Thị Kim Cúc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0037','Trần Bảo Thy',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0038','Nguyễn Thị Bảo Nghi',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0039','Lê Thanh Ngọc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0040','Trần Thị Như Ý',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0041','Trần Ngọc Mỹ Ý',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0042','Trần Ngọc Phúc An',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0043','Trần Ngọc Minh Anh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0044','Trần Ngọc Phúc An',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0047','Trần Ngọc Bích',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0048','Trần Thanh Nhân',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0049','Đỗ Tố Uyên',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0050','Lê Hà My',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0051','Lê Ngọc Trân',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0052','Nguyễn Minh Thi',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0053','Trần Ngọc Anh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0054','Trần Ngọc Khánh Như',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0055','Trần Ngọc Tiên',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0056','Trần Kiều Tiên',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0057','Trần Hữu Phước',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0058','Trần Hoàng Khang',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0059','Trần Lâm Trường',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0060','Trần Trọng Phúc',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');

INSERT INTO HOCVIEN VALUES('HV0061','Trần Trọng Nghĩa',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0062','Trần Minh Nhựt',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0063','Lê Thanh An',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0064','Lê Kim Thy',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0065','Trần Huyền Trang',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0066','Trần Minh Thư',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0067','Trần Thanh Ngân',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0068','Nguyễn Quốc Kiệt',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0069','Lâm Thị Như',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0070','Lâm Minh Thư',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0071','Đỗ Ngọc Như',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0072','Trần Trọng Phúc',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0073','Nguyễn Thanh Như',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0074','Lư Huyền Trang',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
--
INSERT INTO HOCVIEN VALUES('HV0075','Lư Anh Thư',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0076','Đỗ Hà My',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0077','Đỗ Minh Khang',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0078','Đỗ Hoàng Khang',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0079','Đỗ Gia Khang',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0080','Đỗ Bùi Minh Anh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0081','Lê Tuấn Anh',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0082','Đỗ Diễm Ly',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0083','Đỗ Tường Vy',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0084','Đỗ Ngọc Chúc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0085','Đỗ Minh Nhựt',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0086','Đỗ Minh Hoàng',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0087','Đỗ Minh Trung',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0088','Đỗ Minh Long',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0089','Võ Văn Khánh Quốc',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0090','Nguyễn Trung Hậu',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0091','Đỗ Lam Nhã',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0092','Huỳnh Minh Sơn',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0093','Hà Duy Mạnh',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0094','Lưu Hà Phước',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0095','Đỗ Ngọc Kiều Oanh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0096','Đỗ Gia Minh',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0097','Đỗ Thanh Nhi',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0098','Lê Tấn Đạt',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0099','Lê Kim Ánh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0100','Đỗ Phương Thùy',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0101','Lâm Thị Thảo Linh',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0102','Đỗ Thanh Thảo',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0103','Đỗ Ngọc Thùy',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0104','Đỗ Ngọc Phương',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0105','Đỗ Thạch Anh',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0106','Lư Tấn Anh',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0107','Đỗ Hà Giang',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');

INSERT INTO HOCVIEN VALUES('HV0108','Đỗ Trường Giang',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0109','Đỗ Hà My',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0110','Đỗ Tuấn Phát',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0111','Đỗ Tuấn Kiệt',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
---
INSERT INTO HOCVIEN VALUES('HV0112','Đỗ Hà Huy',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0113','Đỗ Hà Ngọc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0114','Đỗ Thị Cẩm Giang',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0115','Lê Bảo Trang',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0116','Lê Kiều My',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0117','Phạm Thanh Trúc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0118','Phạm Ngọc Hà',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0119','Trương Thanh Ngọc',0,'2000-11-02','0917217036','Phong Điền- Cần Thơ');
INSERT INTO HOCVIEN VALUES('HV0120','Đỗ Phạm Gia Huy',1,'2000-11-02','0917217036','Phong Điền- Cần Thơ');










insert into PHIEUTHU values('PT000002','HV0002','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000003','HV0003','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000004','HV0004','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000005','HV0005','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000006','HV0006','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000007','HV0007','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000008','HV0008','L001','2021-06-01',1350000);
insert into PHIEUTHU values('PT000009','HV0009','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000010','HV0010','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000011','HV0011','L001','2021-06-02',1350000);
-- insert into PHIEUTHU values('PT000012','HV0012','L001','2021-06-02',1350000);
-- insert into PHIEUTHU values('PT000013','HV0013','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000014','HV0014','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000015','HV0015','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000016','HV0016','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000017','HV0017','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000018','HV0018','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000019','HV0019','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000020','HV0020','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000021','HV0021','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000022','HV0022','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000023','HV0023','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000024','HV0024','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000025','HV0025','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000026','HV0026','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000027','HV0027','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000028','HV0028','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000029','HV0029','L001','2021-06-02',1350000);
insert into PHIEUTHU values('PT000030','HV0030','L001','2021-06-02',1350000);

insert into PHIEUTHU values('PT000031','HV0031','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000032','HV0032','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000033','HV0033','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000034','HV0034','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000035','HV0035','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000036','HV0036','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000037','HV0037','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000038','HV0038','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000039','HV0039','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000040','HV0040','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000041','HV0041','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000042','HV0042','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000043','HV0043','L003','2021-06-02',1450000);
insert into PHIEUTHU values('PT000044','HV0108','L003','2021-06-05',1450000);
insert into PHIEUTHU values('PT000045','HV0109','L003','2021-06-05',1450000);
insert into PHIEUTHU values('PT000046','HV0110','L003','2021-06-05',1450000);
insert into PHIEUTHU values('PT000047','HV0111','L003','2021-06-05',1450000);
insert into PHIEUTHU values('PT000070','HV0044','L003','2021-06-05',1450000);





INSERT INTO MONHOC(MAMH,TENMH) VALUES ('MH01','Nghe');
INSERT INTO MONHOC(MAMH,TENMH) VALUES ('MH02','Nói');
INSERT INTO MONHOC(MAMH,TENMH) VALUES ('MH03','Đọc');
INSERT INTO MONHOC(MAMH,TENMH) VALUES ('MH04','Viết');


INSERT INTO DIEM values  ('MH01','HV0002', 'L001', 5.5);
INSERT INTO DIEM values  ('MH02','HV0002', 'L001', 6.5);
INSERT INTO DIEM values  ('MH03','HV0002', 'L001', 8.5);
INSERT INTO DIEM values  ('MH04','HV0002', 'L001', 3.5);

INSERT INTO DIEM values  ('MH01','HV0003', 'L001', 5.25);
INSERT INTO DIEM values  ('MH02','HV0003', 'L001', 6.8);
INSERT INTO DIEM values  ('MH03','HV0003', 'L001', 7.5);
INSERT INTO DIEM values  ('MH04','HV0003', 'L001', 5.5);

INSERT INTO DIEM values  ('MH01','HV0004', 'L001', 7.5);
INSERT INTO DIEM values  ('MH02','HV0004', 'L001', 6.5);
INSERT INTO DIEM values  ('MH03','HV0004', 'L001', 7.5);
INSERT INTO DIEM values  ('MH04','HV0004', 'L001', 5.0);

INSERT INTO DIEM values  ('MH01','HV0005', 'L001', 7.5);
INSERT INTO DIEM values  ('MH02','HV0005', 'L001', 8.0);
INSERT INTO DIEM values  ('MH03','HV0005', 'L001', 8.0);
INSERT INTO DIEM values  ('MH04','HV0005', 'L001', 7.75);

INSERT INTO DIEM values  ('MH01','HV0006', 'L001', 5.5);
INSERT INTO DIEM values  ('MH02','HV0006', 'L001', 6.5);
INSERT INTO DIEM values  ('MH03','HV0006', 'L001', 4.5);
INSERT INTO DIEM values  ('MH04','HV0006', 'L001', 3.5);

