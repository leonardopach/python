select * from cidade;

insert into cidade (nome, area ,estado_id)
values("Campinas", 795, 24);

insert into cidade (nome, area ,estado_id)
values("Niteroi", 795, 23);

insert into cidade 
    (nome, area ,estado_id)
values (
    "Caruaru", 920.6,
    (select id from estados where sigla = "PE")
)