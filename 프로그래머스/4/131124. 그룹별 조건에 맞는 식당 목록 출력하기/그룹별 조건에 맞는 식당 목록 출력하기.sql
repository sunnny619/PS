select M.MEMBER_NAME, R.REVIEW_TEXT, R.REVIEW_DATE

from MEMBER_PROFILE as M
 join REST_REVIEW as R on M.MEMBER_ID = R.MEMBER_ID
where R.MEMBER_ID =(
        select MEMBER_ID
        from REST_REVIEW
        group by MEMBER_ID
        order by count(*) desc
        limit 1
    )
    

order by REVIEW_DATE asc, REVIEW_TEXT asc