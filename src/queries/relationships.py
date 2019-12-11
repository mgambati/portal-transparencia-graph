import db

queries = [
    # Orgão realizou uma licitação
    """
        MATCH
            (org:Orgao),
            (licitacao:Licitacao { orgId:org.id })
        CREATE (org)-[:REALIZOU]->(licitacao)
    """,
    # Orgão criou contrato
    """
        MATCH
            (o:Orgao),
            (c:Contrato { orgId:o.id })
        CREATE (o)-[:CRIOU]->(c)
    """,
    # Empresa atuou contrato
    """
        MATCH
            (c:Contrato),
            (e:Empresa { cnpj: c.cnpjContratado })
        CREATE (e)-[:ATUOU]->(c)
    """,
    # Servidor trabalha em orgão
    """
        MATCH
            (s:Servidor),
            (o:Orgao { id: s.orgId })
        CREATE (s)-[:TRABALHA]->(o)
    """,
    # Licitação possui item
    """
        MATCH
            (l:Licitacao),
            (il:ItemLicitacao { licitacaoId: l.id })
        CREATE (l)-[:POSSUI]->(il)
    """,
    # Empresa é sócia de outra empresa
    """
        MATCH
            (e:Empresa),
            (s:Socio { cpfCnpj: e.cnpj }),
            (ex:Empresa { cnpj: s.cnpj })
        CREATE (e)-[:SOCIO { tipo: s.tipo }]->(ex)
    """,
    # Servidor é socio de uma empresa
    """
        MATCH
            (s:Socio),
            (sv:Servidor { id: s.servidorId }),
            (e:Empresa { cnpj: s.cnpj })
        CREATE (sv)-[:SOCIO { tipo: s.tipo }]->(e)
    """,
    # Empresa participou de licitação
    """
        MATCH
            (pl:ParticipanteLicitacao),
            (l:Licitacao { id: pl.licitacaoId }),
            (e:Empresa { cnpj: pl.cnpj })
        CREATE (e)-[:PARTICIPOU { venceu: pl.venceu }]->(l)
    """,
    # Contrato possui termos aditivos
    """
        MATCH
            (ta:TermoAditivo),
            (c:Contrato { id: ta.contratoId })
        CREATE (c)-[:POSSUI]->(ta)
    """,
]


def create_relationships():
    print("Creating relationships...")
    with db.connect() as driver:
        with driver.session() as session:
            tx = session.begin_transaction()
            for query in queries:
                tx.run(query)
            tx.commit()
