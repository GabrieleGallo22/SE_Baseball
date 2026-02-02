import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def populate_dd(self):
        years = self._model.get_all_years()
        for y in years:
            self._view.dd_anno.options.append(ft.dropdown.Option(y))
        self._view.page.update()

    def handle_search_teams(self, e):
        anno_str = self._view.dd_anno.value
        if anno_str is None:
            self._view.show_alert("seleziona un anno")
            return
        anno = int(anno_str)


        squadre = self._model.get_teams(anno)
        self._view.txt_out_squadre.controls.clear()

        if len(squadre) == 0:
            self._view.show_alert("nessuna squadra trovata")
            return

        self._view.txt_out_squadre.controls.append(ft.Text(f"Trovate {len(squadre)} squadre nel {anno}"))

        for s in squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{s[1]}"))

        self._view.dd_squadra.options.clear()
        for s in squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(s[0], s[1]))
        self._view.page.update()

    def handle_crea_grafo(self, e):
        anno_str = self._view.dd_anno.value
        if anno_str is None:
            self._view.show_alert("seleziona un anno")
            return
        anno = int(anno_str)

        self._model.build_graph(anno)
        n_nodi = self._model.get_num_nodes()
        n_edges = self._model.get_num_edges()

        self._view.txt_risultato.controls.clear()
        self._view.txt_risultato.controls.append(ft.Text(f"{n_nodi} nodi e archi {n_edges}"))
        self._view.page.update()


    def handle_dettagli(self, e):
        # 1. Prendo la squadra selezionata (che è il codice, es. "NYY")
        team_code = self._view.dd_squadra.value

        if team_code is None:
            self._view.show_alert("Seleziona una squadra!")
            return

        # 2. Chiedo al model i vicini ordinati
        vicini = self._model.get_sorted_neighbors(team_code)

        # 3. Stampo i risultati
        self._view.txt_risultato.controls.clear()
        self._view.txt_risultato.controls.append(ft.Text(f"Dettagli per la squadra {team_code}:"))

        for v in vicini:
            # v è una tupla (nodo_vicino, peso)
            # nodo_vicino è a sua volta una tupla (code, nome, salario) -> v[0][1] è il nome
            self._view.txt_risultato.controls.append(
                ft.Text(f"{v[0][1]} - Peso: {v[1]}")
            )

        self._view.page.update()

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO

