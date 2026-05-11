class Mahasiswa:
    def __init__(self, nim, nama, ipk):
        self.nim  = nim
        self.nama = nama
        self.ipk  = ipk

    # Tanggung jawab 1: hitung nilai
    def hitung_uks(self):
        return self.ipk * 4

    # Tanggung jawab 2: validasi IPK
    def validasi_ipk(self):
        if not (0.0 <= self.ipk <= 4.0):
            raise ValueError("IPK tidak valid!")

    # Tanggung jawab 3: kirim email
    def kirim_email_nilai(self):
        print(f"Mengirim email ke {self.nama}...")

    # Tanggung jawab 4: cetak transkrip
    def cetak_transkrip(self):
        print(f"Mencetak transkrip {self.nama}...")
      # Tanggung jawab 5: simpan ke database
    def simpan_ke_database(self):
        print(f"Menyimpan {self.nim} ke database...")


mhs = Mahasiswa("2024001", "Andi", 3.5)
mhs.validasi_ipk()
mhs.kirim_email_nilai()
mhs.cetak_transkrip()
mhs.simpan_ke_database()
print("UKS:", mhs.hitung_uks())