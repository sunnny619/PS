-- 코드를 입력하세요
select A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, sum(total*B.P) as TOTAL_SALES
from AUTHOR as A
    join 
        (
            SELECT B.BOOK_ID, B.CATEGORY, B.AUTHOR_ID, sum(SALES) as total, B.PRICE as P
            from BOOK as B
                join BOOK_SALES as BS 
                on B.BOOK_ID = BS.BOOK_ID
            where BS.SALES_DATE like "2022-01%"
            group by BS.BOOK_ID
            order by B.BOOK_ID asc
        ) as B on A.AUTHOR_ID = B.AUTHOR_ID
group by A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
order by A.AUTHOR_ID asc, B.CATEGORY desc
