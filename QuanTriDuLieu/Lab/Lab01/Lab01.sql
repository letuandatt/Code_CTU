-- CREATE DATABASE QLDIEM;

USE QLDIEM;

-- CREATE TABLE khoa (
--     maKhoa CHAR(8),
--     tenKhoa VARCHAR(50),
--     PRIMARY KEY (maKhoa)
-- );

-- CREATE TABLE sinhVien (
--     mssv CHAR(8),
--     hoten VARCHAR(45),
--     GT CHAR(1),
--     ngaySinh DATE, 
--     noiSinh VARCHAR(40),
--     diaChi VARCHAR(100),
--     maKhoa CHAR(8),
--     PRIMARY KEY (mssv),
--     FOREIGN KEY (maKhoa) REFERENCES khoa(maKhoa)
-- );

-- CREATE TABLE hocPhan (
--     maHP CHAR(6),
--     tenHP VARCHAR(50),
--     soTinChi INT UNSIGNED, 
--     soTietLT INT UNSIGNED,
--     soTietTH INT UNSIGNED,
--     maKhoa CHAR(8),
--     PRIMARY KEY (maHP),
--     FOREIGN KEY (maKhoa) REFERENCES khoa(maKhoa)
-- );

-- CREATE TABLE ketQua (
--     mssv CHAR(8),
--     maHP CHAR(6),
--     diem FLOAT,
--     FOREIGN KEY (mssv) REFERENCES sinhVien(mssv),
--     FOREIGN KEY (maHP) REFERENCES hocPhan(maHP)
-- );

-- INSERT INTO hocPhan (maHP, tenHP, soTinChi, soTietLT, soTietTH, maKhoa) 
-- VALUES 
-- ('CT101', 'Lập trình căn bản', 4, 30, 60, 'CNTT&TT'), 
-- ('CT176', 'Lập trình Hướng đối tượng', 3, 30, 30, 'CNTT&TT'), 
-- ('CT237', 'Nguyên lý Hệ điều hành', 3, 30, 30, 'CNTT&TT'), 
-- ('TN001', 'Vi tích phân A1', 3, 45, 0, 'TN'), 
-- ('TN101', 'Xác suất thống kê', 3, 45, 0, 'KT'), 
-- ('SP102', 'Đại số tuyến tính', 4, 60, 0, 'SP'), 
-- ('TN172', 'Toán rời rạc', 4, 60, 0, 'TN'), 
-- ('XH023', 'Anh văn căn bản 1', 4, 60, 0, 'NNG'), 
-- ('TN021', 'Hóa học đại cương', 3, 60, 0, 'TS');

-- INSERT INTO khoa (maKhoa, tenKhoa) 
-- VALUES 
-- ('NNG', 'Khoa Ngoại ngữ'), 
-- ('CNTT&TT', 'Công nghệ thông tin và Truyền thông'), 
-- ('TN', 'Khoa Khoa học tự nhiên'), 
-- ('TS', 'Khoa Thủy sản'), 
-- ('SP', 'Khoa Sư phạm'), 
-- ('KT', 'Khoa Kinh tế');

-- INSERT INTO sinhVien (mssv, hoten, GT, ngaySinh, noiSinh, diaChi, maKhoa) 
-- VALUES 
-- ('B1234567', 'Nguyễn Thanh Hải', 'M', '2000-12-02', 'Bạc Liêu', 'Phòng 01, KTX Khu B, ĐHCT', 'CNTT&TT'),
-- ('B1234568', 'Trần Thanh Mai', 'M', '2001-01-20','Cần Thơ', '232, Nguyễn Văn Khéo, quận Ninh Kiều, TPCT', 'CNTT&TT'),
-- ('B1234569', 'Trần Thu Thủy', 'F', '2001-07-01', 'Cần Thơ', '02, Đại lộ Hòa Bình, quận Ninh Kiều, TPCT', 'CNTT&TT'),
-- ('B1334569', 'Nguyễn Thị Trúc Mã', 'F', '2002-05-25', 'Sóc Trăng', '343, Đường 30/4, quận Ninh Kiều, TPCT', 'SP'),
-- ('B1345678', 'Trần Hồng Trúc', 'F', '2002-03-02', 'Cần Thơ', '123, Trần Hưng Đạo, quận Ninh Kiều, TPCT', 'CNTT&TT'),
-- ('B1345679', 'Bùi Hoàng Yến', 'F', '2001-11-05', 'Vĩnh Long', 'Phòng 201, KTX Khu A, TPCT', 'CNTT&TT'),
-- ('B1345680', 'Trần Minh Tâm', 'M', '2001-02-04', 'Cà Mau', '07, Đại lộ Hòa Bình, quận Ninh Kiều, TPCT', 'KT'),
-- ('B1456789', 'Nguyễn Hồng Thắm', 'F', '2003-05-09', 'An Giang', '133, Nguyễn Văn Cừ, quận Ninh Kiều, TPCT', 'NNG'),
-- ('B1459230', 'Lê Văn Khang', 'M', '2002-06-02', 'Đồng Tháp', '312, Nguyễn Văn Linh, quận Ninh Kiều, TPCT', 'TN'),
-- ('B1456790', 'Lê Khải Hoàng', 'M', '2002-07-03', 'Kiên Giang', '03, Trần Hoàng Na, quận Ninh Kiều, TPCT', 'TS');

-- INSERT INTO ketQua (mssv, maHP, diem) 
-- VALUES 
-- ('B1234567', 'CT101', 4),
-- ('B1234568', 'CT176', 8),
-- ('B1234569', 'CT237', 9),
-- ('B1334569', 'SP102', 2),
-- ('B1345678', 'CT101', 6),
-- ('B1345679', 'CT176', 5),
-- ('B1456789', 'TN172', 10),
-- ('B1459230', 'TN172', 7),
-- ('B1456789', 'XH023', 6),
-- ('B1459230', 'XH023', 8),
-- ('B1234567', 'CT176', 1),
-- ('B1234568', 'CT101', 9),
-- ('B1234569', 'CT101', 8),
-- ('B1334569', 'CT101', 4),
-- ('B1345678', 'TN001', 6),
-- ('B1345679', 'CT101', 2),
-- ('B1456789', 'CT101', 7),
-- ('B1456790', 'TN101', 6),
-- ('B1345680', 'TN101', 7),
-- ('B1345680', 'XH023', 7);


-- Câu 20
alter table sinhvien add constraint kiemtra_mssv check (mssv regexp '^[A-Z0-9]{8}$');

-- Câu 19
alter table ketqua add constraint kiemtra_diem check (diem between 0 and 10);


-- Câu 18
select kq.mahp, sv.hoten, hp.tenhp
from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
					join hocphan hp on kq.mahp = hp.mahp
where kq.mahp = 'XH023'
order by kq.diem desc
limit 1;


-- Câu 17
select sv.mssv, sv.hoten, sv.makhoa
from sinhvien sv join khoa k on sv.makhoa = k.makhoa
				left join ketqua kq on sv.mssv = kq.mssv and k.tenkhoa = 'Anh văn căn bản 1'
where kq.diem is null;


-- Câu 16
select k.makhoa, k.tenkhoa, count(case when sv.gt='M' then 1 end) as soluongnam, count(case when sv.gt='F' then 1 end) as soluongnu
from sinhvien sv join khoa k on sv.makhoa = k.makhoa
group by k.makhoa;

-- Câu 15
select sv.mssv, sv.hoten, avg(kq.diem) as diemtb
from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
group by sv.mssv, sv.hoten
having diemtb = (
    select max(dtb)
    from (
        select avg(diem) as dtb
        from ketqua
        group by mssv
    ) AS maxdtb
);


-- Câu 14
select k.makhoa, k.tenkhoa, count(sv.mssv) as soluongsv
from khoa k join sinhvien sv on k.makhoa = sv.makhoa
group by k.makhoa;


-- Câu 13
select kq.mahp, hp.tenhp, count(kq.mssv) as soluongsv
from ketqua kq join hocphan hp on kq.mahp = hp.mahp
where kq.diem < 5
group by kq.mahp;


-- Câu 12
select hp.mahp, hp.tenhp, count(kq.mssv) as soluongsv
from ketqua kq join hocphan hp on kq.mahp = hp.mahp
group by kq.mahp
order by soluongsv desc
limit 1;



-- Câu 11
select hp.mahp, sv.hoten
from sinhvien sv join hocphan hp on sv.makhoa = hp.makhoa
where hp.sotietth = 0;


-- Câu 10
select sv.mssv, sv.hoten, kq.mahp, kq.diem
from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
where kq.mahp = 'CT101' and kq.diem between 5 and 7;


-- Câu 9
select sv.mssv, sv.hoten, sv.makhoa, kq.diem
from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
order by sv.makhoa asc, sv.hoten asc;

-- Câu 8
select sv.mssv, sv.hoten 
from sinhvien sv join ketqua kq1 on sv.mssv = kq1.mssv and kq1.mahp = 'CT101'
					join ketqua kq2 on sv.mssv = kq2.mssv and kq2.mahp = 'CT176';

-- Câu 7
select sv.mssv, sv.hoten, kq.mahp, kq.diem
from sinhvien sv join ketqua kq where sv.mssv = kq.mssv
having kq.diem < 5;


-- Câu 6
select hp.mahp, hp.tenhp
from ketqua kq right join hocphan hp on kq.mahp = hp.mahp
where kq.mahp is null;



-- Câu 5
select mssv, hoten, GT, makhoa
from sinhvien
where GT = 'M' and makhoa = 'CNTT&TT';


-- Câu 4
select mahp, tenhp
from hocphan
where sotinchi = 3 and sotietlt >= 45;


-- Câu 3
select mssv, hoten, YEAR(CURDATE()) - YEAR(ngaysinh) as tuoi
from sinhvien
where YEAR(CURDATE()) - YEAR(ngaysinh) between 20 and 22;


-- Câu 2
select mssv, hoten, ngaysinh, makhoa
from sinhvien
where hoten NOT LIKE 'L%' and hoten NOT LIKE 'T%';


-- Câu 1
select *
from sinhvien
order by mssv asc;






