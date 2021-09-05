-- IF (수식, 참, 거짓)
SELECT IF (100 > 200, '참이다', '거짓이다');

-- IFNULL (수식1, 수식2)
-- 수식1 == NULL, 수식1
-- 수식1 != NULL, 수식2
SELECT IFNULL (NULL, '널 값'), IFNULL (100, '널 값');

-- NULLIF (수식1, 수식2)
-- 수식1 == 수식2, NULL 
-- 수식1 != 수식2, 수식1
SELECT NULLIF(100, 100), NULLIF(200, 100);

-- CASE ~ WHEN ~ ELSE ~ END
SELECT CASE 10
        WHEN 1 THEN '일'
        WHEN 5 THEN '오'
        WHEN 10 THEN '십'
        ELSE '모름'
END AS '출력 열의 별칭';

-- ASCII (아스키 코드 문자) -> 아스키 코드 값
-- CHAR (숫자) -> 아스키 코드 문자
SELECT ASCII('A'), CHAR(65);

-- BIT_LENGTH() -> 비트 크기, 문자 크기
-- CHAR_LENGTH() -> 문자의 개수 
-- LENGTH() -> Byte 수
-- 한 글자당 영어=1Byte, 한글=3Byte
SELECT BIT_LENGTH('abc'), CHAR_LENGTH('abc'), LENGTH('abc');
SELECT BIT_LENGTH('가나다'), CHAR_LENGTH('가나다'), LENGTH('가나다');

-- CONCAT_WS(구분자, 문자열1, 문자열2, ...)
-- 구분자를 이용하여 문자열들을 연결
SELECT CONCAT_WS('/', '2021', '09', '01');

-- ELT()
-- FIELD()
-- FIND_IN_SET()
-- INSTR()
-- LOCATE()


-- FORMAT() : 숫자를 소수점 아래 자릿수까지 표현 (반올림)
SELECT FORMAT(123456.123456, 4);

-- BIN() : 2진수
-- HEX() : 16진수
-- OCT() : 8진수
SELECT BIN(31), HEX(31), OCT(31);

-- INSERT() : 위치부터 길이만큼 삭제하고 문자열을 끼워 넣음
SELECT INSERT('abcdefghi', 3, 4, '%%%'), INSERT('abcdefghi', 3, 2, '##');

-- LEFT()
-- RIGHT()
-- 방향에서 해당 문자열 길이만큼 반환 
SELECT LEFT('abcdefghi', 3), RIGHT('abcdefghi', 3);

-- UPPER()
-- LOWER()
SELECT UPPER('abcdEFGHI'), LOWER('abcdEFGHI');

-- LPAD()
-- RPAD()
-- 길이만큼 늘린 후 빈 곳을 채움
SELECT LPAD('Hi', 5, '#'), RPAD('Hi', 5, '**');

-- LTRIM() : 왼쪽 공백 제거 
-- RTRIM() : 오른쪽 공백 제거
SELECT LTRIM('     hello'), RTRIM('hello     ');

-- TRIM() : 앞뒤 공백 모두 제거 
-- TRIM(방향 타겟문자열 FROM 원래문자열)
SELECT TRIM('      hello    '), TRIM(BOTH 'a' FROM 'aaahello world! aaaaa');

-- REPEAT(str, 횟수) : str을 횟수만큼 반복 
SELECT REPEAT('count', 3);

-- REPLACE(str, org, new) : str에서 org를 찾아서 new로 변경
SELECT REPLACE('This is my SQL study notebook.', 'SQL', 'MySQL');

-- REVERSE()
SELECT REVERSE('MySQL');

-- SPACE()
SELECT CONCAT('Hello', SPACE(3), 'World!');

-- SUBSTRING(str, start, len) : str의 start 부터 len 길이까지 반환
SELECT SUBSTRING('Python', 3, 2);

-- SUBSTRING_INDEX(str, 구분자, 횟수) : str에서 구분자가 횟수번째까지 나오면 그 이후는 버림
SELECT SUBSTRING_INDEX('developers.kakao.com', '.', 2), SUBSTRING_INDEX('developers.kakao.com', '.', -2);


-- 수학
-- ABS()
SELECT ABS(-100);

-- ACOS(), ASIN(), ATAN(), ATAN2()
-- SIN(), COS(), TAN()

-- CEILING(), FLOOR(), ROUND() : 올림, 내림, 반올림
SELECT CEILING(4.7), FLOOR(4.7), ROUND(4.7);

-- CONV(num, org, new) : num을 org 진수에서 new 진수로 변환, 계산
SELECT CONV('AA', 16, 2), CONV(100, 10, 8);

-- DEGREES(), RADIANS(), PI()
SELECT DEGREES(PI()), RADIANS(180);

-- EXP(), LN(), LOG(), LOG2(), LOG10()

-- MOD()
SELECT MOD(157, 10), 157 % 10, 157 MOD 10;

-- POW(), SQRT()
SELECT POW(2, 3), SQRT(9);

-- RAND() : 0이상 1미만의 실수
SELECT RAND(), FLOOR(1 + (RAND() * (6-1)));

-- SIGN() : 양수 -> 1, 0 -> 0, 음수 -> -1 반환
SELECT SIGN(100), SIGN(0), SIGN(-100.123);

-- TRUNCATE(num, idx) : num을 소수점 기준으로 idx까지 구하고 나머지는 버림
SELECT TRUNCATE(12345.12345, 2), TRUNCATE(12345.12345, -2);


-- 날짜, 시간
-- ADDDATE(), SUBDATE()
SELECT ADDDATE('2025-01-01', INTERVAL 31 DAY), ADDDATE('2025-01-01', INTERVAL 1 MONTH);
SELECT SUBDATE('2025-01-01', INTERVAL 31 DAY), SUBDATE('2025-01-01', INTERVAL 1 MONTH);

-- ADDTIME(), SUBTIME()
SELECT ADDTIME('2025-01-01 23:59:59', '1:1:1'), ADDTIME('15:00:00', '2:10:10');
SELECT SUBTIME('2025-01-01 23:59:59', '1:1:1'), SUBTIME('15:00:00', '2:10:10');

-- CURDATE(), CURTIME(), NOW(), SYSDATE()
SELECT CURDATE(), CURTIME(), NOW(), SYSDATE();

-- YEAR(), MONTH(), DAY(), HOUR(), MINUTE(), SECOND(), MICROSECOND()
SELECT YEAR(CURDATE()), MONTH(CURDATE()), DAYOFMONTH(CURDATE());
SELECT HOUR(CURTIME()), MINUTE(CURRENT_TIME()), SECOND(CURRENT_TIME), MICROSECOND(CURRENT_TIME);

-- DATE(), TIME()
SELECT DATE(NOW()), TIME(NOW());

-- DATEDIFF(), TIMEDIFF()

-- DAYOFWEEK(), MONTHNAME(), DAYOFYEAR()

-- LAST_DAY()

-- MAKEDATE()

-- MAKETIME()

-- PERIOD_ADD(), PERIOD_DIFF()

-- QUARTER()

-- TIME_TO_SEC()


-- 시스템 함수
-- USER(), DATABASE()
SELECT USER(), DATABASE();

-- FOUND_ROWS()

-- ROW_COUNT()

-- VERSION()

-- SLEEP()