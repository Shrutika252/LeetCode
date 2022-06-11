SELECT score, 
DENSE_RANK() OVER (
ORDER BY score desc)
AS 'Rank'
FROM Scores;