# pyright: reportUnknownMemberType=false

import flet as ft


class Taschenrechner(ft.Column):
    result : int
    accus: list[int]=[]
    opperator: str = ""

    def __init__(self):
        super().__init__()

        self.display = ft.TextField(disabled=True, text_align=ft.TextAlign.RIGHT, width=270)
        self.display.text_style = ft.TextStyle(
            size=24, weight=ft.FontWeight.BOLD, font_family="Courier New"
        )
        self.display.value = ""
        self.controls.append(self.display)

        self.controls.append(
            ft.Row(
                [
                    ft.Button(content="7", on_click=self.on_button_click, data="7"),
                    ft.Button(content="8", on_click=self.on_button_click, data="8"),
                    ft.Button(content="9", on_click=self.on_button_click, data="9"),
                ]
            )
        )
        self.controls.append(
            ft.Row(
                [
                    ft.Button(content="4", on_click=self.on_button_click, data="4", bgcolor="green"),
                    ft.Button(content="5", on_click=self.on_button_click, data="5"),
                    ft.Button(content="6", on_click=self.on_button_click, data="6"),
                ]
            )
        )
        self.controls.append(
            ft.Row(
                [
                    ft.Button(content="1", on_click=self.on_button_click, data="1"),
                    ft.Button(content="2", on_click=self.on_button_click, data="2", bgcolor="green"),
                    ft.Button(content="3", on_click=self.on_button_click, data="3"),
                ]
            )
        )
        self.controls.append(
            ft.Row(
                [
                    ft.Button(content="C", on_click=self.on_button_click, data="C"),
                    ft.Button(content="0", on_click=self.on_button_click, data="0"),
                    ft.Button(content="=", on_click=self.on_button_click, data="=")
                ]
            )
        )        
        self.controls.append(
            ft.Row(
                [
                    ft.Button(content="+", on_click=self.on_button_click, data="+"),
                    ft.Button(content="-", on_click=self.on_button_click, data="-"),
                    ft.Button(content="*", on_click=self.on_button_click, data="*"),
                ]
            )
        )


    def on_button_click(self, e: ft.Event[ft.Button]):
        try:
            int( e.control.data)
            self.display.value += e.control.data

            self.accus.append(int(self.display.value))
        except:
            if e.control.data =='+':
                self.display.value = ""
                self.opperator = "+"
                self.resuslt_without_equall()
            elif e.control.data =="=":
                self.display.value = "="
                self.calculate()
            elif e.control.data =="*":
                self.display.value = ""
                self.opperator ="*" 
                self.resuslt_without_equall() 
            elif e.control.data =='-':
                self.display.value = ""
                self.opperator = "-"
                self.resuslt_without_equall()
            elif e.control.data =='C':
                self.display.value = ""
                self.opperator = ""
                self.accus = []
            else:
                self.display.value = f"{e.control.data} not implemented"

    def resuslt_without_equall(self):
        if len(self.accus) == 2:
            self.calculate()
            ...

    def calculate(self):            # gibt auch Ergebnis auf dem Display aus
        try:
            accu2 = self.accus.pop()
            accu1 = self.accus.pop()
            res: int
            if self.opperator == "+":
                res = accu1 + accu2
            elif self.opperator =="*":
                res = accu1 * accu2
            elif self.opperator =="-":
                res = accu1 - accu2
            else:
                res = accu2
            self.result = res
            self.accus.append(res)
            self.display.value = str(self.result)
        except:
            self.display.value = "Error"
        
        
        

def main(page: ft.Page):
    page.title = "Taschenrechner"
    page.add(Taschenrechner())


ft.app(target=main)
