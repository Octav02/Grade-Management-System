from erori.validator_error import ValidatorError

class ValidatorStudent:

    def __init__(self):
        '''
        Initializeaza un validator de studenti
        '''
        pass

    def valideaza(self, student):
        '''
        Verifica daca id-ul unui student >0 si daca numele nu e vid
        :param student: student
        :return: -
        :raises: ValidatorError: daca id-ul <= 0, atunci concateneaza mesajul "id invalid!\n"
                                 daca numele este vid, atunci concateneaza mesajul "nume invalid!\n"
        '''
        erori = ""
        if student.get_id_student() <= 0:
            erori += "id invalid!\n"
        if student.get_nume_student() == "":
            erori += "nume invalid!\n"
        if len(erori) > 0:
            raise ValidatorError(erori)