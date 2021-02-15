-- join 키워드를 사용하지 않는 방법
select sum(c.population)
from CITY as c, COUNTRY as con
where c.countrycode=con.code and con.continent='Asia';


-- inner join을 사용한 조회
select c.name
from CITY c inner join COUNTRY con
on c.countrycode=con.code
where con.continent='Africa';


-- floor() 함수 : 가장 가까운 정수로 내림
-- join 뒤에 오는 테이블의 컬럼을 참조하려면 group by로 집계해야 함
select con.continent, floor(avg(c.population))
from CITY c inner join COUNTRY con
on c.countrycode=con.code
group by con.continent;
