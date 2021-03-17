"""py2neo使用"""

from py2neo import Graph, Node, Relationship
from py2neo.matching import NodeMatcher, RelationshipMatcher
from utils import printer

graph = Graph('bolt://localhost:7687', username='neo4j', password='123456')

print(graph.schema.node_labels)  # 节点的类型
print(graph.schema.relationship_types)  # 关系的类型


def create_node():
    """创建节点"""
    transaction = graph.begin()  # 开始一个 transaction
    node1 = Node("Person", name='Jesse')
    transaction.create(node1)
    transaction.commit()


def create_relationship():
    """创建节点和关系"""
    a_1 = Node("Person", name='张三')
    b_1 = Node("Person", name='李四')
    r_1 = Relationship(a_1, 'KNOWS', b_1)
    _s = a_1 | b_1 | r_1
    graph.create(_s)


@printer
def match():
    """这里的节点是正常的，它有两个属性name和age
    name是Liz age是34
    match("Person").where(age=34).first() 正常
    match("Person").where(name='Liz').first() 正常
    match("Person", name="Liz").first() 正常
    match("Person", age=34).first() 正常
    match("Person", age=34).where(name="Liz").first() None
    match("Person", name="Liz").where(age=34).first() None
    """
    matcher_1 = NodeMatcher(graph)
    matcher_2 = RelationshipMatcher(graph)
    # TODO: 这里的 age 属性使用后返回结果为 None
    node = matcher_1.match("Person", name="Liz").where(age=34).first()
    relation = matcher_2.match(r_type='FRIENDS')
    return list(relation), node, type(relation)


if __name__ == "__main__":
    match()
