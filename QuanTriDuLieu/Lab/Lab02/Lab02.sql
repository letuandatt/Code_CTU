use qldiem;

-- Câu 1
delimiter $$
drop procedure if exists hienthikhoa $$
create procedure hienthikhoa (in ma_khoa char(8))
begin
	if exists (select * from khoa where makhoa=ma_khoa) then
		select k.makhoa, k.tenkhoa, count(sv.mssv) as soluong_sv
        from sinhvien sv join khoa k on sv.makhoa = k.makhoa
        where k.makhoa = ma_khoa
        group by k.makhoa;
	else
		select "Không có khoa" as thongbao;
	end if;
end $$

call hienthikhoa("MT");

-- Câu 2
delimiter $$
drop procedure if exists hienthisinhvien $$
create procedure hienthisinhvien (in diem_ int)
begin
	if exists (select * from ketqua where diem < diem_) then
		select sv.mssv, sv.hoten, kq.mahp, kq.diem
        from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
        where kq.diem < diem_;
	else
		select "Không có sinh viên nào" as thongbao;
	end if;
end $$
call hienthisinhvien(1);

-- Câu 3
delimiter $$
drop procedure if exists diem_tb $$
create procedure diem_tb (in mssv_ char(8), out dtb float)
begin
	if exists (select * from sinhvien where mssv = mssv_) then
		set dtb = (
			select sum(kq.diem * hp.sotinchi) / sum(hp.sotinchi)
            from ketqua kq join hocphan hp on kq.mahp = hp.mahp
            where kq.mssv = mssv_
            group by kq.mssv
        );
	else 
		set dtb = -1;
	end if;
end $$

call diem_tb('B1234567', @dtb);
select @dtb as diemtb;

-- Câu 4
delimiter $$
drop procedure if exists BangDiem_TB $$
create procedure BangDiem_TB (in makhoa_ char(8))
begin
	select k.tenkhoa, sv.hoten, (sum(kq.diem * hp.sotinchi) / sum(hp.sotinchi)) as diemtrungbinh
    from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
						join hocphan hp on kq.mahp = hp.mahp
							join khoa k on sv.makhoa = k.makhoa
	where sv.mssv in (select mssv from sinhvien where makhoa = makhoa_)
    group by kq.mssv;
end $$

call BangDiem_TB("CNTT&TT");

-- Câu 5
delimiter $$
drop procedure if exists svchuahochp $$
create procedure svchuahochp(in mahp_ char(5))
begin
	if exists (select * from hocphan where mahp = mahp_) then
		select distinct kq.mssv, sv.hoten
        from ketqua kq join sinhvien sv on kq.mssv = sv.mssv
		where kq.mssv not in (select mssv from ketqua where mahp = mahp_);
	else
		select "Không có học phần này" as thongbao;
	end if;
end $$

call svchuahochp("CT175");

-- Câu 6
delimiter $$
drop procedure if exists Xep_Loai $$
create procedure Xep_Loai (in mssv_ char(8))
begin
	declare dtb decimal(3, 1);
    declare loai varchar(50);
    
    call diem_tb(mssv_, dtb);
    
    if dtb >= 9.0 then
		set loai = "Xuất sắc";
	elseif dtb >= 8.0 then
		set loai = "Giỏi";
	elseif dtb >= 7.0 then
		set loai = "Khá";
	elseif dtb >= 6.0 then
		set loai = "Trung bình khá";
	elseif dtb >= 5.0 then
		set loai = "Trung bình";
	else
		set loai = "Không đủ điều kiện tốt nghiệp";
	end if;
    
    select mssv_ as mssv, dtb as diemtb, loai as xeploai;
end $$ 

call Xep_Loai("B1234567");

-- Câu 7
delimiter $$
drop procedure if exists SV_LOAI $$
create procedure SV_LOAI (in loai_ varchar(50))
begin
	declare gioihantren decimal(10, 2);
    declare gioihanduoi decimal(10, 2);
    
    if loai_ = "Xuất sắc" then
		set gioihantren = 10.0;
        set gioihanduoi = 9.0;
	elseif loai_ = "Giỏi" then
		set gioihantren = 8.9;
        set gioihanduoi = 8.0;
	elseif loai_ = "Khá" then
		set gioihantren = 7.9;
        set gioihanduoi = 7.0;
	elseif loai_ = "Trung bình khá" then
		set gioihantren = 6.9;
        set gioihanduoi = 6.0;
	elseif loai_ = "Khá" then
		set gioihantren = 5.9;
        set gioihanduoi = 5.0;
	else
		select "Loại không hợp lệ" as thongbao;
	end if;
    
	select sv.mssv, sv.hoten, (sum(kq.diem * hp.sotinchi) / sum(hp.sotinchi)) as diemtrungbinh
    from sinhvien sv join ketqua kq on sv.mssv = kq.mssv
					join hocphan hp on kq.mahp = hp.mahp
	group by sv.mssv, sv.hoten
    having diemtrungbinh between gioihanduoi and gioihantren;
end $$

call SV_LOAI("Giỏi");

-- Câu 8
delimiter $$
drop function if exists tongdvhoctrinh $$
create function tongdvhoctrinh (mssv_ char(10))
returns int
deterministic
begin
	declare tongsodvht int;
    select sum(hp.sotietlt + hp.sotietth) into tongsodvht
    from hocphan hp join ketqua kq on hp.mahp = kq.mahp
    where kq.mssv = mssv_;
    return tongsodvht;
end $$
select tongdvhoctrinh("B1234567");

-- Câu 9
delimiter $$
drop function if exists TOT_NGHIEP $$
create function TOT_NGHIEP (mssv_ char(8))
returns bool
deterministic
begin
	declare dtb decimal(10, 2);
    select sum((kq.diem * 0.4) * hp.sotinchi) / sum(hp.sotinchi) into dtb
    from ketqua kq join hocphan hp on hp.mahp = kq.mahp
    where kq.mssv = mssv_;
    if dtb >= 2.5 then
		return true;
	else
		return false;
	end if;
end $$

select TOT_NGHIEP("B1234568");

-- Câu 10
DELIMITER $$
DROP FUNCTION IF EXISTS SL_SV_TOT_NGHIEP $$
CREATE FUNCTION SL_SV_TOT_NGHIEP (tenKhoa_ VARCHAR(100))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE totalSVTotNghiep INT;
    SELECT COUNT(*) INTO totalSVTotNghiep
    FROM sinhVien sv
    JOIN khoa k ON sv.maKhoa = k.maKhoa
    WHERE k.tenKhoa = tenKhoa_
    AND TOT_NGHIEP(sv.mssv) = TRUE;
    RETURN totalSVTotNghiep;
END $$

SELECT k.maKhoa, SL_SV_TOT_NGHIEP(k.tenKhoa) AS soLuongSVTotNghiep
FROM khoa k
WHERE k.tenKhoa = 'Công nghệ thông tin và truyền thông';

-- Câu 11
delimiter $$
drop function if exists dhpnhohon5 $$
create function dhpnhohon5 (mssv_ char(8))
returns int
deterministic
begin
	declare sohpdiemnhohon5 int;
    select count(diem) as slhpdiemnhohon5 into sohpdiemnhohon5
    from ketqua
    where mssv = mssv_ and diem < 5;
    return sohpdiemnhohon5;
end $$
select dhpnhohon5("B1234568");