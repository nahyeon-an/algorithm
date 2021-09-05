USE sqldb;

-- JSON_OBJECT(), JSON_ARRAY() : JSON으로 변환
SELECT JSON_OBJECT('name', name, 'height', height) AS 'JSON 값'
FROM usertbl
WHERE height >= 180;

SET @json='{"usertbl":
    [
        {"name":"임재범", "height":182},
        {"name":"이승기", "height":182},
        {"name":"성시경", "height":186}
    ]
}';

-- 문자열이 json 형식을 만족하면 1, 아니면 0 반환
SELECT JSON_VALID(@json) AS JSON_VALID;

-- '성시경' 문자열의 위치를 반환
-- one : 처음 매치되는 하나만 반환
-- all : 매치되는 모든 것을 반환
SELECT JSON_SEARCH(@json, 'one', '성시경') AS JSON_SEARCH;

-- 지정된 위치의 값을 추출, 반환
SELECT JSON_EXTRACT(@json, '$.usertbl[2].name') AS JSON_EXTRACT;

-- 새로운 값을 추가
SELECT JSON_INSERT(@json, '$.usertbl[0].mDate', '2009-09-09') AS JSON_INSERT;

-- 값을 변경
SELECT JSON_REPLACE(@json, '$.usertbl[0].name', '홍길동') AS JSON_REPLACE;

-- 항목 삭제
SELECT JSON_REMOVE(@json, '$.usertbl[0]') AS JSON_REMOVE;