from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

cluster = Cluster()
connection = cluster.connect('lab1')

with open('create.cql') as f:
    txt = f.read()
        statements = txt.split(';')
        for i in statements:
            statements = i.strip()
            if statements != '':
                print('Executing ', statements)
                query = SimpleStatement(statements, consistency_level=ConsistencyLevel.ALL)
                connection.execute(query)
                print(statements,' - done')

with open('work.cql') as f:
    txt = f.read()
        statements = txt.split(';')
        for i in statements:
            statements = i.strip()
            if statements != '':
                print('Executing ', statements)
                query = SimpleStatement(statements, consistency_level=ConsistencyLevel.ONE)
                connection.execute(query)
                print(statements,' - done')


with open('drop.cql') as f:
    txt = f.read()
        statements = txt.split(';')
        for i in statements:
            statements = i.strip()
            if statements != '':
                print('Executing ', statements)
                query = SimpleStatement(statements, consistency_level=ConsistencyLevel.QUORUM)
                connection.execute(query)
                print(statements,' - done')