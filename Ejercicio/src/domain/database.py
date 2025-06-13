class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Conectando a la base de datos...")
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._data = []
        return cls._instance

    def add_user(self, user):
        self._data.append(user)

    def list_users(self):
        return self._data
