{{
  config(
    materialized = 'ephemeral',
    )
}}

WITH raw_BA AS (
    SELECT *
    FROM {{ source('BUCKSBUDDY', 'raw_BA') }}
)
SELECT 
    TITLE AS POST_TITLE,
    ID AS POST_ID,
    AUTHOR AS POST_AUTHOR,
    SCORE AS POST_SCORE,
    COMMENT_AUTHOR AS COMMENT_AUTHOR,
    COMMENT AS COMMENT
FROM 
    raw_BA