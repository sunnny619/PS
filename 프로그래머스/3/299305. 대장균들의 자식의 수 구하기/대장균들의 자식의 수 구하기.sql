-- 코드를 작성해주세요
select P.ID, count(C.PARENT_ID)
from ECOLI_DATA as P
    left join ECOLI_DATA as C on P.ID = C.PARENT_ID
group by P.ID
order by P.ID asc