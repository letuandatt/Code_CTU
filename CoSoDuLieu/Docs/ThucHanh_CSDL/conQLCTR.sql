CREATE TABLE  CGTRINH (
	STT_CTR int NOT NULL ,
	TEN_CTR varchar (20)  NULL ,
	DIACHI_CTR varchar (20)  NULL ,
	TINH_THANH varchar (15)  NULL ,
	KINH_PHI int NULL ,
	TEN_CHU varchar (20)  NULL ,
	TEN_THAU varchar (20)  NULL ,
	NGAY_BD date NULL 
) ;


CREATE TABLE  CHUNHAN (
	TEN_CHU varchar (20)  NOT NULL ,
	DCHI_CHU varchar (20)  NULL 
) ;


CREATE TABLE  CHUTHAU (
	TEN_THAU varchar (20)  NOT NULL ,
	TEL char (7)  NULL ,
	DCHI_THAU varchar (20)  NULL 
) ;


CREATE TABLE  CONGNHAN (
	HOTEN_CN varchar (20)  NOT NULL ,
	NAMS_CN int NULL ,
	NAM_VAO_N int NULL ,
	CH_MON varchar (10)  NULL 
) ;


CREATE TABLE  KTRUCSU (
	HOTEN_KTS varchar (20)  NOT NULL ,
	NAMS_KTS int NULL ,
	PHAI char (2)  NULL ,
	NOI_TN varchar (15)  NULL ,
	DCHI_LL_KTS varchar (30)  NULL 
) ;


CREATE TABLE  THAMGIA (
	HOTEN_CN varchar (20)  NOT NULL ,
	STT_CTR int NOT NULL ,
	NGAY_TGIA date NULL ,
	SO_NGAY int NULL 
) ;


CREATE TABLE  THIETKE (
	HOTEN_KTS varchar (20)  NOT NULL ,
	STT_CTR int NOT NULL ,
	THU_LAO int NULL 
) ;


ALTER TABLE  CGTRINH ADD 
	CONSTRAINT PK_CGTRINH PRIMARY KEY  	(STT_CTR	)  ; 


ALTER TABLE  CHUNHAN ADD 
	CONSTRAINT PK_CHUNHAN PRIMARY KEY  (	TEN_CHU	)  ; 


ALTER TABLE  CHUTHAU ADD 
	CONSTRAINT PK_CHUTHAU PRIMARY KEY  (	TEN_THAU	)  ; 


ALTER TABLE  CONGNHAN ADD 
	CONSTRAINT PK_CONGNHAN PRIMARY KEY  (	HOTEN_CN	)  ; 


ALTER TABLE  KTRUCSU ADD 
	CONSTRAINT PK_KTRUCSU PRIMARY KEY  	(	HOTEN_KTS	)  ; 


ALTER TABLE  THAMGIA ADD 
	CONSTRAINT PK_THAMGIA PRIMARY KEY  	(	HOTEN_CN,	STT_CTR	)  ; 


ALTER TABLE  THIETKE ADD 
	CONSTRAINT PK_THIETKE PRIMARY KEY  	(	HOTEN_KTS,	STT_CTR	)  ; 


ALTER TABLE  CGTRINH ADD 
	CONSTRAINT FK_CGTRINH_CHUNHAN FOREIGN KEY 	(	TEN_CHU	) REFERENCES  CHUNHAN (	TEN_CHU	);

ALTER TABLE  CGTRINH ADD 
	CONSTRAINT FK_CGTRINH_CHUTHAU FOREIGN KEY 
	(	TEN_THAU	) REFERENCES  CHUTHAU (	TEN_THAU	);


ALTER TABLE  THAMGIA ADD 
	CONSTRAINT FK_THAMGIA_CGTRINH FOREIGN KEY 
	(		STT_CTR	) REFERENCES  CGTRINH (		STT_CTR	);

ALTER TABLE  THAMGIA ADD 
	CONSTRAINT FK_THAMGIA_CONGNHAN FOREIGN KEY 
	(		HOTEN_CN	) REFERENCES  CONGNHAN (		HOTEN_CN	);


ALTER TABLE  THIETKE ADD 
	CONSTRAINT FK_THIETKE_CGTRINH FOREIGN KEY 	(STT_CTR) REFERENCES  CGTRINH (	STT_CTR	);

ALTER TABLE  THIETKE ADD 
	CONSTRAINT FK_THIETKE_KTRUCSU FOREIGN KEY 
	(	HOTEN_KTS	) REFERENCES  KTRUCSU (	HOTEN_KTS );


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

------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
--PHAN TU LUYEN
--CAU 3----------------------------------------------------------
select      *
from        ktrucsu
where       hoten_kts LIKE 'le %'
            and nams_kts = 1956
;
--CAU 4----------------------------------------------------------
select      ten_ctr
from        cgtrinh
where       ngay_bd between 'SEP-1-1994' and 'OCT-20-1994'
;
--CAU 5----------------------------------------------------------
select      ten_ctr, diachi_ctr
from        cgtrinh
where       ten_thau = 'cty xd so 6'
;
--CAU 6----------------------------------------------------------
select      distinct a.ten_thau, a.dchi_thau
from        chuthau a, cgtrinh b, thietke c, ktrucsu d
where       a.ten_thau=b.ten_thau
            and b.stt_ctr=c.stt_ctr
            and c.hoten_kts=d.hoten_kts
            and b.tinh_thanh = 'can tho'
            and d.hoten_kts = 'le kim dung'
;
--CAU 7----------------------------------------------------------
select      distinct a.noi_tn
from        ktrucsu a, thietke b, cgtrinh c
where       a.hoten_kts=b.hoten_kts
            and b.stt_ctr=c.stt_ctr
            and c.ten_ctr = 'khach san quoc te'
            and c.tinh_thanh = 'can tho'
;
--CAU 8----------------------------------------------------------
select      a.hoten_cn, a.nams_cn, a.nam_vao_n
from        congnhan a, thamgia b, cgtrinh c, chuthau d
where       a.hoten_cn=b.hoten_cn
            and b.stt_ctr=c.stt_ctr
            and c.ten_thau=d.ten_thau
            and (a.ch_mon='han' OR a.ch_mon='dien')
            and d.ten_thau = 'le van son'
;
--CAU 9----------------------------------------------------------
select      a.hoten_cn
from        thamgia a, cgtrinh b
where       a.stt_ctr=b.stt_ctr
            and b.ten_ctr = 'khach san quoc te'
            and b.tinh_thanh = 'can tho'
            and a.ngay_tgia between 'DEC-15-1994' and 'DEC-31-1994'
;
--CAU 10----------------------------------------------------------
create view tam10 as
    select      a.hoten_kts, a.nams_kts, a.noi_tn,
                COUNT(CASE WHEN c.kinh_phi>400 THEN c.stt_ctr END) so_ctr
    from        ktrucsu a, thietke b, cgtrinh c
    where       a.hoten_kts=b.hoten_kts
                and b.stt_ctr=c.stt_ctr
    group by    a.hoten_kts, a.nams_kts, a.noi_tn

select      hoten_kts, nams_kts
from        tam10
where       noi_tn = 'tp hcm'
            and so_ctr>=1

drop view tam10
;
--CAU 11----------------------------------------------------------
select      a.hoten_cn, a.ch_mon
from        congnhan a, thamgia b, cgtrinh c, thietke d, ktrucsu e
where       a.hoten_cn=b.hoten_cn
            and b.stt_ctr=c.stt_ctr
            and c.stt_ctr=d.stt_ctr
            and d.hoten_kts=e.hoten_kts
            and e.hoten_kts = 'le thanh tung'
;
--CAU 12----------------------------------------------------------
select      ten_ctr
from        cgtrinh
where       kinh_phi = (select MIN(kinh_phi) from cgtrinh)
;
--CAU 13----------------------------------------------------------
select      hoten_kts
from        ktrucsu
where       EXTRACT(YEAR FROM CURRENT_DATE)-nams_kts = (select MIN(EXTRACT(YEAR FROM CURRENT_DATE)-nams_kts) from ktrucsu) 
;
--CAU 14----------------------------------------------------------
select      ten_thau, SUM(kinh_phi) tong_kp
from        cgtrinh
group by    ten_thau       
;
--CAU 15----------------------------------------------------------
select      a.ten_thau, a.dchi_thau
from        chuthau a, cgtrinh b
where       a.ten_thau=b.ten_thau
            and b.kinh_phi = (select MIN(kinh_phi) from cgtrinh)
;
--CAU 16----------------------------------------------------------
create view tam16 as
    select      hoten_kts, SUM(thu_lao) tong_thulao
    from        thietke 
    group by    hoten_kts

select      hoten_kts
from        tam16
where       tong_thulao > 25

drop view tam16
;
--CAU 17----------------------------------------------------------
create view tam17 as
    select      hoten_kts, SUM(thu_lao) tong_thulao
    from        thietke 
    group by    hoten_kts

select      COUNT(hoten_kts) so_kts
from        tam17
where       tong_thulao > 25

drop view tam17
;
--CAU 18----------------------------------------------------------
select      hoten_kts, COUNT(stt_ctr) so_ctr
from        thietke
group by    hoten_kts
;
--CAU 19----------------------------------------------------------
select      b.stt_ctr, b.ten_ctr, COUNT(a.hoten_cn) tong_cn
from        thamgia a, cgtrinh b
where       a.stt_ctr=b.stt_ctr
group by    b.stt_ctr, b.ten_ctr
;
--CAU 20----------------------------------------------------------
create view tam20 as
    select      b.ten_ctr, b.diachi_ctr, COUNT(a.hoten_cn) tong_cn
    from        thamgia a, cgtrinh b
    where       a.stt_ctr=b.stt_ctr
    group by    b.ten_ctr, b.diachi_ctr

select      ten_ctr, diachi_ctr
from        tam20
where       tong_cn = (select MAX(tong_cn) from tam20)

drop view tam20
;
--CAU 21----------------------------------------------------------
select      tinh_thanh, TO_CHAR(AVG(kinh_phi), '9999.99') kinhphi_tb
from        cgtrinh
group by    tinh_thanh       
;

------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
------------------------------------------------------------
--PHAN CO HUONG DAN
--CAU 22----------------------------------------------------------
select      a.ten_ctr, a.diachi_ctr
from        cgtrinh a, thamgia b, congnhan c
where       a.stt_ctr=b.stt_ctr
            and b.hoten_cn=c.hoten_cn
            and c.hoten_cn = 'nguyen hong van'
            and 'DEC-18-1994' between b.ngay_tgia and (b.ngay_tgia+so_ngay)
;
--CAU 23----------------------------------------------------------
select      a.hoten_kts
from        thietke a, cgtrinh b, chuthau c
where       a.stt_ctr=b.stt_ctr
            and b.ten_thau=c.ten_thau
            and c.ten_thau = 'phong dich vu so xd'
INTERSECT
select      a.hoten_kts
from        thietke a, cgtrinh b, chuthau c
where       a.stt_ctr=b.stt_ctr
            and b.ten_thau=c.ten_thau
            and c.ten_thau = 'le van son'
;
--CAU 24----------------------------------------------------------
select      a.hoten_cn
from        thamgia a, cgtrinh b
where       a.stt_ctr=b.stt_ctr
            and b.tinh_thanh = 'can tho'
MINUS
select      a.hoten_cn
from        thamgia a, cgtrinh b
where       a.stt_ctr=b.stt_ctr
            and b.tinh_thanh = 'vinh long'
;
--CAU 25----------------------------------------------------------
select      ten_thau
from        cgtrinh
where       kinh_phi > ALL(select kinh_phi
                           from cgtrinh
                           where ten_thau = 'phong dich vu so xd')
;
--CAU 26----------------------------------------------------------
select      distinct hoten_kts
from        thietke
where       thu_lao < (select TO_CHAR(AVG(thu_lao), '9999.99')
                       from thietke)
;
--CAU 27----------------------------------------------------------
create view tam27 as
    select      hoten_cn, SUM(so_ngay) tong_so_ngay
    from        thamgia
    group by    hoten_cn       

select      hoten_cn
from        tam27
where       tong_so_ngay > (select tong_so_ngay 
                            from tam27 
                            where hoten_cn='nguyen hong van')

drop view tam27
;
--CAU 28----------------------------------------------------------
select      hoten_cn
from        thamgia
group by    hoten_cn
having      COUNT(stt_ctr) = (select COUNT(stt_ctr) from cgtrinh)
;
--CAU 29----------------------------------------------------------
select      distinct a.ten_thau || ' - ' || b.ten_thau cap_thau 
from        cgtrinh a, cgtrinh b
where       a.tinh_thanh = b.tinh_thanh
            and a.ten_thau<b.ten_thau
;
--CAU 30----------------------------------------------------------
select      a.hoten_cn || ' - ' || b.hoten_cn cap_hoten_cn
from        thamgia a, thamgia b
where       a.hoten_cn < b.hoten_cn
group by    a.hoten_cn, b.hoten_cn
having      COUNT(CASE WHEN a.stt_ctr=b.stt_ctr
            AND((a.ngay_tgia between b.ngay_tgia and b.ngay_tgia+b.so_ngay)
                 OR (b.ngay_tgia between a.ngay_tgia and a.ngay_tgia+b.so_ngay))
            THEN a.stt_ctr END) >=2
;
--CAU 22----------------------------------------------------------
select      
from        
where       
;





