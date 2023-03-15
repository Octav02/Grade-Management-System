from erori.repository_error import RepositoryError


class RepoNote:
    def __init__(self):
        '''
        Initializeaza un dictionar de studenti, initial vid
        '''
        self._note = {}

    def adauga_nota(self, nota):
        '''
        Adauga o nota in dictionarul de note, daca aceasta nu exista deja
        :param nota: nota
        :return: -
        :raises: RepositoryError daca id-ul notei exista deja in dictionar, afiseaza mesajul "Nota existenta!"
        '''
        if nota.get_id_nota() in self._note:
            raise RepositoryError("Nota existenta!")
        self._note[nota.get_id_nota()] = nota

    def modifica_nota(self, nota):
        '''
        Inlocuieste nota din dictionar aavand id-ul notei date ca parametru,cu aceasta din urma
        :param nota: nota
        :return: -
        :raises: RepositoryError: Daca id-ul notei nu se gaseste in dictionar, afiseaza mesajul "Nota inexistenta!"
        '''
        if nota.get_id_nota() not in self._note:
            raise RepositoryError("Nota inexistenta!")
        self._note[nota.get_id_nota()] = nota

    def get_all_note(self):
        '''
        Returneaza o lista cu toate notele din dictionar
        :return: note-lista
        '''
        note = []
        for id_nota in self._note:
            note.append(self._note[id_nota])
        return note

    def cauta_nota_dupa_id(self, id_nota):
        '''
        Returneaza nota din dictionar avand id-ul id_nota
        :param id_nota: int
        :return: nota
        :raises: RepositoryError: Daca id-ul notei nu se gaseste in dictionar, afiseaza mesajul "Nota inexistenta!"
        '''
        if id_nota not in self._note:
            raise RepositoryError("Nota inexistenta!")
        return self._note[id_nota]

    def sterge_nota_dupa_id(self, id_nota):
        '''
        Sterge nota din dictionar cu id-ul id_nota
        :param id_nota: int
        :return: -
        :raises: RepositoryError: Daca id-ul notei nu se gaseste in dictionar, afiseaza mesajul "Nota inexistenta!"
        '''
        if id_nota not in self._note:
            raise RepositoryError("Nota inexistenta!")
        del self._note[id_nota]

    def __len__(self):
        '''
        Returneaza lungimea dictionarului de note
        :return: int
        '''
        return len(self._note)
