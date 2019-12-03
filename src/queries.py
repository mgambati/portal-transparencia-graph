from utils import to_neotime_date


def create_servidor_node(tx, row):
    query = """
        CREATE (n:Servidor {
            nome: $nome,
            cpf: $cpf,
            cargo: $descricao_cargo,
            funcao: $funcao,
            jornadaDeTrabalho: $jornada_de_trabalho,
            orgExercicioId: $cod_org_exercicio,
            orgLotacaoId: $cod_org_lotacao,
            uorgExercicioId: $cod_uorg_exercicio,
            uorgLotacaoId: $cod_uorg_lotacao,
            regimeJuridico: $regime_juridico,
            ufExercicio: $uf_exercicio,
            situacaoVinculo: $situacao_vinculo
        })
        """

    return tx.run(query, row.to_dict())


def create_empresa_node(tx, row):
    query = """
        CREATE (n:Empresa {
            cnpj: $cnpj,
            razaoSocial: $razaosocial,
            nomeFantasia: $nomefantasia,
            codCnae: $cod_cnae,
            codNaturezaJuridica: $cod_natjuridica,
            tipo: $tipo_pessoa
        })
        """

    return tx.run(query, row.to_dict())


def create_orgao_node(tx, row):
    query = """
        CREATE (n:Orgao {
            id: $cod_org_exercicio,
            nome: $org_exercicio,
            orgSuperiorId: $cod_orgsup_exercicio
        })
        """

    return tx.run(query, row.to_dict())


def create_licitacao_node(tx, row):
    query = """
        CREATE (n:Licitacao {
            numeroLicitacao: $númeroLicitação,
            numeroProcesso: $númeroProcesso,
            modalidadeCompra: $modalidadeCompra,
            situacaoLicitacao: $situaçãoLicitação,
            orgSuperiorId: $códigoÓrgãoSuperior,
            orgId: $códigoÓrgão,
            ugId: $códigoUg,
            municipio: $município,
            dataResultadoCompra: $dataResultadoCompra,
            dataAbertura: $dataAbertura,
            valor: $valorLicitação
        })
        """
    data = row.to_dict()
    data["dataResultadoCompra"] = to_neotime_date(data["dataResultadoCompra"])
    data["dataAbertura"] = to_neotime_date(data["dataAbertura"])

    return tx.run(query, data)


def create_contrato_node(tx, row):
    query = """
        CREATE (n:Contrato {
            numeroDoContrato: $númeroDoContrato,
            objeto: $objeto,
            fundamentoLegal: $fundamentoLegal,
            modalidadeCompra: $modalidadeCompra,
            situacaoContrato: $situaçãoContrato,
            orgSuperiorId: $códigoÓrgãoSuperior,
            orgId: $códigoÓrgão,
            ugId: $códigoUg,
            dataAssinaturaContrato: $dataAssinaturaContrato,
            dataPublicacaoDou: $dataPublicaçãoDou,
            dataInicioVigencia: $dataInícioVigência,
            dataFimVigencia: $dataFimVigência,
            cnpjContratado: $cnpjContratado,
            valorInicialCompra: $valorInicialCompra,
            valorFinalCompra: $valorFinalCompra
        })
        """
    data = row.to_dict()

    data["dataAssinaturaContrato"] = to_neotime_date(data["dataAssinaturaContrato"])
    data["dataPublicaçãoDou"] = to_neotime_date(data["dataPublicaçãoDou"])
    data["dataInícioVigência"] = to_neotime_date(data["dataInícioVigência"])
    data["dataFimVigência"] = to_neotime_date(data["dataFimVigência"])

    return tx.run(query, data)


def create_items_licitacao_node(tx, row):
    query = """
        CREATE (n:ItemLicitacao {
            numeroLicitacao: $númeroLicitação,
            numeroProcesso: $númeroProcesso,
            orgId: $códigoÓrgão,
            ugId: $códigoUg,
            cnpjVencedor: $cnpjVencedor,
            descricao: $descrição,
            quantidadeItem: $quantidadeItem,
            valorItem: $valorItem
        })
        """
    return tx.run(query, row.to_dict())


def create_participante_licitacao_node(tx, row):
    query = """
        CREATE (n:ParticipanteLicitacao {
            numeroLicitacao: $númeroLicitação,
            numeroProcesso: $númeroProcesso,
            orgId: $códigoÓrgão,
            ugId: $códigoUg,
            codigoItemCompra: $códigoItemCompra,
            cnpjParticipante: $cnpjParticipante,
            flagVencedor: $flagVencedor
        })
    """

    return tx.run(query, row.to_dict())


def create_termo_aditivo_node(tx, row):
    query = """
        CREATE (n:TermoAditivo {
            numeroContrato: $numeroContrato,
            orgSuperiorId: $códigoÓrgãoSuperior,
            orgId: $códigoÓrgão,
            ugId: $códigoUg,
            numeroTermoAditivo: $númeroTermoAditivo,
            dataPublicacao: $dataPublicação,
            objeto: $objeto
        })
    """
    data = row.to_dict()
    data["dataPublicação"] = to_neotime_date(data["dataPublicação"])

    return tx.run(query, data)


def create_socio_node(tx, row):
    query = """
        CREATE (n:Socio {
            cnpj: $cnpj,
            nome: $nome,
            cpfCnpj: $cpfCnpj,
            tipo: $tipo
        })
    """

    return tx.run(query, row.to_dict())

