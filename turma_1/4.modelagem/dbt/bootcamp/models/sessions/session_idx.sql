{{
    config(
        materialized='ephemeral'
    )
}}

select
user_domain_id,
event_timestamp,
previous_timestamp,
new_session,
SUM(new_session) OVER (PARTITION BY user_domain_id ORDER BY event_timestamp ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS session_idx
from {{ ref('new_sessions') }}