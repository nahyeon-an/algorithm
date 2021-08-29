USE sqldb;

-- 기본 
-- INSERT INTO table(col1, col2, ...) VALUES (val1, val2, ...)
CREATE TABLE test_tbl1 (id int, userName char(3), age int);
INSERT INTO test_tbl1 VALUES (1, '홍길동', 32);
INSERT INTO test_tbl1(id, userName, age) VALUES (2, '김철수', 24);
INSERT INTO test_tbl1(id, userName) VALUES (3, '태연');
DROP TABLE test_tbl1;

-- Auto Increment 가 지정된 컬럼
-- 해당 열이 없다고 생각하고 insert
-- 또는, null 을 지정
-- Auto Increment 컬럼은 반드시 Primary key 또는 Unique 로 지정되어야 함
CREATE TABLE test_tbl2 (
    id int AUTO_INCREMENT PRIMARY KEY,
    userName char(3),
    age int);
INSERT INTO test_tbl2 VALUES (NULL, '태연', 30);
INSERT INTO test_tbl2 VALUES (NULL, '소희', 29);
INSERT INTO test_tbl2 VALUES (NULL, '지은', 24);

-- 마지막에 입력된 id 값
SELECT LAST_INSERT_ID();

-- auto increment 값을 100으로 변경하기
ALTER TABLE test_tbl2 AUTO_INCREMENT=100;
INSERT INTO test_tbl2 VALUES (NULL, '현진', 28);

DROP TABLE test_tbl2;

-- 초기값 1000, 증가값 3으로 변경
-- 증가값 : 서버 변수의 설정을 바꿈
CREATE TABLE test_tbl3 (
    id int AUTO_INCREMENT PRIMARY KEY,
    userName char(3),
    age int);
ALTER TABLE test_tbl3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;
INSERT INTO test_tbl3 VALUES (NULL, '정연', 30);
INSERT INTO test_tbl3 VALUES (NULL, '나연', 29);
INSERT INTO test_tbl3 VALUES (NULL, '지효', 24);
INSERT INTO test_tbl3 VALUES (NULL, '다현', 26), (NULL, '사나', 26);

DROP TABLE test_tbl3;

-- INSERT INTO ~ SELECT
-- 대량의 데이터 삽입
CREATE TABLE test_tbl4 (id int, fname varchar(50), lname varchar(50));
INSERT INTO test_tbl4 
SELECT emp_no, first_name, last_name 
FROM employees.employees;

DROP TABLE test_tbl4;

CREATE TABLE test_tbl5 
(SELECT emp_no, first_name, last_name FROM employees.employees);

DROP TABLE test_tbl5;

-- 조건부 데이터 삽입
CREATE TABLE member_tbl (SELECT userId, name, addr FROM usertbl LIMIT 3);
ALTER TABLE member_tbl
ADD CONSTRAINT pk_member PRIMARY KEY (userId);
SELECT * FROM member_tbl;

-- 첫번째 데이터 때문에 모든 데이터가 삽입 안 됨
INSERT INTO member_tbl
VALUES ('BBK', '비비코', '미국'), ('SJH', '서장훈', '서울'), ('HJY', '현주엽', '경기');

-- 오류 데이터 제외하고 입력하도록 만들기
INSERT IGNORE INTO member_tbl
VALUES ('BBK', '비비코', '미국'), ('SJH', '서장훈', '서울'), ('HJY', '현주엽', '경기');

-- 키가 중복이면 데이터 업데이트하도록 
INSERT INTO member_tbl
VALUES ('BBK', '비비코', '미국')
ON DUPLICATE KEY UPDATE name='비비코', addr='미국';

-- 키가 중복되지 않으면 일반 Insert
INSERT INTO member_tbl
VALUES ('DJM', '동짜몽', '일본')
ON DUPLICATE KEY UPDATE name='동짜몽', addr='일본';