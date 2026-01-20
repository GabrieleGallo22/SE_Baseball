import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._nodes = []

    def get_all_years(self):
        return DAO.get_all_years()

    def get_graph_details(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def get_all_nodes(self):
        return self._nodes

    def build_graph(self, anno):
        self._grafo.clear()
        self._nodes = DAO.get_team_of_year(anno)
        self._grafo.add_nodes_from(self._nodes)

        self._idMap = {}
        for t in self._nodes:
            self._idMap[t.id] = t

        for t1 in self._nodes:
            for t2 in self._nodes:
                if t1.id < t2.id:
                    peso = t1.total_salary + t2.total_salary
                    self._grafo.add_edge(t1, t2, weight=peso)

    def get_details(self, team_id):
        team_node = self._idMap[int(team_id)]

        vicini = []
        for neighbor in self._grafo.neighbors(team_node):
            weight =

