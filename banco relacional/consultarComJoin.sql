select 
    e.nome as Estado, 
    c.nome as Cidade, 
    regiao as Região 
from estados e, cidade c
where e.id = c.estado_id;


select 
    e.nome as Estado, 
    c.nome as Cidade, 
    regiao as Região 
from estados e 
inner join cidade c on e.id = c.estado_id;

select 
    e.nome as Estado, 
    c.nome as Cidade, 
    regiao as Região 
from estados e 
left outer join cidade c on e.id = c.estado_id;

select 
    e.nome as Estado, 
    c.nome as Cidade, 
    regiao as Região 
from estados e 
right outer join cidade c on e.id = c.estado_id;