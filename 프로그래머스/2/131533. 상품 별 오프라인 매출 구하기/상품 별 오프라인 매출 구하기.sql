-- 코드를 입력하세요
select P.PRODUCT_CODE, sum(O.SALES_AMOUNT*P.PRICE) as SALES
from PRODUCT as P 
    join OFFLINE_SALE as O on P.PRODUCT_ID = O.PRODUCT_ID
group by P.PRODUCT_ID
order by SALES desc, P.PRODUCT_CODE asc
