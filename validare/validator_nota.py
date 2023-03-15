from erori.validator_error import ValidatorError


class ValidatorNota:
    def __init__(self):
        '''
        Initializeaza un validator de note
        '''
        pass

    def valideaza(self, nota):
        '''
        Verifica daca id > 0 si daca valoarea notei >= 1
        :param nota: nota
        :return: -
        :raises: ValidatorError daca id <= 0 atunci concateneaza mesajul "id invalid!\n"
                                daca valoarea notei < 1 atunci concateneaza mesajul "nota invalida!\n"
        '''
        erori = ""
        if nota.get_id_nota() <= 0:
            erori += "id invalid!\n"
        if nota.get_nota() < 1.0:
            erori += "nota invalida!\n"
        if len(erori) > 0:
            raise ValidatorError(erori)