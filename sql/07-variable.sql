SET @var1 = 5;
SET @var2 = 3;
SET @var3 = 4.25;
SET @var4 = '가수 이름 ==> ';

SELECT @var1;
SELECT @var2 + @var3;

SELECT @var4, name 
FROM usertbl
WHERE height > 180;

-- LIMIT 는 원칙적으로 변수와 함께 사용되지 못함
-- 하지만 다음과 같이 prepare, execute ~ using 구문을 통해 
-- LIMIT @변수 와 같은 효과를 냄
SET @var1 = 3;
PREPARE my_query
FROM 'SELECT name, height FROM usertbl ORDER BY height LIMIT ?';
EXECUTE my_query 
USING @var1;

-- 명시적 형변환
-- 대표적으로 CAST(), CONVERT() 함수가 자주 사용됨
SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수'
FROM buytbl;

SELECT CONVERT(AVG(amount), SIGNED INTEGER) AS '평균 구매 개수'
FROM buytbl;

SELECT AVG(amount) AS '평균 구매 개수'
FROM buytbl;

-- 구분자를 날짜 형식으로 변환
SELECT CAST('2020$12$12' AS DATE);
SELECT CAST('2020/12/12' AS DATE);
SELECT CAST('2020%12%12' AS DATE);
SELECT CAST('2020@12@12' AS DATE);

SELECT num, 
CONCAT(CAST(price AS CHAR(10)), 'X', CAST(amount AS CHAR(4)), '=') AS '단가X수량', 
price*amount AS '구매액'
FROM buytbl;

-- 암시적 형변환
-- 문자 -> 정수
SELECT '100' + '200';
-- 정수 -> 문자
SELECT CONCAT(100, '200');
-- 문자 -> 0
SELECT 0 = 'mega2';
-- 문자 -> 2
SELECT 1 > '2mega';