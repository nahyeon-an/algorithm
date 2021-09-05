CREATE DATABASE moviedb;

USE moviedb;

CREATE TABLE movietbl
(
    movie_id        INT,
    movie_title     VARCHAR(30),
    movie_director  VARCHAR(20),
    movie_star      VARCHAR(20),
    movie_script    LONGTEXT,
    movie_film      LONGBLOB
) DEFAULT CHARSET=utf8mb4;

-- 아무것도 입력되지 않음 
INSERT INTO movietbl 
VALUES (1, '쉰들러 리스트', '스필버그', '리암 니슨', 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Schindler.txt'), 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Schindler.mp4'));
SELECT * FROM movietbl;

-- 시스템 변수, 최대 패킷 크기(= 최대 파일 크기) 조회
SHOW variables LIKE 'max_allowed_packet';
SHOW variables LIKE 'secure_file_priv';

TRUNCATE movietbl

INSERT INTO movietbl 
VALUES (1, '쉰들러 리스트', '스필버그', '리암 니슨', 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Schindler.txt'), 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Schindler.mp4'));

INSERT INTO movietbl 
VALUES (2, '쇼생크 탈출', '프랭크 다라본트', '팀 로빈스', 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Shawshank.txt'), 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Shawshank.mp4'));

INSERT INTO movietbl 
VALUES (3, '라스트 모히칸', '마이클 만', '다니엘 데이 루이스', 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Mohican.txt'), 
LOAD_FILE('/Users/nahyeonan/data/mysql/movies/Mohican.mp4'));

SELECT * FROM movietbl;

-- 내려받기 (txt)  
SELECT movie_script
FROM movietbl
WHERE movie_id=1
INTO OUTFILE '/Users/nahyeonan/data/mysql/movies/schindler_out.txt'
LINES TERMINATED BY '\\n';

-- 동영상
-- DUMPFILE -> 바이너리 파일로 다운
SELECT movie_film
FROM movietbl
WHERE movie_id=3
INTO DUMPFILE '/Users/nahyeonan/data/mysql/movies/schindler_out.mp4';