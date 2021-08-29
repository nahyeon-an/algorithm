USE sqldb;

-- 데이터 베이스의 테이블 목록 확인
SHOW TABLES;

-- 테이블의 모든 데이터 확인
SELECT * FROM usertbl;
SELECT * FROM buytbl;

-- select ~ where : 특정 조건을 만족하는 데이터를 조회
-- 조건 연산자 (=, <, >, <=, >=, <>, !=)
-- 관계 연산자 (not, and, or)
SELECT *
FROM usertbl
WHERE name = '김경호';

SELECT userId, Name
FROM usertbl
WHERE birthYear >= 1970 AND height >=182;

SELECT userId, Name
FROM usertbl
WHERE birthYear >= 1970 OR height >=182;

-- between ~ and : 값의 범위에 따른 조회
-- 연속적인 값을 가지는 컬럼에서만 사용 가능
-- 180 이상 183 이하
SELECT name, height
FROM usertbl
WHERE height BETWEEN 180 AND 183;

-- in : 이산적인 값이 범위 내에 존재하는지 조회
SELECT name, addr
FROM usertbl
WHERE addr IN ('경남', '전남', '경북');

-- like : 문자열의 내용을 검색
-- % : 글자 수와 상관 없이 매칭
-- _ : 한 글자 매칭 (underscore, underbar)
SELECT name, height
FROM usertbl
WHERE name LIKE '김%';

SELECT name, height
FROM usertbl
WHERE name LIKE '_종신';


-- subquery : 서브쿼리, 하위쿼리 (쿼리문 안의 쿼리문)
SELECT name, height
FROM usertbl
WHERE height > (
  SELECT height FROM usertbl WHERE name = '김경호'
);

-- any = some : 서브쿼리가 2개 이상의 값을 반환할 때, 여러 값들 중 하나라도 만족하면 데이터 조회
-- 지역이 '경남'인 사람의 키보다 크거나 같은 사람
-- 173, 170보다 작은 조용필을 제외한 나머지 9개의 데이터가 출력됨
-- 결과적으로 키가 170이상인 데이터를 조회
SELECT name, height
FROM usertbl
WHERE height >= ANY (
  SELECT height FROM usertbl WHERE addr = '경남'
);

SELECT height FROM usertbl WHERE addr = '경남';

-- all : 서브쿼리의 여러 값들을 모두 만족하는 데이터를 조회
-- 결과적으로 키 173이상인 데이터를 조회
SELECT name, height
FROM usertbl
WHERE height >= ALL (
  SELECT height FROM usertbl WHERE addr = '경남'
);

-- =any() : in(subquery) 와 동일
SELECT name, height
FROM usertbl
WHERE height = ANY (
  SELECT height FROM usertbl WHERE addr = '경남'
);

SELECT name, height
FROM usertbl
WHERE height IN (
  SELECT height FROM usertbl WHERE addr = '경남'
);

-- order by : 정렬, 모든 구문에서 가장 마지막에 나타나야 함
-- 기본 : 오름차순 (ascending)
SELECT name, mDate
FROM usertbl
ORDER BY mDate;

-- 내림차순 정렬
SELECT name, mDate
FROM usertbl
ORDER BY mDate DESC;

-- 여러개의 정렬 기준 : 키가 큰 순서로, 키가 같으면 이름 순으로 정렬
SELECT name, height
FROM usertbl
ORDER BY height DESC, name ASC;

-- distinct : 중복되지 값은 한번만 조회
SELECT DISTINCT addr 
FROM usertbl;

-- limit : 출력의 개수를 제한
SELECT *
FROM usertbl
ORDER BY name DESC
LIMIT 4;
-- limit 시작 위치, 개수
SELECT *
FROM usertbl
ORDER BY name DESC
LIMIT 1, 3;
-- limit 개수 offset 시작 위치
SELECT * 
FROM usertbl 
ORDER BY name DESC 
LIMIT 3 OFFSET 1;

-- 테이블 복사
CREATE TABLE buytbl2 (SELECT * FROM buytbl);
SELECT *
FROM buytbl2;
DROP TABLE buytbl2;

-- 일부 컬럼만 복사
CREATE TABLE buytbl3 (SELECT userId, prodName FROM buytbl);
SELECT *
FROM buytbl3;
DROP TABLE buytbl3;