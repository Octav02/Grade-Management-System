from domeniu.nota import Nota
from domeniu.sef_promotie_dto import SefPromotieDTO
from domeniu.student_dto import StudentDTO
import random


class ServiceNote:
    def __init__(self, validator_nota, repo_studenti, repo_discipline, repo_note):
        '''
        Intializeaz service-ul de note cu un validator de note, repository-ul de studenti, de discipline si cel de note
        :param validator_nota: validator
        :param repo_studenti: repository
        :param repo_discipline: repository
        :param repo_note: repository
        '''
        self.__validator_nota = validator_nota
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline
        self.__repo_note = repo_note



    def adauga_nota(self, id_nota, id_student, id_disciplina, valoare_nota):
        '''
        Programul cauta studentul cu id-ul id_student si disciplina cu id_disciplina si creeaza
        o nota avand id_nota, studentul gasit si disciplina gasita. Valideaza nota, iar daca e valida
        o adauga in repo
        :param id_nota: int
        :param id_student: int
        :param id_disciplina: int
        :param valoare_nota: float
        :return: -
        :raises:RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
                                 daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
                ValidatorError daca id <= 0 atunci concateneaza mesajul "id invalid!\n"
                                daca valoarea notei < 1 atunci concateneaza mesajul "nota invalida!\n"

        '''
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        disciplina = self.__repo_discipline.cauta_disciplina_dupa_id(id_disciplina)
        nota = Nota(id_nota, student, disciplina, valoare_nota)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota(nota)

    def modifica_nota(self, id_nota, id_student, id_disciplina, valoare_nota):
        '''
        Programul cauta studentul cu id-ul id_student si disciplina cu id_disciplina si creeaza
        o nota avand id_nota, studentul gasit si disciplina gasita. Valideaza nota, iar daca e valida
        inlocuieste nota din repo avand id-ul id_nota cu nota creata
        :param id_nota: int
        :param id_student: int
        :param id_disciplina: int
        :param valoare_nota: float
        :return: -
        :raises: RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
                                 daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"
                   ValidatorError daca id <= 0 atunci concateneaza mesajul "id invalid!\n"
                                daca valoarea notei < 1 atunci concateneaza mesajul "nota invalida!\n"

        '''
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        disciplina = self.__repo_discipline.cauta_disciplina_dupa_id(id_disciplina)
        nota = Nota(id_nota, student, disciplina, valoare_nota)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.modifica_nota(nota)

    def medie_studenti_litera(self, litera):
        medie = 0
        leng = 0
        note = self.__repo_note.get_all_note()
        for nota in note:
            student = nota.get_student()
            nume_student = student.get_nume_student()
            if nume_student[0] == litera:
                leng+=1
                medie += nota.get_nota()
        medie /= leng
        return medie


    def get_studenti_note_de_la_disciplina(self, id_disciplina):
        '''
        Returneaza toti studentii si notele lor de la o anumita disciplina,
        sortati crescator dupa note si alfabetic dupa nume
        :param id_disciplina: int
        :return: lista
        '''
        info_studenti = {}
        note = self.get_all_note()
        for nota in note:
            disciplina = nota.get_disciplina()
            if disciplina.get_id_disciplina() == id_disciplina:
                id_student = nota.get_student().get_id_student()
                if id_student not in info_studenti:
                    info_studenti[id_student] = []
                info_studenti[id_student].append(nota.get_nota())
        for lista_note in info_studenti.values():
            lista_note.sort()
        lista_studenti = []
        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume = student.get_nume_student()
            student_dto = StudentDTO(nume, info_studenti[id_student])
            lista_studenti.append(student_dto)
        lista_studenti.sort()
        return lista_studenti

    def cauta_nota_dupa_id(self, id_nota):
        '''
        Returneaza nota din dictionar avand id-ul id_nota
        :param id_nota: int
        :return: nota
        :raises: RepositoryError: Daca id-ul notei nu se gaseste in dictionar, afiseaza mesajul "Nota inexistenta!"
        '''
        return self.__repo_note.cauta_nota_dupa_id(id_nota)

    def sterge_nota_dupa_id(self, id_nota):
        '''
        Sterge nota din dictionar cu id-ul id_nota
        :param id_nota: int
        :return: -
        :raises: RepositoryError: Daca id-ul notei nu se gaseste in dictionar, afiseaza mesajul "Nota inexistenta!"
        '''
        self.__repo_note.sterge_nota_dupa_id(id_nota)

    def sterge_student_si_note(self, id_student):
        '''
        Cauta studentul cu id-ul id_student si sterge din repo-ul de studenti studentul respectiv
        si toate notele sale din repo-ul de note
        :param id_student: int
        :return: -
        :raises:  RepositoryError: Daca id-ul studentului nu se gasesete in dictionarul de studenti, afisand "Student inexistent!"
        '''
        student = self.__repo_studenti.cauta_student_dupa_id(id_student)
        lista_note = self.__repo_note.get_all_note()
        for nota in lista_note:
            if nota.get_student() == student:
                self.__repo_note.sterge_nota_dupa_id(nota.get_id_nota())
        self.__repo_studenti.sterge_student_dupa_id(id_student)

    def sterge_disciplina_si_note(self, id_disciplina):
        '''
        Cauta disciplina cu id-ul id_disciplina si sterge din repo-ul de discipline disciplina respectiva
        si toate notele asociate disciplinei din repo-ul de note
        :param id_disciplina: int
        :return: -
        :raises: RepositoryError daca id-ul disciplinei nu se gaseste in dicitonarul de discipline, afisand "Disciplina inexistenta"

        '''
        disciplina = self.__repo_discipline.cauta_disciplina_dupa_id(id_disciplina)
        lista_note = self.__repo_note.get_all_note()
        for nota in lista_note:
            if nota.get_disciplina() == disciplina:
                self.__repo_note.sterge_nota_dupa_id(nota.get_id_nota())
        self.__repo_discipline.sterge_disciplina_dupa_id(id_disciplina)

    def get_sefi_promotie(self):
        '''
        Returneaza primii 20% studenti(nume si media studentului) ordonati dupa media notelor la toate materiile
        :return:list
        '''
        info_studenti = {}
        note = self.__repo_note.get_all_note()
        for nota in note:
            id_student_nota = nota.get_student().get_id_student()
            valoare_nota = nota.get_nota()
            if id_student_nota not in info_studenti:
                info_studenti[id_student_nota] = []
            info_studenti[id_student_nota].append(valoare_nota)
        sefi_promotie = []
        numar_cerut = len(info_studenti) // 5
        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student_dupa_id(id_student)
            nume_student = student.get_nume_student()
            medie_student = sum(info_studenti[id_student]) / len(info_studenti[id_student])
            sef_promotie_dto = SefPromotieDTO(nume_student, medie_student)
            sefi_promotie.append(sef_promotie_dto)
        sefi_promotie.sort(reverse=True)
        return sefi_promotie[:numar_cerut]

    def creare_si_adaugare_note(self):
        '''
        Creeaza si adauga la lista o disciplina random
        :return: -
        '''
        id = random.randint(1, 100000000001)
        lista_id_studenti = []
        studenti = self.__repo_studenti.get_all_studenti()
        for student in studenti:
            lista_id_studenti.append(student.get_id_student())
        lista_id_discipline = []
        discipline = self.__repo_discipline.get_all_discipline()
        for disciplina in discipline:
            lista_id_discipline.append(disciplina.get_id_disciplina())
        id_student = id % len(lista_id_studenti)
        id_disciplina = id % len(lista_id_discipline)
        valoare_nota = random.randint(1, 11)
        self.adauga_nota(id,id_student,id_disciplina, valoare_nota)

    def get_all_note(self):
        '''
        Returneaza o lista cu toate notele din dictionar
        :return: note-lista
        '''
        return self.__repo_note.get_all_note()
