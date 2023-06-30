SELECT * from estados;

SELECT nome, sigla, regiao, populacao 
from estados 
WHERE regiao = "Sul";

select nome as "Nome do estado" , regiao, populacao 
from estados
where populacao >= 10
order by populacao 