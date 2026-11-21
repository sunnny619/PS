-- 코드를 입력하세요
select B.WRITER_ID as USER_ID, U.NICKNAME, sum(B.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as B
    join USED_GOODS_USER as U on B.WRITER_ID = U.USER_ID
where B.STATUS like "DONE"
group by B.WRITER_ID
having sum(B.PRICE) >= 700000 
order by TOTAL_SALES asc
