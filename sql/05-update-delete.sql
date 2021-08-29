USE sqldb;

CREATE TABLE test_tbl4 (id int, fname varchar(50), lname varchar(50));
INSERT INTO test_tbl4 
SELECT emp_no, first_name, last_name 
FROM employees.employees;

-- 기본 : UPDATE 테이블명 SET ~ WHERE ~
-- 기존의 값을 변경
-- where 절을 생략하면 전체 행이 변경됨
UPDATE test_tbl4
SET lname = '없음'
WHERE fname = 'Kyoichi';

-- price 컬럼 데이터 전체를 1.5배
UPDATE buytbl 
SET price = 1.5*price;

-- 기본 : DELETE FROM 테이블명 WHERE ~
-- 행 단위로 삭제
DELETE FROM test_tbl4
WHERE fname='Aamer';

-- 상위 5개만 삭제
DELETE FROM test_tbl4
WHERE fname='Kyoichi'
LIMIT 5;