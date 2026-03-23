--Analysis Queries for Cyber Log ETL Project
--Top malicious Souce IP's

SELECT source_ip, COUNT(*) AS malicious_count
FROM network_events
WHERE is_malicious = true
GROUP BY source_ip
ORDER BY malicious_count DESC
LIMIT 10;

-- Most Targeted Destination IP's
SELECT source_ip, COUNT(*) AS malicious_count
FROM network_events
WHERE is_malicious = true
GROUP BY source_ip
ORDER BY malicious_count DESC
LIMIT 10;

--Malcious vs Benign Events Over Time
SELECT is_malicious, COUNT(*) 
FROM network_events
GROUP BY is_malicious;

--Most Repeat offenders
SELECT source_ip,
       COUNT(*) AS total_events,
       SUM(CASE WHEN is_malicious THEN 1 ELSE 0 END) AS malicious_events,
       SUM(CASE WHEN is_malicious THEN 1 ELSE 0 END)*1.0 / COUNT(*) AS malicious_ratio
FROM network_events
GROUP BY source_ip
HAVING COUNT(*) > 10
ORDER BY malicious_ratio DESC;