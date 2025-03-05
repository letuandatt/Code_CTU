create database qlsv;

use qlsv;

create table sinhvien (
	masv char(10),
    tensv varchar(50),
    lopsv varchar(50),
    ngaynhaphoc date not null,
    primary key (masv)
);

insert into sinhvien value ('B0001', 'Nguyễn Châu', 'CT12', '2022-10-01');
insert into sinhvien value ('B0002', 'Trần Chí Thanh', 'CT13', '2021-09-05');
insert into sinhvien value ('B0003', 'Trương Hải Hà', 'CT12', '2022-10-02');
insert into sinhvien value ('B0004', 'Lê Văn Cường', 'CT14', '2023-09-01');
insert into sinhvien value ('B0005', 'Dương Thanh', 'CT14', '2023-09-09');

-- Giao dịch
create table trans1 (
	accountID int primary key,
    balance decimal(10, 2)
);

create table trans2 (
	accountID int primary key,
    balance decimal(10, 2)
);

start transaction;
insert into trans1 values (1, 1000.00);
insert into trans2 values (2, 2000.00);
commit;

-- Câu 10
start transaction;
update trans1 set balance = balance + 1000.00 where accountid = 1;
do sleep(5);
start transaction;
update trans2 set balance = balance + 1000.00 where accountid = 2;
do sleep(5);
update trans1 set balance = balance - 1000.00 where accountid = 1;
commit;
update trans2 set balance = balance - 1000.00 where accountid = 2;
commit;

select * from trans1, trans2;

-- Câu 9
start transaction;
set session transaction isolation level read uncommitted;
update trans1 set balance = balance - 100.00 where accountid = 1;
start transaction;
set session transaction isolation level read uncommitted;
update trans2 set balance = balance + 100.00 where accountid = 2;
select * from trans1, trans2;
commit;

-- Câu 8
delimiter $$

drop procedure if exists chuyentien $$
create procedure chuyentien(in sotien decimal(10, 2))
begin
	declare soDuTK1 decimal(10, 2);
    select balance from trans1 where accountid = 1 into soDuTK1;
    if soDuTK1 >= sotien then
		update trans1 set balance = balance - sotien where accountid = 1;
        update trans2 set balance = balance + sotien where accountid = 2;
	else
		rollback;
        signal sqlstate '45000'
        set message_text = 'Số dư tài khoản không đủ';
	end if;
end $$

start transaction;
call chuyentien(5000.00);
commit;

select * from trans1, trans2;

-- Câu 7
start transaction;
update trans1 set balance = balance - 1000.00 where accountid = 1;
update trans2 set balance = balance + 1000.00 where accountid = 2;
commit;

select * from trans1, trans2;

-- Câu 6
start transaction;
update trans1 set balance = 3000.00 where accountid = 1;
update trans2 set balance = 4000.00 where accountid = 2;
commit;

select * from trans1, trans2;

-- Câu 5
delimiter $$
drop trigger if exists GanGiaTriMacDinhLopSV;
create trigger GanGiaTriMacDinhLopSV
before insert
on sinhvien
for each row
begin
	if new.lopsv is null or new.lopsv = '' then
		set new.lopsv = 'CHUA XAC NHAN';
	end if;
end $$

insert into sinhvien value ('B0008', 'Lê Thị B', '', curdate());
select * from sinhvien;

-- Câu 4
delimiter $$
drop trigger if exists TuDongThemMaSV;
create trigger TuDongThemMaSV
before insert
on sinhvien
for each row
begin
	if substring(new.masv, 1, 1) != 'B' then
		set new.masv = concat('B', new.masv);
	end if;
end;

insert into sinhvien value ('0007', 'Nguyễn Văn A', 'CT15', curdate());
select * from sinhvien;

-- Câu 3
delimiter $$

drop trigger if exists TuDongCapNhatNgayNhapHoc;
create trigger TuDongCapNhatNgayNhapHoc
before insert
on sinhvien
for each row
begin
	if new.ngaynhaphoc is null then
		set new.ngaynhaphoc = curdate();
	end if;
end $$

insert into sinhvien(masv, tensv, lopsv) value ('B0006', 'Lê Tuấn Đạt', 'CT13');
select * from sinhvien;


-- Câu 2
delimiter $$

drop trigger if exists kiemtraxoaSV;
create trigger kiemtraxoaSV
before delete
on sinhvien
for each row
begin
	if old.lopsv = 'CT12' then
		signal sqlstate '45000'
        set message_text = 'Không thể xóa sinh viên của lớp CT12';
	end if;
end $$

delete from sinhvien where masv = 'B0003';

-- Câu 1
delimiter $$

create trigger kiemtrahopleMaSV
before insert
on sinhvien
for each row
begin
	if new.masv is null or new.masv = '' then
		signal sqlstate '45000'
        set message_text = "Mã SV không được trống";
	end if;
end $$

insert into sinhvien values ('', 'Lê Tuấn Đạt', 'CT12', '2021-10-01');