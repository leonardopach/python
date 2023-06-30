CREATE TABLE IF NOT EXISTS empresas (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cnpj INT UNSIGNED,
    PRIMARY KEY (id),
    UNIQUE KEY(cnpj)
);

-- cidades_empresas
CREATE TABLE IF NOT EXISTS empresas_unidades (
    empresas_id INT UNSIGNED NOT NULL,
    cidade_id INT UNSIGNED NOT NULL,
    sede TINYINT(1) NOT NULL,
    PRIMARY KEY (empresas_id, cidade_id),
    FOREIGN KEY (empresas_id) REFERENCES  empresas (id),
    FOREIGN KEY (cidade_id) REFERENCES cidade (id)
);


desc empresas;