select c.nome, p.assunto, p.data_abertura
from clientes c
join processos p on c.id_cliente = p.id_cliente
where year(p.data_abertura) = 2023 AND c.estado = "SP";