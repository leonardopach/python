select 
	c.nome as Cidade,
    c.id  as "ID Cidade",
    p.id as "ID Prefeito",
    p.nome as "Nome Prefeito" ,
    area
from cidade c 
inner join prefeito p 
on c.id = p.cidade_id;

select *
from cidade c 
inner join prefeito p 
on c.id = p.cidade_id;

select *
from cidade c 
left join prefeito p 
on c.id = p.cidade_id;

select *
from cidade c 
right join prefeito p 
on c.id = p.cidade_id;

select *
from cidade c 
left join prefeito p 
on c.id = p.cidade_id union select *
from cidade c 
right join prefeito p 
on c.id = p.cidade_id;

