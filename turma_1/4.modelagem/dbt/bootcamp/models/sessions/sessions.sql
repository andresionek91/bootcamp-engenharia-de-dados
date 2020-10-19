{{
    config(
        materialized='table'
    )
}}


select
user_domain_id || cast(session_idx as varchar) as  session_id,
*
from {{ ref('session_idx') }}