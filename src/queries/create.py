servidor = """
    CREATE (n:Servidor {
        nome: $nome,
        cpf: $cpf,
        cargo: $descricao_cargo,
        uf: $uf_exercicio,
        vinculo: $situacao_vinculo,
        orgId: $cod_org_exercicio,
        uorgId: $cod_uorg_exercicio
    })
"""

empresa = """
    CREATE (n:Empresa {
        cnpj: $cnpj,
        razaoSocial: $razaosocial,
        nomeFantasia: $nomefantasia,
        tipo: $tipo_pessoa
    })
"""

orgao = """
    CREATE (n:Orgao {
        id: $cod_org_exercicio,
        nome: $org_exercicio,
        orgSuperiorId: $cod_orgsup_exercicio
    })
"""

licitacao = """
    CREATE (n:Licitacao {
        id: $id,
        licitacao: $númeroLicitação,
        processo: $númeroProcesso,
        modalidade: $modalidadeCompra,
        situacao: $situaçãoLicitação,
        municipio: $município,
        resultadoPublicadoEm: $dataResultadoCompra,
        abertoEm: $dataAbertura,
        valor: $valorLicitação,
        orgSuperiorId: $códigoÓrgãoSuperior,
        orgId: $códigoÓrgão,
        ugId: $códigoUg
    })
"""

contrato = """
    CREATE (n:Contrato {
        numero: $númeroDoContrato,
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

itens_licitacao = """
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

participante_licitacao = """
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

termo_aditivo = """
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

socio = """
    CREATE (n:Socio {
        cnpj: $cnpj,
        nome: $nome,
        cpfCnpj: $cpfCnpj,
        tipo: $tipo
    })
"""
