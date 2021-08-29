# SQL  

## Contents
#### 02 ~ 03 (SELECT)  
- ANY, SOME, ALL, DISTINCT, LIMIT, OFFSET, BETWEEN, LIKE  
- GROUP BY, SUM(), AVG(), MIN(), MAX(), COUNT(), COUNT(DISTINCT) 중복제외 행의 개수, STDEV() 표준편차, VAR_SAMP() 분산, HAVING, WITH ROLLUP

#### 04 (INSERT)  

#### 05 (UPDATE, DELETE)  

#### 06 (WITH, CTE)  

<br>

## SQL 분류
### DML (데이터 <u>조작</u> 언어)  
대상 : 테이블의 행  
- DML 을 사용하려면 테이블이 정의되어 있어야 한다 !  

SELECT, INSERT, UPDATE, DELETE, 트랜잭션이 발생하는 SQL  
### DDL (데이터 <u>정의</u> 언어)  
DB 개체를 생성/삭제/변경  
CREATE, DROP, ALTER  
트랜잭션을 발생시키지 않는다
- rollback, commit 등은 적용시킬 수 없다  
- 실행 즉시 MySQL 에 적용된다  
### DCL (데이터 <u>제어</u> 언어)  
권한 부여/뺏기  
GRANT, REVOKE, DENY

<br>

## 대용량 테이블의 효율적인 삭제
### DELETE vs. DROP vs. TRUNCATE
DELETE : 트랜잭션 로그를 기록함 (매우 오래 걸림)  
DROP : 테이블 자체를 삭제  
TRUNCATE : 트랜잭션 로그를 기록하지 않는 DELETE  

#### 결론 
: 테이블도 삭제할 때 **DROP**, 테이블은 남기고 내용만 삭제할 때 **TRUNCATE** 가 효율적이다 !  

<br>

## 조건부 데이터 삽입/변경
**100 건의 데이터를 입력하려고 하는데, 첫번째 데이터의 오류 때문에 나머지 데이터가 입력되지 않는다면?**  
오류 데이터는 제외하고 나머지 데이터 삽입하기  
- INSERT **IGNORE** INTO ~  

중복 데이터는 업데이트  
- INSERT ~ **ON DUPLICATE KEY UPDATE** ~  

<br>

## CTE (Common Table Expression)
복잡한 쿼리문을 단순화시키는 데에 사용  
뷰와 용도는 비슷함  
but, <u>CTE와 파생테이블은 구문이 끝나면 소멸됨</u>  
뷰는 계속 존재해서 다른 구문에서도 사용 가능  
아직 정의되지 않은 CTE를 미리 참조하는 것은 불가능  

<br>