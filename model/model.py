import networkx as nx
from database.dao import DAO

class Model:

    def get_all_years(self):
        return DAO.get_all_years()
    def get_teams(self, anno):
        return DAO.get_teams(anno)

    def __init__(self):
        self._grafo = nx.Graph()
        self._nodes = []

    def build_graph(self, anno):
        self._grafo.clear()
        self._nodes = DAO.get_teams(anno)
        self._grafo.add_nodes_from(self._nodes)

        self._idMap={}
        for s in self._nodes:
            self._idMap[s[0]] = s
            self._grafo.add_node(s)

        for i in range(len(self._nodes)):
            for j in range(i+1, len(self._nodes)):
                u = self._nodes[i]
                v = self._nodes[j]

                salary_u = u[2]
                salary_v = v[2]
                peso = salary_v + salary_u
                self._grafo.add_edge(u, v, weight = peso)

    def get_num_nodes(self):
        return self._grafo.number_of_nodes()
    def get_num_edges(self):
        return self._grafo.number_of_edges()

    def get_sorted_neighbors(self, team_code_selezionato):
        # 1. Recupero il nodo oggetto usando la stringa selezionata
        # Qui entra in gioco la idMap che abbiamo creato prima!
        if team_code_selezionato not in self._idMap:
            return []

        nodo_scelto = self._idMap[team_code_selezionato]

        vicini = []

        # 2. Cerco i vicini nel grafo
        # self._grafo.neighbors(nodo) restituisce i nodi collegati
        for vicino in self._grafo.neighbors(nodo_scelto):
            # Recupero il peso dell'arco
            peso = self._grafo[nodo_scelto][vicino]['weight']
            vicini.append((vicino, peso))

        # 3. Ordino per peso decrescente (dal più grande al più piccolo)
        # x[1] indica che ordiniamo in base al secondo elemento della tupla (il peso)
        vicini.sort(key=lambda x: x[1], reverse=True)

        return vicini


if __name__ == '__main__':
    my_model = Model()
    my_model.build_graph(1999)

    print(f"Nodi totali: {my_model._grafo.number_of_nodes()}")

    # Vediamo i primi 3 nodi inseriti
    for n in list(my_model._grafo.nodes)[:3]:
        print(n)