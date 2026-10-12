
class Tugas:
    def __init__(self, id_tugas, nama, mapel, deadline):
        self.id_tugas = id_tugas
        self.nama = nama
        self.mapel = mapel
        self.deadline = deadline

    def to_list(self):
        return [
            self.id_tugas,
            self.nama,
            self.mapel,
            self.deadline
        ]

    def __str__(self):
        return (
            f"{self.nama} - {self.mapel} "
            f"(ID: {self.id_tugas}) - Deadline: {self.deadline}"
        )
