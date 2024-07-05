
-- 1
select * from khoahoc;
select * from hocvien;
select * from chuongtrinh;
select * from loailop
select * from lop;
--2
select * 
from hocvien
where gioitinh=1;
--3
select hoten
from hocvien
where diachi LIKE '%C¿n Tho%';
--4
select l.*
from lop l join khoahoc k on k.makh=l.makh
where tenkh='Khóa 1';
--
select *
from lop l , khoahoc k
where k.makh=l.makh
     and tenkh='Khóa 1';
--5
select mahv,tenhv
from  khoahoc k join lop l on k.makh=l.makh
        join phieuthu p on p.malop=l.malop
        join hocvien h on h.mahv=p.mahv
where tenkh='Khóa 1';
--8
select *
from hocvien
where extract(month from ngaysinh)=12 and extract(year from ngaysinh)=2001;
--9
--10
select *
from phieuthu
where ngaylapphieu between '2021-06-05' and '2021-06-10';
--13
select p.*
from phieuthu p join lop l on p.malop=l.malop
       join loailop ll on ll.maloai=l.maloai
where l.tenlop='L¿p 1' and tenloai='Ti¿ng Anh A1';
--15
select count(*) sohv 
from hocvien
--16
select count(*)
from phieuthu p join hocvien h on p.mahv=h.mahv
      join lop l on l.malop=p.malop
      join loailop ll on ll.maloai=l.maloai
where l.tenlop='L¿p 1' and tenloai='Ti¿ng Anh can b¿n';   