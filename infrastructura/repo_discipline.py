from erori.repository_error import RepositoryError


class RepoDiscipline:
    def __init__(self):
        '''
        Initializeaza un dictionar de discipline, initial vid
        '''
        self._discipline = {}

    def adauga_disciplina(self, disciplina):
        '''
        Adauga o disciplina in dicitonarul de discipline ,daca aceasta nu exista deja in dictionar
        :param disciplina: disciplina
        :return: -
        :raises: RepositoryError daca id-ul disciplinei exista deja in dictionar, afjsand "Disciplina existenta!"
        '''
        if disciplina.get_id_disciplina() in self._discipline:
            raise RepositoryError("Disciplina existenta!")
        self._discipline[disciplina.get_id_disciplina()] = disciplina


    def modifica_disciplina(self, disciplina):
        '''
        Inlocuieste disciplina din dictionar avand id-ul disciplinei data ca parametru, cu aceasta din urma
        :param disciplina: disciplina
        :return:-
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
        '''
        if disciplina.get_id_disciplina() not in self._discipline:
            raise RepositoryError("Disciplina inexistenta!")
        self._discipline[disciplina.get_id_disciplina()] = disciplina

    def get_all_discipline(self):
        '''
        Returneaza o lista cu toate disciplinele din dictionar
        :return: discipline- lista
        '''
        discipline = []
        for id_disciplina in self._discipline:
            discipline.append(self._discipline[id_disciplina])
        return discipline

    def cauta_disciplina_dupa_id(self, id_disciplina):
        '''
        Returneaza disciplina din dictionar cu id-ul id_disciplina
        :param id_disciplina: int
        :return: disciplina
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
        '''
        if id_disciplina not in self._discipline:
            raise RepositoryError("Disciplina inexistenta!")
        return self._discipline[id_disciplina]

    def sterge_disciplina_dupa_id(self, id_disciplina):
        '''
        Sterge disciplina din dictionar cu id-ul id_disciplina
        :param id_disciplina: int
        :return: -
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
        '''
        if id_disciplina not in self._discipline:
            raise RepositoryError("Disciplina inexistenta!")
        del self._discipline[id_disciplina]

    def __len__(self):
        '''
        Returneaza lungimea dictionarului de studenti
        :return: int
        '''
        return len(self._discipline)
