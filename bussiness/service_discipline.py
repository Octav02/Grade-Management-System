from domeniu.disciplina import Disciplina
import random

class ServiceDiscipline:
    def __init__(self, validator_disciplina, repo_discipline):
        '''
        Intializeaza service-ul de discipline cu un validator de discipline si un repository de discipline
        :param validator_disciplina: validator
        :param repo_discipline: repository
        '''
        self.__validator_disciplina = validator_disciplina
        self.__repo_discipline = repo_discipline

    def creeaza_si_adauga_disciplina(self):
        '''
        Creeaza o disciplina random si o adauga la lista de discipline
        :return: -
        '''
        id = random.randint(1, 10000001)
        lista_nume = ["Andrei", "Bogdan", "Cristi", "Constantin", "Codrut", "Mihnea", "Octav", "Alexandra", "Casiana",
                      "Matei",
                      "Darius", "Daria", "Minodora", "Tudor", "Emanuela", "Elena", "Andreea", "Mihai"]
        id_nume = random.randint(0, len(lista_nume) - 1)
        nume = lista_nume[id_nume]
        lista_materii = ["Analiza", "Logica", "Algebra", "Microeconomie", "Macroeconomie", "InteligentaArtificiala", "FundamenteleProgramarii", "Sport", "Contabilitate",
                   "Mandarina"]
        id_materie = random.randint(0, len(lista_materii) - 1)
        materie = lista_materii[id_materie]
        self.adauga_disciplina(id,materie,nume)

    def adauga_disciplina(self, id_disciplina, nume_disciplina, profesor_disciplina):
        '''
        Creeaza o disciplina cu parametrii dati, o valideaza si daca e valida o adauga in dictionar
        :param id_disciplina: int
        :param nume_disciplina: string
        :param profesor_disciplina: string
        :return: -
        :raises: RepositoryError daca id-ul disciplinei exista deja in dictionar, afjsand "Disciplina existenta!"
                  ValidatorError: daca id-ul <=0 atunci concateneaza mesajul "id invalid!\n"
                                  daca numele este vid atunci concateneaza mesajul "nume invalid!\n"
                                  daca profesorul este vid atunci concateneaza mesajul "profesor invalid!\n"

        '''
        disciplina = Disciplina(id_disciplina,nume_disciplina,profesor_disciplina)
        self.__validator_disciplina.valideaza(disciplina)
        self.__repo_discipline.adauga_disciplina(disciplina)

    def modifica_disciplina(self, id_disciplina, nume_disciplina, profesor_disciplina):
        '''
        Creeaz o disciplina cu parametrii dati, o valideaza, iar daca e valida inlocuieste
        disciplina din dictionar cu id-ul id_disciplina cu disciplina creata
        :param id_disciplina: int
        :param nume_disciplina: string
        :param profesor_disciplina: string
        :return: -
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
                 ValidatorError: daca id-ul <=0 atunci concateneaza mesajul "id invalid!\n"
                                  daca numele este vid atunci concateneaza mesajul "nume invalid!\n"
                                  daca profesorul este vid atunci concateneaza mesajul "profesor invalid!\n"

        '''
        disciplina = Disciplina(id_disciplina, nume_disciplina, profesor_disciplina)
        self.__validator_disciplina.valideaza(disciplina)
        self.__repo_discipline.modifica_disciplina(disciplina)

    def get_all_discipline(self):
        '''
        Returneaza o lista cu toate disciplinele din dictionar
        :return: discipline- lista
        '''
        return self.__repo_discipline.get_all_discipline()

    def cauta_disciplina_dupa_id(self, id_disciplina):
        '''
        Returneaza disciplina din dictionar cu id-ul id_disciplina
        :param id_disciplina: int
        :return: disciplina
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
        '''
        return self.__repo_discipline.cauta_disciplina_dupa_id(id_disciplina)

    def sterge_disciplina_dupa_id(self, id_disciplina):
        '''
        Sterge disciplina din dictionar cu id-ul id_disciplina
        :param id_disciplina: int
        :return: -
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
        '''
        self.__repo_discipline.sterge_disciplina_dupa_id(id_disciplina)