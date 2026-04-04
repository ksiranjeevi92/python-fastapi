class Database:
    _instnace = None
    def __new__(cls):
        if cls._instnace is None:
            cls._instnace = super(Database,cls).__new__(cls)
            cls._instnace.connection = "Database connected"
        return cls._instnace
    
a = Database()
b = Database()

print(a is b)
