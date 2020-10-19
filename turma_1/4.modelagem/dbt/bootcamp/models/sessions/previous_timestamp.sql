{{
    config(
        materialized='ephemeral'
    )
}}

select
user_domain_id,
date_parse(event_timestamp,'%Y-%m-%d %H:%i:%s.%f') as event_timestamp,
LAG(date_parse(event_timestamp,'%Y-%m-%d %H:%i:%s.%f'), 1) OVER (PARTITION BY user_domain_id ORDER BY event_timestamp) as  previous_timestamp
from {{ ref('stg__atomic_events') }}