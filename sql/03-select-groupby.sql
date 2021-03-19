use sqldb;

-- 집계함수는 주로 group by 절과 함께 사용되며
-- 데이터를 그룹화하는 데에 사용
select userId, sum(amount)
from buytbl
group by userId;
