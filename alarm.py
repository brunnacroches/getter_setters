class Alarm:
    
    def __init__(self, stade: bool) -> None:
        self.__state = stade

    def get_stade(self) -> bool:
        return self.__stade
    
    def set_stade(self, valor: bool) -> None:
        if isinstance(value, bool):
            self.__stade = value