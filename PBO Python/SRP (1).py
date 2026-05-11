class Mahasiswa:
    """Hanya menyimpan data mahasiswa."""
    def __init__(self, nim, nama, ipk):
        self.nim  = nim
        self.nama = nama
        self.ipk  = ipk

    def hitung_uks(self):
        return self.ipk * 4


class PenghitungAkademik:
    """Hanya menangani logika perhitungan akademik."""
    @staticmethod
    def validasi_ipk(ipk):
        if not (0.0 <= ipk <= 4.0):
            raise ValueError(f"IPK tidak valid: {ipk}")
        return True

class PengirimEmail:
    """Hanya mengirim email."""
    def kirim_nilai(self, mahasiswa):
        print(f"Email dikirim ke {mahasiswa.nama}")


class PencetakDokumen:
    """Hanya mencetak dokumen."""
    def cetak_transkrip(self, mahasiswa):
        print(f"Transkrip {mahasiswa.nama} dicetak")


class RepositoriMahasiswa:
    """Hanya menangani penyimpanan data."""
    def simpan(self, mahasiswa):
        print(f"Menyimpan NIM {mahasiswa.nim}")


# Penggunaan
mhs     = Mahasiswa("2024001", "Andi", 3.5)
hitung  = PenghitungAkademik()
email   = PengirimEmail()
cetak   = PencetakDokumen()
repo    = RepositoriMahasiswa()

hitung.validasi_ipk(mhs.ipk)
email.kirim_nilai(mhs)
cetak.cetak_transkrip(mhs)
repo.simpan(mhs)
print("UKS:", mhs.hitung_uks())