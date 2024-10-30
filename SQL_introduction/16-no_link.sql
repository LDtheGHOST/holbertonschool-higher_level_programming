-- liste tous les enregistrements de la table second_table de la base de données hbtn_0c_0 -
SELECT score, TRIM(name) AS name
FROM second_table
WHERE name IS NOT NULL AND TRIM(name) != ''
ORDER BY score DESC;