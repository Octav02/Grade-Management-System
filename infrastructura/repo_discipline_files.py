from domeniu.disciplina import Disciplina
from infrastructura.repo_discipline import RepoDiscipline


class RepoDisciplineFisier(RepoDiscipline):
    def __init__(self, nume_fisier):
        RepoDiscipline.__init__(self)
        self.__nume_fisier = nume_fisier

    def __load_from_file(self):
        with open(self.__nume_fisier, "r") as f:
            lines = f.readlines()
            self._discipline.clear()
            for line in lines:
                line.strip()
                if line != "\n":
                    params = line.split(";")
                    id = int(params[0])
                    nume = params[1]
                    profesor = params[2]
                    disciplina = Disciplina(id, nume, profesor)
                    self._discipline[id] = disciplina

    def __write_to_file(self):
        with open(self.__nume_fisier, "w") as f:
            for disciplina in self._discipline.values():
                id = disciplina.get_id_disciplina()
                nume = disciplina.get_nume_disciplina()
                profesor = disciplina.get_profesor_disciplina()
                f.write(str(id) + ";" + nume + ";" + profesor+";\n")

    def adauga_disciplina(self, disciplina):
        self.__load_from_file()
        RepoDiscipline.adauga_disciplina(self, disciplina)
        self.__write_to_file()

    def modifica_disciplina(self, disciplina):
        self.__load_from_file()
        RepoDiscipline.modifica_disciplina(self, disciplina)
        self.__write_to_file()

    def sterge_disciplina_dupa_id(self, id_disciplina):
        self.__load_from_file()
        RepoDiscipline.sterge_disciplina_dupa_id(self, id_disciplina)
        self.__write_to_file()

    def cauta_disciplina_dupa_id(self, id_disciplina):
        self.__load_from_file()
        return RepoDiscipline.cauta_disciplina_dupa_id(self, id_disciplina)

    def get_all_discipline(self):
        self.__load_from_file()
        return RepoDiscipline.get_all_discipline(self)

    def __len__(self):
        self.__load_from_file()
        return len(self._discipline)
