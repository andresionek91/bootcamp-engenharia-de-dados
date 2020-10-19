{{
    config(
        materialized='ephemeral'
    )
}}

select
user_domain_id,
event_timestamp,
previous_timestamp,
CASE WHEN date_diff('minute', previous_timestamp, event_timestamp) >= 30 THEN 1 ELSE 0 END as new_session
from {{ ref ('previous_timestamp') }}