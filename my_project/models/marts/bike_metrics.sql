SELECT
    location_city,
    location_country,
    COUNT(DISTINCT id) AS total_systems,
    COUNT(*) AS record_count,
    AVG(location_latitude) AS avg_latitude,
    AVG(location_longitude) AS avg_longitude
FROM {{ ref('stg_bike_data') }}
GROUP BY location_city, location_country
