# pyright: reportUnknownMemberType=false

from dataclasses import dataclass


@dataclass
class ItemTyp:
    bezeichnung: str
    gewicht: int

    def __repr__(self) -> str:
        return f"{self.bezeichnung} (gew.: {self.gewicht})"


@dataclass
class ItemStack:
    typ: ItemTyp
    anzahl: int

    @property
    def gewicht(self) -> int:
        return self.typ.gewicht * self.anzahl

    def __repr__(self) -> str:
        return f"{self.anzahl}x {self.typ}"


@dataclass
class Truhe:
    items: list[ItemStack]
    kapazitaet: int

    @property
    def gewicht(self) -> int:
        gewicht = 0
        for g in self.items:
            gewicht += g.gewicht
        return gewicht

    def erhoehe_menge(self, item_bezeichnung: str):
        item = self.item_by_bezeichnung(item_bezeichnung)
        if not item:
            raise ValueError("Item nicht in Truhe.")
        if self.gewicht + item.typ.gewicht > self.kapazitaet:
            raise ValueError("Truhe ist voll.")
        item.anzahl += 1

    def verringere_menge(self, item_bezeichnung: str):
        item = self.item_by_bezeichnung(item_bezeichnung)
        if item is None:
            raise ValueError("Item nicht in Truhe.")
        if item.anzahl == 0:
            raise ValueError("Menge kann nicht negativ werden.")
        item.anzahl -= 1

    def item_by_bezeichnung(self, bezeichnung: str) -> ItemStack | None:
        for i in self.items:
            if i.typ.bezeichnung == bezeichnung:
                return i
        return None

    def __repr__(self) -> str:
        return f"Truhe(gew.: {self.gewicht}/{self.kapazitaet} -- {self.items})"


if __name__ == "__main__":
    truhe = Truhe(items=[
            ItemStack(ItemTyp("Heiltrank", 5), 1),
            ItemStack(ItemTyp("Rubin", 1), 5)
    ], kapazitaet=16)
    print(truhe)

    truhe.verringere_menge("Rubin")
    print(truhe)

    truhe.erhoehe_menge("Heiltrank")
    print(truhe)

    truhe.erhoehe_menge("Heiltrank")
    print(truhe)


