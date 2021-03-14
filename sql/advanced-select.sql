-- case ~ (when - then) ~ else ~ end 문
select
    case
        when (a+b <= c) then "Not A Triangle"
        when (a=b and b=c and c=a) then "Equilateral"
        when (a=b or b=c or c=a) then "Isosceles"
        else "Scalene"
    end
from TRIANGLES;


-- where 구문으로 직업 하나마다 결과값 나오도록 수정
select concat(name, "(", (
    select
    case
      when occupation="Doctor" then "D"
      when occupation="Actor" then "A"
      when occupation="Singer" then "S"
      when occupation="Professor" then "P"
    end
    from OCCUPATIONS
    where name = name
), ")")
from OCCUPATIONS;
select
