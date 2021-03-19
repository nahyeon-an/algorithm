use sqldb;

-- 데이터 베이스의 테이블 목록 확인
show tables;

-- 테이블의 모든 데이터 확인
select * from usertbl;
select * from buytbl;

-- select ~ where : 특정 조건을 만족하는 데이터를 조회
-- 조건 연산자 (=, <, >, <=, >=, <>, !=)
-- 관계 연산자 (not, and, or)
select *
from usertbl
where name = '김경호';

select userId, Name
from usertbl
where birthYear >= 1970 and height >=182;

select userId, Name
from usertbl
where birthYear >= 1970 or height >=182;

-- between ~ and : 값의 범위에 따른 조회
-- 연속적인 값을 가지는 컬럼에서만 사용 가능
-- 180 이상 183 이하
select name, height
from usertbl
where height between 180 and 183;

-- in : 이산적인 값이 범위 내에 존재하는지 조회
select name, addr
from usertbl
where addr in ('경남', '전남', '경북');

-- like : 문자열의 내용을 검색
-- % : 글자 수와 상관 없이 매칭
-- _ : 한 글자 매칭 (underscore, underbar)
select name, height
from usertbl
where name like '김%';

select name, height
from usertbl
where name like '_종신';


-- subquery : 서브쿼리, 하위쿼리 (쿼리문 안의 쿼리문)
select name, height
from usertbl
where height > (
  select height from usertbl where name = '김경호'
);

-- any = some : 서브쿼리가 2개 이상의 값을 반환할 때, 여러 값들 중 하나라도 만족하면 데이터 조회
-- 지역이 '경남'인 사람의 키보다 크거나 같은 사람
-- 173, 170보다 작은 조용필을 제외한 나머지 9개의 데이터가 출력됨
-- 결과적으로 키가 170이상인 데이터를 조회
select name, height
from usertbl
where height >= any (
  select height from usertbl where addr = '경남'
);

-- all : 서브쿼리의 여러 값들을 모두 만족하는 데이터를 조회
-- 결과적으로 키 173이상인 데이터를 조회
select name, height
from usertbl
where height >= all (
  select height from usertbl where addr = '경남'
);

-- =any() : in(subquery) 와 동일
select name, height
from usertbl
where height = any (
  select height from usertbl where addr = '경남'
);

-- order by : 정렬, 모든 구문에서 가장 마지막에 나타나야 함
-- 기본 : 오름차순 (ascending)
select name, mDate
from usertbl
order by mDate;

-- 내림차순 정렬
select name, mDate
from usertbl
order by mDate desc;

-- 여러개의 정렬 기준 : 키가 큰 순서로, 키가 같으면 이름 순으로 정렬
select name, height
from usertbl
order by height desc, name asc;

-- distinct : 중복되지 값은 한번만 조회
select distinct addr from usertbl;

-- limit : 출력의 개수를 제한
select *
from usertbl
order by name desc
limit 4;
-- limit 시작 위치, 개수
select *
from usertbl
order by name desc
limit 1, 3;
-- limit 개수 offset 시작 위치
select * from usertbl order by name desc limit 3 offset 1;
