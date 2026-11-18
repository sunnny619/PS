-- 코드를 입력하세요
select USER_ID, PRODUCT_ID
from ONLINE_SALE
group by USER_ID, PRODUCT_ID
having count(ONLINE_SALE_ID) >= 2
order by USER_ID asc, PRODUCT_ID desc