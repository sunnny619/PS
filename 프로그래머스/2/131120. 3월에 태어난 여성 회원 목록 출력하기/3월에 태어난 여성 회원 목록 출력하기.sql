-- 코드를 입력하세요
select MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH
from MEMBER_PROFILE
where date_format(DATE_OF_BIRTH,"%m") like "03" and GENDER like "W" and TLNO is not null
order by MEMBER_ID asc