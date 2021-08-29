USE sqldb;

-- 기본
-- abc 는 실존하는 테이블이 아님
-- with ~ as () 구문으로 만든 결과 
WITH abc(userId, total)
AS (
    SELECT userId, SUM(price*amount)
    FROM buytbl 
    GROUP BY userId)
SELECT * FROM abc ORDER BY total DESC;

SELECT userId, SUM(price*amount)
FROM buytbl 
GROUP BY userId;

-- 각 지역별로 가장 큰 키 1명을 뽑아서
-- 그들의 키의 평균 
WITH cte_user(addr, maxHeight)
AS (
    SELECT addr, MAX(height)
    FROM usertbl
    GROUP BY addr)
SELECT AVG(maxHeight*1.0) AS '지역별 가장 큰 키의 평균' FROM cte_user;
