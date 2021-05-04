-- case ~ (when - then) ~ else ~ end 문
select
    case
        when (a+b <= c) then "Not A Triangle"
        when (a=b and b=c and c=a) then "Equilateral"
        when (a=b or b=c or c=a) then "Isosceles"
        else "Scalene"
    end
from TRIANGLES;


-- name 순으로 정렬, 직업을 ()안에 대문자 첫글자로 넣기
-- 문자열 함수 : concat(), lower(), left()
select concat(name, '(', left(occupation, 1), ')')
from occupations
order by name;
select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.')
from occupations
group by occupation
order by count(occupation), lower(occupation);


-- 문제 : Occupations (더 공부/생각해야 함, 사용자 정의 변수)
-- 사용자 정의 변수
set @d := 0, @p := 0, @s := 0, @a := 0;
select (
  select name
  from occupations
  where occupation = 'Doctor'
), professor name, singer name, actor Name
from occupations;
