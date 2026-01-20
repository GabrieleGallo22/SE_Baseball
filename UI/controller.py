import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def fillDD(self):
        years = self._model.get_all_years()
        years_options=[]
        for y in years:
            nuova_opzione = ft.dropdown.Option(y)
            years_options.append(nuova_opzione)

        self._view.dd_anno.options = years_options
        self._view.update()

    def handle_crea_grafo(self, e):
        anno_scelto = self._view.dd_anno.value
        if anno_scelto is None:
            self._view.create_alert("Seleziona un anno!")
            return

        # 1. Creo il grafo
        self._model.build_graph(int(anno_scelto))

        # 2. Stampo i risultati
        n_nodi, n_archi = self._model.get_graph_details()
        self._view.txt_risultato.controls.clear()
        self._view.txt_risultato.controls.append(
            ft.Text(f"Grafo creato.\nNumero di vertici: {n_nodi}\nNumero di archi: {n_archi}"))

        # --- PARTE NUOVA: RIEMPIO LA TENDINA SQUADRE ---

        # 3. Recupero le squadre (i nodi)
        squadre = self._model.get_all_nodes()

        # 4. Creo le opzioni per la tendina
        # Uso 'key' per l'ID e 'text' per il nome visualizzato
        squadre_options = []
        for s in squadre:
            squadre_options.append(ft.dropdown.Option(key=s.id, text=s.name))

        # 5. Riempio la tendina (IMPORTANTE: controlla come hai chiamato la tendina nella View!)
        # Io ipotizzo si chiami dd_squadra, se si chiama diversamente cambia il nome qui sotto.
        self._view.dd_squadra.options = squadre_options

        self._view.update()

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO