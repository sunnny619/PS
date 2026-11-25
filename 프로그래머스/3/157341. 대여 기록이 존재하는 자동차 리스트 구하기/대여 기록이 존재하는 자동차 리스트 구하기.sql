-- 코드를 입력하세요
SELECT H.CAR_ID
from CAR_RENTAL_COMPANY_CAR as C
    join CAR_RENTAL_COMPANY_RENTAL_HISTORY as H on C.CAR_ID = H.CAR_ID
where C.CAR_TYPE like '세단' and H.START_DATE like '%-10-%'
group by H.CAR_ID
order by H.CAR_ID desc