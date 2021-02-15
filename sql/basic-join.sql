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


-- IMPORTANT !!
-- on 이 없는 Join 쿼리 : 두 테이블에 직접적인 컬럼 연결이 없을 때
-- mark between min and max : mark >= min and mark <= max
select if(grade<8, null, name), grade, marks
from Students inner join Grades
where marks between min_mark and max_mark
order by grade desc, name;


-- group by, having
-- join 시 어떤 테이블이 메인인지 잘 판단해야 함
select h.hacker_id, h.name
from Submissions s
inner join Hackers h on s.hacker_id=h.hacker_id
inner join Challenges c on s.challenge_id=c.challenge_id
inner join Difficulty d on c.difficulty_level=d.difficulty_level
where s.score=d.score and c.difficulty_level=d.difficulty_level
group by h.hacker_id, h.name
having count(s.hacker_id)>1
order by count(s.hacker_id) desc, s.hacker_id;
