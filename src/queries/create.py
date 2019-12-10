servidor = """
    CREATE (n:Servidor {
        id: $id,
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

socio = """
    CREATE (n:Socio {
        cnpj: $cnpj,
        nome: $nome,
        cpfCnpj: $cpfCnpj,
        tipo: $tipo,
        servidorId: $servidorId
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
        assinadoEm: $dataAssinaturaContrato,
        vigenciaIniciaEm: $dataInícioVigência,
        vigenciaTerminaEm: $dataFimVigência,
        cnpjContratado: $cnpjContratado,
        valorInicial: $valorInicialCompra,
        valorFinal: $valorFinalCompra,
        orgId: $códigoÓrgão,
        ugId: $códigoUg
    })
"""

itens_licitacao = """
    CREATE (n:ItemLicitacao {
        licitacao: $númeroLicitação,
        processo: $númeroProcesso,
        orgId: $códigoÓrgão,
        ugId: $códigoUg,
        cnpjVencedor: $cnpjVencedor,
        descricao: $descrição,
        quantidade: $quantidadeItem,
        valor: $valorItem,
        licitacaoId: $licitacaoId
    })
"""

participante_licitacao = """
    CREATE (n:ParticipanteLicitacao {
        licitacao: $númeroLicitação,
        processo: $númeroProcesso,
        cnpj: $cnpjParticipante,
        venceu: $flagVencedor,
        orgId: $códigoÓrgão,
        ugId: $códigoUg,
        licitacaoId: $licitacaoId
    })
"""

termo_aditivo = """
    CREATE (n:TermoAditivo {
        contrato: $númeroContrato,
        numero: $númeroTermoAditivo,
        publicadoEm: $dataPublicação,
        objeto: $objeto,
        orgId: $códigoÓrgão,
        ugId: $códigoUg
    })
"""

