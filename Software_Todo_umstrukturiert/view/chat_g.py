class ErzeugeTodoView(ft.Column):

    def __init__(self, presenter: ErzeugeTodoPresenter):
        super().__init__()
        self.presenter = presenter

        self.selected_date = datetime.date.today()

        # ---------------- UI FIELDS ----------------
        self.title = ft.TextField(label="Titel")
        self.notiz = ft.TextField(label="Notiz")

        self.deadline_text = ft.Text(str(self.selected_date))
        self.calendar = ft.RadioGroup(
            content=ft.Row([
                ft.Radio(value=True, label="Ja"),
                ft.Radio(value=False, label="Nein"),
            ])
        )

        self.prio = ft.Dropdown(
            value="keine",
            options=[
                ft.dropdown.Option("keine"),
                ft.dropdown.Option("niedrig"),
                ft.dropdown.Option("mittel"),
                ft.dropdown.Option("hoch"),
            ],
        )

        self.category = ft.RadioGroup(
            value="keine",
            content=ft.Row([
                ft.Radio(value="keine", label="Keine"),
                ft.Radio(value="Studium", label="Studium"),
                ft.Radio(value="Haushalt", label="Haushalt"),
                ft.Radio(value="Freizeit", label="Freizeit"),
            ])
        )

        # ---------------- LOAD DATA ----------------
        self.lade_ui()

        # ---------------- BUILD UI ----------------
        self.controls.append(
            ft.Card(
                content=ft.Column([
                    self.title,
                    self.notiz,
                    self.deadline_text,
                    self.calendar,
                    self.prio,
                    self.category,
                    ft.Button("Speichern", on_click=self.save)
                ])
            )
        )

    # ---------------- LOAD INTO VIEW ----------------
    def lade_ui(self, todo_id: int | None = None):
        data = self.presenter.lade_todo(todo_id) if todo_id else {}

        self.title.value = data.get("Titel", "")
        self.notiz.value = data.get("Notiz", "")
        self.selected_date = data.get("Deadline", self.selected_date)
        self.calendar.value = data.get("Kalender", False)
        self.prio.value = data.get("Priorität", "keine")
        self.category.value = data.get("Kategorie", "keine")

    # ---------------- SAVE ----------------
    def save(self, e):
        self.presenter.save_todo(
            titel=self.title.value,
            notiz=self.notiz.value,
            deadline=self.selected_date,
            calendar=self.calendar.value,
            priority=self.prio.value,
            category=self.category.value,
            extra={}
        )