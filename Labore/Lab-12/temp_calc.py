# pyright: reportUnknownMemberType=false

import flet as ft

class TempCalc(ft.Row):

    def __init__(self):
        super().__init__()

        self.celsius_input = ft.TextField(label="Celsius", on_change=self.wandle_c_nach_f)
        self.fahrenheit_input = ft.TextField(label="Fahrenheit", on_change=self.wandle_f_nach_c)

        self.controls.append(self.celsius_input)
        self.controls.append(self.fahrenheit_input)


    def wandle_c_nach_f(self, e: ft.Event[ft.TextField]):
        # guard
        if self.celsius_input.value == '':
            self.celsius_input.bgcolor = None
            self.fahrenheit_input.value = ''
            return
         
        try:
            self.celsius_input.bgcolor = None
            celsius = float(self.celsius_input.value)
            fahrenheit = (celsius * 9/5) + 32
            self.fahrenheit_input.value = f"{fahrenheit:.2f}"
            self.update()
        except: 
            self.celsius_input.bgcolor = "#ffaaaa"
            # self.celsius_input = ft.TextField(label="Celsius", on_change=self.wandle_c_nach_f,bgcolor="#ffaaaa")
            print()



    def wandle_f_nach_c(self, e: ft.Event[ft.TextField]):
         if self.fahrenheit_input.value != '':
            try:
                self.fahrenheit_input.bgcolor = None
                fahrenheit = float(self.fahrenheit_input.value)
                celsius = (fahrenheit * 5/9) - 32
                self.celsius_input.value = f"{celsius:.2f}"
                self.update()
            except: 
                self.fahrenheit_input.bgcolor = "#ffaaaa"
                # self.celsius_input = ft.TextField(label="Celsius", on_change=self.wandle_c_nach_f,bgcolor="#ffaaaa")
                print()
         else:
            self.fahrenheit_input.bgcolor = None
            self.celsius_input.value = ''       

            
def main(page: ft.Page):
    page.title = "Temperatur-Konverter"
    page.add(TempCalc())
    page.add(TempCalc())
    page.add(TempCalc())

ft.app(target=main)