SELECT 
  location_city,
  COUNT(*) AS trip_count,
FROM {{ ref('stg_bike_data') }}
GROUP BY location_city
