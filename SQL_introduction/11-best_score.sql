-- liste tous les enregistrements avec un score >= 10 dans la table second_table de la base de données hbtn_0c_0 --
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;