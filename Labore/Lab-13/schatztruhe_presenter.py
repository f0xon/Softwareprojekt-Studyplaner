from dataclasses import dataclass

from schatztruhe_modell import ItemStack, ItemTyp, Truhe


@dataclass(frozen=True)
class ItemStackViewModel:
    bezeichnung: str
    anzahl: int
    gewicht: int


class TruhePresenter:
    
    _letzter_fehler: str | None = None
    _model: Truhe

    def __init__(self):
        super().__init__()
        self._model = Truhe(items=[
            ItemStack(ItemTyp("Heiltrank", 5), 1),
            ItemStack(ItemTyp("Rubin", 1), 5)
        ], kapazitaet=16)

    @property
    def kapazitaet(self) -> int:
        return self._model.kapazitaet
    
    @property
    def gewicht(self) -> int:
        return self._model.gewicht
    
    @property
    def letzter_fehler(self) -> str | None:
        return self._letzter_fehler

    @property
    def items(self) -> list[ItemStackViewModel]:
        value: list[ItemStackViewModel] = []
        for item in self._model.items:
            value.append(ItemStackViewModel(item.typ.bezeichnung, item.anzahl, item.gewicht))
        return value
        # return [
        #     ItemStackViewModel(self._model.items[0].typ.bezeichnung, self._model.items[0].anzahl, self._model.items[0].gewicht),
        #     ItemStackViewModel(self._model.items[1].typ.bezeichnung, self._model.items[1].anzahl, self._model.items[1].gewicht)
        # ]
  
    def erhoehe_menge(self, bezeichnung: str):
        try:
            self._model.erhoehe_menge(bezeichnung)
            self._letzter_fehler = None
        except ValueError as e:
            self._letzter_fehler = str(e)

    def verringere_menge(self, bezeichnung: str):
        try:
            self._model.verringere_menge(bezeichnung)
            self._letzter_fehler = None
        except ValueError as e:
            self._letzter_fehler = str(e)

    def loesche_item(self, bezeichnung: str):
        try:
            self._model.loesche_item(bezeichnung)
            self._letzter_fehler = None
        except ValueError as e:
            self._letzter_fehler = str(e)

if __name__ == "__main__":
    presenter = TruhePresenter()
    print(presenter.items)