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