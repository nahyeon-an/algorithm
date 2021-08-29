USE sqldb;

-- 집계함수는 주로 group by 절과 함께 사용되며
-- 데이터를 그룹화하는 데에 사용
-- userId 별로 구매한 물품의 개수
SELECT userId AS '사용자 아이디', sum(amount) AS '총 구매 개수'
FROM buytbl
GROUP BY userId;

-- 구매액 총합
SELECT userId AS '사용자 아이디', sum(price*amount) AS '총 구매액'
FROM buytbl
GROUP BY userId;

-- 전체 구매자의 물품 개수 평균
SELECT AVG(amount) AS '평균 구매 개수'
FROM buytbl;

-- userId 별로 평균 구매 개수
SELECT userId, AVG(amount) AS '평균 구매 개수'
FROM buytbl
GROUP BY userId;

-- 가장 큰 키와 가장 작은 키의 회원 이름 (서브쿼리가 편리한 경우)
SELECT name, height
FROM usertbl
WHERE height = (SELECT MAX(height) FROM usertbl) OR 
height = (SELECT MIN(height) FROM usertbl);

-- 테이블의 전체 사용자 수
SELECT COUNT(*) FROM usertbl;

-- 휴대폰을 가진 사용자 수 조회
-- null 을 가진 것은 제외하고 카운트
SELECT COUNT(mobile1) AS '휴대폰이 있는 사용자'
FROM usertbl;

-- 총 구매액이 1000 이상인 사용자 조회
-- 집계함수는 where 절에 나타날 수 없다. 
-- 집계함수에 대한 조건 = Having 절 (항상 Group by 뒤에 나타남)
SELECT userId AS '사용자', SUM(price*amount) AS '총 구매액' 
FROM buytbl
GROUP BY userId
HAVING SUM(price*amount) > 1000
ORDER BY SUM(price*amount);

-- WITH ROLLUP : 총합, 중간 합계 출력
SELECT num, groupName, SUM(price*amount) AS '비용'
FROM buytbl
GROUP BY groupName, num
WITH ROLLUP;