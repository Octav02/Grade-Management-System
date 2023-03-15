class StudentLitera:
    def __init__(self,nume_student,medie_student):
        self.__nume_student = nume_student
        self.__medie_student = medie_student
    def get_nume(self):
        return self.__nume_student
    def get_medie(self):
        return self.__medie_student
    def __str__(self):
        return f"Studentul {self.__nume_student} cu media {self.__medie_student}"
    def __lt__(self, other):
        return self.__medie_student < other.__medie_student