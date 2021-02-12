-- 이중 select 쿼리문 = 괄호 ()로 묶어서 넣는다.
-- 글자의 길이를 반환하는 함수 : length()
select city, length(city)
from STATION
where length(city)=(
    select min(length(city)) from STATION
)
order by city
limit 1;


-- 특정 글자로 시작하는 도시 이름 검색
select distinct city
from STATION
where city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%';


-- 첫번째 글자와 마지막 글자 모두 모음인 도시 이름 찾기
-- 소문자로 바꾸는 함수 : lower()
-- (첫 글자가 모음인 경우) and (마지막 글자가 모음인 경우)
select distinct city
from STATION
where (
    (lower(city) like 'a%' or lower(city) like 'e%' or lower(city) like 'i%' or lower(city) like 'o%' or lower(city) like 'u%')
    and
    (lower(city) like '%a' or lower(city) like '%e' or lower(city) like '%i' or lower(city) like '%o' or lower(city) like '%u')
);


-- 모음으로 시작하지 않는 도시 이름 출력 : not 키워드 사용법
select distinct city
from STATION
where not (city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%');
