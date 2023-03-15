from erori.repository_error import RepositoryError
from erori.validator_error import ValidatorError


class Consola:
    def __init__(self, service_studenti, service_discipline, service_note):
        self.__service_studenti = service_studenti
        self.__service_discipline = service_discipline
        self.__service_note = service_note
        self.__comenzi = {
            "adauga_student": self.__ui_adauga_student,
            "modifica_student": self.__ui_modifica_student,
            "cauta_student": self.__ui_cauta_student,
            "adauga_disciplina": self.__ui_adauga_disciplina,
            "cauta_disciplina": self.__ui_cauta_disciplina,
            "modifica_disciplina": self.__ui_modifica_disciplina,
            "sterge_disciplina": self.__ui_sterge_disciplina,
            "adauga_nota": self.__ui_adauga_nota,
            "modifica_nota": self.__ui_modifica_nota,
            "cauta_nota": self.__ui_cauta_nota,
            "sterge_nota": self.__ui_sterge_nota,
            "sterge_student": self.__ui_sterge_student,
            "printeaza_studenti": self.__ui_printeaza_studenti,
            "printeaza_discipline": self.__ui_printeaza_discipline,
            "printeaza_note": self.__ui_printeaza_note,
            "printeaza_sefi_promotie": self.__ui_printeaza_sefi_promotie,
            "creare_studenti": self.__ui_creaza_studenti,
            "creare_discipline": self.__ui_creaza_discipline,
            "creare_note": self.__ui_creaza_note,
            "printeaza_studenti_note_disciplina": self.__ui_printeaza_studenti_note_disciplina,
            "printeaza_medie_studenti_litera": self.__ui_printeaza_medie_studenti_litera,
            "help": self.__ui_printeaza_help
        }

    def __ui_printeaza_medie_studenti_litera(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        litera = params[0]
        try:
            print(f"Media studentilor cu litera {litera} este : {self.__service_note.medie_studenti_litera(litera)}")
        except:
            print("Nu exista studenti care incep cu aceasta litera")
    def __ui_creaza_note(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        nr = int(params[0])
        while nr != 0:
            try:
                self.__service_note.creare_si_adaugare_note()
            except RepositoryError as re:
                pass
            else:
                nr = nr - 1
    def __ui_creaza_discipline(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        nr = int(params[0])
        while nr != 0:
            try:
                self.__service_discipline.creeaza_si_adauga_disciplina()
            except RepositoryError as re:
                print(re)
            else:
                nr = nr - 1
    def __ui_creaza_studenti(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        nr = int(params[0])
        while nr != 0:
            try:
                self.__service_studenti.creeaza_si_adauga_student()
            except RepositoryError as re:
                pass
            else:
                nr = nr - 1

    def __ui_printeaza_sefi_promotie(self, params):
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        sefi_promotie = self.__service_note.get_sefi_promotie()
        if len(sefi_promotie) == 0:
            print("Nu exista suficienti studenti pentru a printa primii 20% dintre ei")
            return
        print("Studentii cautati sunt :")
        for sef_promotie in sefi_promotie:
            print(sef_promotie)

    def __ui_printeaza_studenti_note_disciplina(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        lista_studenti = self.__service_note.get_studenti_note_de_la_disciplina(int(params[0]))
        if len(lista_studenti) == 0:
            print("Nu exista note sau studenti la aceasta materie")
            return
        print("Studentii cautati sunt: ")
        for student in lista_studenti:
            print(student)
    def __ui_printeaza_studenti(self, params):
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        lista_studenti = self.__service_studenti.get_all_studenti()
        if len(lista_studenti) == 0:
            print("Nu exista studenti in lista")
            return
        for student in lista_studenti:
            print(student)

    def __ui_modifica_student(self, params):
        if len(params) != 2:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        nume = params[1]
        self.__service_studenti.modifica_student(id, nume)
        print("Modificare efectuata cu succes")

    def __ui_modifica_disciplina(self, params):
        if len(params) != 3:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        nume = params[1]
        profesor = params[2]
        self.__service_discipline.modifica_disciplina(id, nume, profesor)
        print("Modificare efectuata cu succes")

    def __ui_modifica_nota(self, params):
        if len(params) != 4:
            print("Numar parametri invalid!")
            return
        id_nota = int(params[0])
        id_student = int(params[1])
        id_disciplina = int(params[2])
        valoare_nota = float(params[3])
        self.__service_note.modifica_nota(id_nota, id_student, id_disciplina, valoare_nota)
        print("Modificare efectuata cu succes")

    def __ui_cauta_student(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        student = self.__service_studenti.cauta_student_dupa_id(id)
        print(f"Studentul cautat este {student}")

    def __ui_cauta_disciplina(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        disciplina = self.__service_discipline.cauta_disciplina_dupa_id(id)
        print(f"Disciplina cautata este {disciplina}")

    def __ui_cauta_nota(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        nota = self.__service_note.cauta_nota_dupa_id(id)
        print(f"Nota cautata este {nota}")

    def __ui_printeaza_discipline(self, params):
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        lista_discipline = self.__service_discipline.get_all_discipline()
        if len(lista_discipline) == 0:
            print("Nu exista discipline in lista")
            return
        for disciplina in lista_discipline:
            print(disciplina)

    def __ui_printeaza_note(self, params):
        if len(params) != 0:
            print("Numar parametri invalid!")
            return
        lista_note = self.__service_note.get_all_note()
        if len(lista_note) == 0:
            print("Nu exista note in lista")
            return
        for nota in lista_note:
            print(nota)

    def __ui_adauga_student(self, params):
        if len(params) != 2:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        nume = params[1]
        self.__service_studenti.adauga_student(id, nume)
        print("Adaugare efectuata cu succes")

    def __ui_adauga_disciplina(self, params):
        if len(params) != 3:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        nume = params[1]
        profesor = params[2]
        self.__service_discipline.adauga_disciplina(id, nume, profesor)
        print("Adaugare efectuata cu succes")

    def __ui_adauga_nota(self, params):
        if len(params) != 4:
            print("Numar parametri invalid!")
            return
        id_nota = int(params[0])
        id_student = int(params[1])
        id_disciplina = int(params[2])
        nota = float(params[3])
        self.__service_note.adauga_nota(id_nota, id_student, id_disciplina, nota)
        print("Adaugare efectuata cu succes")

    def __ui_sterge_student(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        self.__service_note.sterge_student_si_note(id)
        print("Stergere efectuata cu succes")

    def __ui_sterge_disciplina(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        self.__service_note.sterge_disciplina_si_note(id)
        print("Stergere efectuata cu succes")

    def __ui_sterge_nota(self, params):
        if len(params) != 1:
            print("Numar parametri invalid!")
            return
        id = int(params[0])
        self.__service_note.sterge_nota_dupa_id(id)
        print("Stergere efectuata cu succes")

    def __ui_printeaza_help(self, params):
        print("adauga_student id nume")
        print("modifica_student id nume")
        print("cauta_student id")
        print("sterge_student id")
        print("printeaza_studenti")
        print("adauga_disciplina id nume profesor")
        print("modifica_disciplina id nume profesor")
        print("cauta_disciplina id")
        print("sterge disciplina id")
        print("printeaza_discipline")
        print("adauga_nota id id_student id_disciplina valoare_nota")
        print("modifica_nota id id_student id_disciplina valoare_nota")
        print("cauta_nota id")
        print("sterge_nota id")
        print("printeaza_sefi_promotie")
        print("printeaza_note")
        print("creare_studenti nr_studenti")
        print("creare_discipline nr_discipline")
        print("printeaza_studenti_note_disciplina id_disicplina")

    def runUI(self):
        print("Pentru a accesa o lista cu comenzi si cu parametrii asteptati ca input, introdu comanda help, iar pentru"
              "a iesi introdu comanda exit")
        while True:
            command = input(">>>")
            command = command.strip()
            parti = command.split()
            nume_comanda = parti[0]
            params = parti[1:]
            if nume_comanda == "exit":
                print("Bye!")
                return
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda](params)
                except ValueError:
                    print("Eroare invalida! tip numeric invalid!")
                except RepositoryError as re:
                    print(f"Repoistory Error : {re}")
                except ValidatorError as ve:
                    print(f"Validator Error : {ve}")
