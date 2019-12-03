from utils import to_neotime_date
from queries import create


def add_servidor(tx, row):
    return tx.run(create.servidor, row.to_dict())


def add_empresa(tx, row):
    return tx.run(create.empresa, row.to_dict())


def add_orgao(tx, row):
    return tx.run(create.orgao, row.to_dict())


def add_licitacao(tx, row):
    data = row.to_dict()
    data["dataResultadoCompra"] = to_neotime_date(data["dataResultadoCompra"])
    data["dataAbertura"] = to_neotime_date(data["dataAbertura"])

    return tx.run(create.licitacao, data)


def add_contrato(tx, row):
    data = row.to_dict()

    data["dataAssinaturaContrato"] = to_neotime_date(data["dataAssinaturaContrato"])
    data["dataPublicaçãoDou"] = to_neotime_date(data["dataPublicaçãoDou"])
    data["dataInícioVigência"] = to_neotime_date(data["dataInícioVigência"])
    data["dataFimVigência"] = to_neotime_date(data["dataFimVigência"])

    return tx.run(create.contrato, data)


def add_items_licitacao(tx, row):
    return tx.run(create.itens_licitacao, row.to_dict())


def add_participante_licitacao(tx, row):
    return tx.run(create.participante_licitacao, row.to_dict())


def add_termo_aditivo(tx, row):
    data = row.to_dict()
    data["dataPublicação"] = to_neotime_date(data["dataPublicação"])

    return tx.run(create.termo_aditivo, data)


def add_socio(tx, row):
    return tx.run(create.socio, row.to_dict())

