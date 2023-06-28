update estados
set nome = "Maranhão"
where sigla = "MA"


select `nome`, populacao from estados
where sigla = "PR"

update estados
set nome = "Paraná",
    populacao = 2.9
where sigla = "PR"

select
    est.nome,
    sigla,
    populacao
from estados est
where sigla = "PR"