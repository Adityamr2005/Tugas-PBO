class KalkulatorNilai:
    def hitung(self, nilai, tipe_mahasiswa):
        if tipe_mahasiswa == "reguler":
            return nilai * 1.0
        elif tipe_mahasiswa == "beasiswa":
            return nilai * 1.2
        elif tipe_mahasiswa == "bidikmisi":
            return nilai * 1.15
        elif tipe_mahasiswa == "afirmasi":
            return nilai * 1.25
        # Setiap tipe baru = ubah method ini!


kalkulator = KalkulatorNilai()
print(kalkulator.hitung(85, "beasiswa"))
print(kalkulator.hitung(85, "bidikmisi"))