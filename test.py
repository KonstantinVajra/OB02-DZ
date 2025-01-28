from zoneinfo import reset_tzpath


class User():
    def __init__(self, id: int, name: str, level: str = "user"):
        self.__id = id
        self.__name = name
        self.__level = level

   def get_id(self):
       return self.__id





