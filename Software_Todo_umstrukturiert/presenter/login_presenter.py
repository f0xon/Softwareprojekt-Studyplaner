from Software_Todo_umstrukturiert.repo.todo_repo import TodoRepo

class LoginPresenter:
    def __init__(self, repo:TodoRepo):
        self._repo = repo
        self.current_user = None

    def login(self, username: str) -> None:
        # ultra simpel: user existiert immer
        self.current_user = username

    def user_eingeloggt(self)->bool:
        if self.current_user is None:
            return False
        else: 
            return True