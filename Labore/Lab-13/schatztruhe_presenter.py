from dataclasses import dataclass

from schatztruhe_modell import ItemStack, ItemTyp, Truhe


@dataclass(frozen=True)
class ItemStackViewModel:
    bezeichnung: str
    anzahl: int
    gewicht: int


class TruhePresenter:
    
    _letzter_fehler: str | None = None

    def __init__(self):
        super().__init__()
        self._model = Truhe(items=[
            ItemStack(ItemTyp("Heiltrank", 5), 1),
            ItemStack(ItemTyp("Rubin", 1), 5)
        ], kapazitaet=16)

    @property
    def kapazitaet(self) -> int:
        return 0
    
    @property
    def gewicht(self) -> int:
        return 0
    
    @property
    def letzter_fehler(self) -> str | None:
        return "Hier könnte Ihre Werbung stehen."

    @property
    def items(self) -> list[ItemStackViewModel]:
        return [
            ItemStackViewModel('foo', 0, 0),
            ItemStackViewModel('bar', 1, 1)
        ]

    
if __name__ == "__main__":
    presenter = TruhePresenter()
    print(presenter.items)