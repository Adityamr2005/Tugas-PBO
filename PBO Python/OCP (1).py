class StrategiPerhitungan:
    """Base class — kontrak untuk semua strategi."""
    def hitung(self, nilai):
        raise NotImplementedError


class StrategiReguler(StrategiPerhitungan):
    def hitung(self, nilai):
        return nilai * 1.0


class StrategiBeasiswa(StrategiPerhitungan):
    def hitung(self, nilai):
        return nilai * 1.2


class StrategiBidikmisi(StrategiPerhitungan):
    def hitung(self, nilai):
        return nilai * 1.15
class StrategiAfirmasi(StrategiPerhitungan):
    def hitung(self, nilai):
        return nilai * 1.25


class KalkulatorNilai:
    """Tidak perlu diubah saat tipe baru ditambahkan."""
    def __init__(self, strategi: StrategiPerhitungan):
        self.strategi = strategi

    def hitung(self, nilai):
        return self.strategi.hitung(nilai)


# Penggunaan
k1 = KalkulatorNilai(StrategiBeasiswa())
k2 = KalkulatorNilai(StrategiBidikmisi())
print(k1.hitung(85))   # 102.0
print(k2.hitung(85))   # 97.75
