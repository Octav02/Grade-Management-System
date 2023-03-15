class StudentDTO:
    def __init__(self, nume, lista_note):
        self.__nume = nume
        self.__lista_note = lista_note

    def get_nume(self):
        return self.__nume
    def get_note(self):
        return self.__lista_note

    def __str__(self):
        return f"Studentul {self.__nume} cu notele : {self.__lista_note}"

    def __lt__(self, other):
        return self.__nume < other.__nume