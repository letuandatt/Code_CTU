--BAI 1
--1.1----------------------------------------------------------
select      b.tenct, b.diachict
from        chuthau a, congtrinh b
where       a.msct = b.msct
            and a.tenthau = 'Hong Xuan Truong'
;
--1.2----------------------------------------------------------
select      distinct a.tenthau, a.diachithau
from        chuthau a, congtrinh b, thietke c, kientrucsu d
where       a.msct=b.msct
            and b.sttct=c.sttct
            and c.mskts=d.mskts
            and b.tinhthanh = 'TPCT'
            and d.hotenkts = 'Le Kim Dung'
;
--1.3----------------------------------------------------------
select      a.hotenkts, a.noitn
from        kientrucsu a, thietke b, congtrinh c
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and lower(c.tenct) = 'khach san quoc te'
            and c.tinhthanh = 'TPCT'
;
--1.4----------------------------------------------------------
select      distinct a.hotencn, a.ngaysinh
from        congnhan a, thamgia b, congtrinh c, chuthau d
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and c.msct=d.msct
            and (a.chuyenmon = 'han' or a.chuyenmon = 'dien')
            and d.tenthau = 'Le Van Son'
;
--1.5----------------------------------------------------------
select      a.hotencn, b.songay
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and lower(c.tenct)='khach san quoc te'
            and c.tinhthanh = 'TPCT'
            and b.ngaytg between 'DEC-15-94' and 'DEC-31-94'
;
--1.6----------------------------------------------------------
select      c.tenct, c.diachict
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and a.hotencn = 'Nguyen Hong Van'
            and 'DEC-18-94' between b.ngaytg and (b.ngaytg+b.songay)
;
--1.7----------------------------------------------------------
select      distinct a.hotenkts, a.ngaysinh
from        kientrucsu a, thietke b, congtrinh c
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and a.noitn = 'TP HCM'
            and c.kinhphi>400
;
--1.8----------------------------------------------------------
select      distinct a.hotencn, a.chuyenmon
from        congnhan a, thamgia b, congtrinh c, thietke d, kientrucsu e
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and c.sttct=d.sttct
            and d.mskts=e.mskts
            and e.hotenkts = 'Nguyen Anh Thu'
;
--1.9----------------------------------------------------------
select      distinct a.tenchu
from        chunhan a, congtrinh b, chuthau c, thietke d, kientrucsu e 
where       a.msch=b.msch
            and b.msct=c.msct
            and b.sttct=d.sttct
            and d.mskts=e.mskts
            and e.hotenkts = 'Nguyen Anh Thu'
            and c.tenthau = 'Hoang Cong Binh'
;
--1.10----------------------------------------------------------
select      a.tenct
from        congtrinh a, thietke b, kientrucsu c
where       a.sttct=b.sttct
            and b.mskts=c.mskts
            and c.noitn = 'TP HCM'
            and b.thulao>20
;

------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
--BAI 2
--2.1----------------------------------------------------------
select      distinct a.mskts, a.hotenkts
from        kientrucsu a, thietke b, congtrinh c, chuthau d
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and c.msct=d.msct
            and d.tenthau = 'Hoang Cong Binh'
INTERSECT
select      distinct a.mskts, a.hotenkts
from        kientrucsu a, thietke b, congtrinh c, chuthau d
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and c.msct=d.msct
            and d.tenthau = 'Le Van Son'
;
--2.2----------------------------------------------------------
select      sttct, tenct
from        congtrinh
where       kinhphi = (select max(kinhphi)
                       from congtrinh)
;
--2.3----------------------------------------------------------
select      a.mscn, a.hotencn
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and c.tinhthanh = 'TPCT'
MINUS
select      a.mscn, a.hotencn
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and c.tinhthanh = 'Vinh Long'
;
--2.4----------------------------------------------------------
select      distinct a.msct, a.tenthau
from        chuthau a, congtrinh b
where       a.msct=b.msct
            and b.kinhphi > ALL(select  b.kinhphi
                                from    congtrinh b, chuthau a
                                where   b.msct=a.msct
                                        and a.tenthau = 'Hoang Cong Binh')
;
--2.5----------------------------------------------------------
select      distinct a.mskts, a.hotenkts
from        kientrucsu a, thietke b
where       a.mskts=b.mskts
            and b.thulao < ALL(select   TO_CHAR(AVG(thulao), '99.99')
                               from     thietke)
order by    a.mskts                               
;
--2.6----------------------------------------------------------
select      distinct a.tenthau, a.diachithau
from        chuthau a, congtrinh b
where       a.msct=b.msct
            and b.kinhphi = (select   MIN(kinhphi)
                               from     congtrinh)
;
--2.7----------------------------------------------------------
select      a.hotencn, a.chuyenmon
from        congnhan a, thamgia b, congtrinh c, thietke d, kientrucsu e
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and c.sttct=d.sttct
            and d.mskts=e.mskts
            and e.hotenkts = 'Le Thanh Tung'
            and EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM a.ngaysinh)<40
;
--2.8----------------------------------------------------------
select      distinct a.tenthau, a1.tenthau tenthau_1
from        chuthau a, chuthau a1, congtrinh b, congtrinh b1
where       a.msct=b.msct
            and a1.msct=b1.msct
            and b.tinhthanh = b1.tinhthanh
            and a.tenthau>a1.tenthau
            
;
--2.9----------------------------------------------------------
select      c.tenct, c.ngaybd
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and a.hotencn = 'Nguyen Thi Suu'
INTERSECT
select      c.tenct, c.ngaybd
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and a.hotencn = 'Le Manh Quoc'
;
--2.10----------------------------------------------------------
select      distinct a.mscn, a.hotencn
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
            and c.kinhphi > (select     AVG(kinhphi)
                             from       congtrinh)
;

------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------

--BAI 3
--3.1----------------------------------------------------------
select      b.msct, b.tenthau, SUM(a.kinhphi) tongkp
from        congtrinh a, chuthau b
where       a.msct=b.msct
group by    b.msct, b.tenthau
;
--3.2----------------------------------------------------------
create view tam2 as
    select      a.mskts, sum(thulao) tongtl
    from        kientrucsu a, thietke b
    where       a.mskts=b.mskts
    group by    a.mskts
    
select      a.mskts, a.hotenkts, b.tongtl
from        kientrucsu a, tam2 b
where       a.mskts=b.mskts
            and b.tongtl>25
            
drop view tam2
;
--3.3------------------------------------------------
create view tam3 as
    select      a.mskts, SUM(b.thulao) tongtl
    from        kientrucsu a, thietke b
    where       a.mskts=b.mskts
    group by    a.mskts

select      COUNT(mskts) tongkts
from        tam3 
where       tongtl>50

drop view tam3
;
--3.4----------------------------------------------------------
create view tam4 as
    select      b.sttct, COUNT(a.mscn) tongcn
    from        thamgia a, congtrinh b
    where       a.sttct=b.sttct
    group by    b.sttct

select      a.sttct, a.tenct, b.tongcn
from        congtrinh a, tam4 b
where       a.sttct=b.sttct

drop view tam4
;
--3.5----------------------------------------------------------
create view tam5 as
    select      b.sttct, COUNT(a.mscn) tongcn
    from        thamgia a, congtrinh b
    where       a.sttct=b.sttct
    group by    b.sttct

select      a.tenct, a.diachict
from        congtrinh a, tam5 b
where       a.sttct=b.sttct
            and tongcn = (select max(tongcn) from tam5)

drop view tam5
;
--3.6----------------------------------------------------------
create view tam6 as
    select      tinhthanh, TO_CHAR(AVG(kinhphi), '9999.99') kinhphitb
    from        congtrinh
    group by    tinhthanh

select      tinhthanh, kinhphitb
from        tam5
where       kinhphitb>1000.00

drop view tam6
;
--3.7----------------------------------------------------------
create view tam7 as
    select      mscn, SUM(songay) tongngay
    from        thamgia
    group by    mscn

select      a.mscn, a.hotencn
from        congnhan a, tam7 b
where       a.mscn=b.mscn
            and b.tongngay > (select b.tongngay
                              from   tam7 b, congnhan a
                              where  a.mscn=b.mscn
                                     and a.hotencn = 'Nguyen Hong Van')

drop view tam7
;
--3.8----------------------------------------------------------
select      a.msct, a.tenthau, b.tinhthanh, COUNT(b.sttct) socongtrinh
from        chuthau a, congtrinh b
where       a.msct=b.msct
            and a.tenthau LIKE '% Van %'
group by    a.msct, a.tenthau, b.tinhthanh
;
--3.9----------------------------------------------------------
create view tam9 as
    select      a.mscn, a.hotencn, COUNT(b.sttct) socongtrinh
    from        congnhan a, thamgia b
    where       a.mscn=b.mscn
    group by    a.mscn, a.hotencn

    select      mscn, hotencn
    from        tam9
    where       socongtrinh = (select  COUNT(sttct)-3 soct
                               from     congtrinh)

drop view tam9
;
--3.10----------------------------------------------------------
create view tam10 as
    select      a.mscn, b.mscn mscn_1, 
                COUNT(CASE WHEN a.sttct=b.sttct THEN a.sttct END) socongtrinh_chung
    from        thamgia a, thamgia b
    where       a.mscn<b.mscn
    group by    a.mscn, b.mscn      

select      a.hotencn, a1.hotencn hotencn_1
from        congnhan a, congnhan a1, tam10 b
where       a.mscn = b.mscn
            and a1.mscn = b.mscn_1
            and b.socongtrinh_chung>=2        

drop view tam10
;

------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
--BAI 4
--4.1----------------------------------------------------------
select      distinct a.hotenkts, a.noitn
from        kientrucsu a, thietke b, congtrinh c
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and a.hotenkts LIKE 'Le %'
            and c.tinhthanh IN (select   b.tinhthanh
                               from     chuthau a, congtrinh b
                               where    a.msct=b.msct
                                        and a.tenthau = 'Hoang Cong Binh')
;
--4.2----------------------------------------------------------
select      a.sttct, a.tenct, a.kinhphi
from        kientrucsu c, thietke b, congtrinh a
where       c.mskts=b.mskts
            and b.sttct=a.sttct
            and EXTRACT(YEAR FROM c.ngaysinh) = (select MIN(EXTRACT(YEAR FROM ngaysinh))
                                                 from kientrucsu)
;
--4.3----------------------------------------------------------
select      a.mskts, a.hotenkts
from        kientrucsu a, thietke b, congtrinh c, chunhan d
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and c.msch=d.msch
            and d.diachichu = '101 Hai Ba Trung'
;
--4.4----------------------------------------------------------
create view tam4 as
    select      msct, COUNT(sttct) socongtrinh
    from        congtrinh
    group by    msct       

select      distinct a.mskts, a.hotenkts
from        kientrucsu a, thietke b, congtrinh c, chuthau d, tam4 e
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            --and c.msct=d.msct
            and e.msct=c.msct
            and EXTRACT(YEAR FROM CURRENT_DATE)-EXTRACT(YEAR FROM a.ngaysinh)<40
            and e.socongtrinh>=3

drop view tam4
;
--4.5----------------------------------------------------------
select      a.mscn, a.hotencn
from        congnhan a, thamgia b, congtrinh c
where       a.mscn=b.mscn
            and b.sttct=c.sttct
group by    a.mscn, a.hotencn
having      COUNT(c.tinhthanh)>2
;
--4.6----------------------------------------------------------
create view tam6 as
select      b.tinhthanh, COUNT(a.mscn) socn
from        thamgia a, congtrinh b
where       a.sttct=b.sttct
group by    b.tinhthanh

select      tinhthanh
from        tam6
where       socn = (select MAX(socn) from tam6)

drop view tam6
;
--4.7----------------------------------------------------------
create view tam7 as
    select      c.tinhthanh, SUM(b.thulao) thulao
    from        kientrucsu a, thietke b, congtrinh c
    where       a.mskts=b.mskts
                and b.sttct=c.sttct
                and a.hotenkts = 'Le Kim Dung'
    group by    c.tinhthanh
                
select      tinhthanh
from        tam7
where       thulao = (select MIN(thulao) from tam7)

drop view tam7
;
--4.8----------------------------------------------------------
select      a.hotenkts, e.hotencn
from        kientrucsu a, thietke b, congtrinh c, thamgia d, congnhan e
where       a.mskts=b.mskts
            and b.sttct=c.sttct
            and d.sttct=c.sttct
            and d.mscn=e.mscn
            and b.sttct=d.sttct
            and EXTRACT(YEAR FROM a.ngaysinh) < EXTRACT(YEAR FROM e.ngaysinh)
;
--4.9----------------------------------------------------------
select      a.mscn, a.hotencn, COUNT(b.sttct) socongtrinh
from        congnhan a, thamgia b
where       a.mscn=b.mscn
            and EXTRACT(MONTH FROM a.ngaysinh)=5
group by    a.mscn, a.hotencn
;
--4.10----------------------------------------------------------
create view tam10 as
    select      c.sttct, c.tenct, COUNT(b.mscn) socongnhan,
                COUNT(CASE WHEN a.phai='Nam' THEN a.mscn END) sonam,
                COUNT(CASE WHEN a.phai='Nu' THEN a.mscn END) sonu
    from        congnhan a, thamgia b, congtrinh c
    where       a.mscn=b.mscn
                and b.sttct=c.sttct
    group by    c.sttct, c.tenct

select      sttct, tenct, socongnhan, sonam, sonu
from        tam10
where       socongnhan>2

drop view tam10
;
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
--BAI 5
--5.1-------------------------------------------------------
select      a.mscn, a.hotencn, c.tenct
from        congnhan a left outer join thamgia b on a.mscn=b.mscn
            left outer join congtrinh c on b.sttct=c.sttct
order by    a.mscn     
;
--5.2-------------------------------------------------------
select      a.mscn, a.hotencn
from        congnhan a left outer join thamgia b on a.mscn=b.mscn
where       b.sttct IS NULL
order by    a.mscn 
;
--5.3-------------------------------------------------------
select      a.sttct, a.tenct, COUNT(b.mscn) socn
from        congtrinh a left outer join thamgia b on a.sttct=b.sttct
group by    a.sttct, a.tenct       
;
--5.4-------------------------------------------------------
select      a.mscn, a.hotencn, COUNT(b.sttct) soct
from        congnhan a left outer join thamgia b on a.mscn=b.mscn
group by    a.mscn, a.hotencn   
;
--5.5-------------------------------------------------------
create view tam5 as
    select      a.mskts, a.hotenkts, a.noitn, COUNT(b.sttct) soct
    from        kientrucsu a left outer join thietke b on a.mskts=b.mskts
    group by    a.mskts, a.hotenkts, a.noitn       

select      mskts, hotenkts, noitn
from        tam5
where       soct = 0

drop view tam5;
;
--5.6-------------------------------------------------------
create view tam6 as
    select      distinct a.sttct, a.tenct, a.kinhphi, COUNT (b.mskts) sokts
    from        congtrinh a left outer join thietke b on a.sttct=b.sttct
    group by    a.sttct, a.tenct, a.kinhphi   

select      sttct, tenct
from        tam6
where       sokts = 0
            and kinhphi>3500

drop view tam6
;
--5.7-------------------------------------------------------
create view tam7 as
    select      a.msch, a.tenchu, b.tenct, COUNT(c.mscn) socn
    from        chunhan a left outer join congtrinh b on a.msch=b.msch
                left outer join thamgia c on b.sttct=c.sttct 
    group by    a.msch, a.tenchu, b.tenct   

select      msch, tenchu, tenct
from        tam7
where       socn = 0
            and tenct IS NOT NULL

drop view tam7
;
--5.8-------------------------------------------------------
create view tam8 as
    select      a.mscn, a.hotencn, a.ngaysinh,
                COUNT(b.sttct) soct
    from        congnhan a left outer join thamgia b on a.mscn=b.mscn
    group by    a.mscn, a.hotencn, a.ngaysinh

select      mscn, hotencn
from        tam8
where       soct = 0
            and EXTRACT(YEAR FROM ngaysinh) = (select MAX(EXTRACT(YEAR FROM ngaysinh))
                                               from   tam8
                                               where  soct=0)

drop view tam8
;
--5.9-------------------------------------------------------
create view tam9 as
    select      a.msct, a.tenthau, b.tinhthanh,
                COUNT(b.sttct) soct
                --COUNT(CASE WHEN b.tinhthanh<>'TPCT' THEN a.msct END) dem
    from        chuthau a left outer join congtrinh b on a.msct=b.msct
    --where       b.tinhthanh = 'TPCT'
    group by    a.msct, a.tenthau, b.tinhthanh
    --having      COUNT(CASE WHEN b.tinhthanh<>'TPCT' THEN a.msct END) = 0
select      
from        
where       

drop view tam9
;
--5.10-------------------------------------------------------
create view tam10 as
    select      a.msch, a.tenchu, a.diachichu,
                COUNT(c.mscn) socn,
                COUNT(CASE WHEN d.phai='Nu' THEN d.mscn END) socn_nu
    from        chunhan a left outer join congtrinh b on a.msch=b.msch
                left outer join thamgia c on b.sttct=c.sttct
                left outer join congnhan d on c.mscn=d.mscn
    group by    a.msch, a.tenchu, a.diachichu
    --where       

select      msch, tenchu
from        tam10
where       tenchu LIKE 'Nguyen %'
            and diachichu LIKE '% Hai Ba Trung'
            and socn_nu = 0

drop view tam10
;


---------------------------------------------------------
---------------------------------------------------------
select      
from        
where       
;
