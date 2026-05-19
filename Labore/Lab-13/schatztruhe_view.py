
# pyright: reportUnknownMemberType=false
import flet as ft

from schatztruhe_presenter import TruhePresenter

class TruheView(ft.Column):
    
    def __init__(self, presenter: TruhePresenter):
        super().__init__()
        self.presenter = presenter
        self.update_view()

    def update_view(self):
        self.controls.clear()
        self.controls.append(
            ft.Text(f"Gewicht/Kapazität: {self.presenter.gewicht}/{self.presenter.kapazitaet}")
        )

        table = ft.DataTable(
            columns=[
                ft.DataColumn(label=ft.Text("Bezeichnung")),
                ft.DataColumn(label=ft.Text("Anzahl")),
                ft.DataColumn(label=ft.Text("Gewicht"))
            ]
        )
        self.controls.append(table)

        for item in self.presenter.items:
            table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(item.bezeichnung)),
                    ft.DataCell(
                        ft.Row([
                            ft.Button("-", data=item.bezeichnung, on_click=self.on_minus_clicked),
                            ft.Text(str(item.anzahl)),
                            ft.Button("+", data=item.bezeichnung, on_click=self.on_plus_clicked)
                        ])
                    ),
                    ft.DataCell(ft.Text(str(item.gewicht)))
                ])
            )

        if self.presenter.letzter_fehler is not None:
            self.controls.append(ft.Text(f"Fehler: {self.presenter.letzter_fehler}", color=ft.Colors.RED))

    def on_plus_clicked(self, e: ft.Event[ft.Button]):
        # bezeichnung = e.control.data
        # self.presenter.erhoehe_menge(bezeichnung)
        self.update_view()

    def on_minus_clicked(self, e: ft.Event[ft.Button]):
        # bezeichnung = e.control.data
        # self.presenter.verringere_menge(bezeichnung)
        self.update_view()


def main(page: ft.Page):
    page.title = "Schatztruhe"
    presenter = TruhePresenter()
    page.add(TruheView(presenter))

    
if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, port=8080)