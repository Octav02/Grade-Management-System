from erori.validator_error import ValidatorError


class ValidatorDisciplina:
    def __init__(self):
        '''
        Initializeaza un validator de discipline
        '''
        pass

    def valideaza(self, disciplina):
        '''
        Verifica daca id-ul > 0, si daca numele si profesorul disciplinei sunt vizi
        :param disciplina: disciplina
        :return: -
        :raises: ValidatorError: daca id-ul <=0 atunci concateneaza mesajul "id invalid!\n"
                                 daca numele este vid atunci concateneaza mesajul "nume invalid!\n"
                                 daca profesorul este vid atunci concateneaza mesajul "profesor invalid!\n"
        '''
        erori = ""
        if disciplina.get_id_disciplina() <= 0:
            erori += "id invalid!\n"
        if disciplina.get_nume_disciplina() == "":
            erori += "nume invalid!\n"
        if disciplina.get_profesor_disciplina() == "":
            erori += "profesor invalid!\n"
        if len(erori) > 0:
            raise ValidatorError(erori)