# file : models.py
# contoh model untuk flask

class ContohModel:
    def __init__(self):
        self.text = "Aplikasi Flask"
    
    def CetakTeks(self):
        return self.text
    
class ModelBerita:
    def __init__(self, judul=None, tanggal=None, isi=None):
        self.judul = judul
        self.tanggal = tanggal
        self.isi = isi
        
    def setJudul(self, judul):
        self.judul = judul
    
    def cetakJudul(self):
        return self.judul
    
    def setTanggal(self, tanggal):
        self.tanggal = tanggal
    
    def cetakTanggal(self):
        return self.tanggal
    
    def setIsi(self, isi):
        self.isi = isi
    
    def cetakIsi(self):
        return self.isi
    
    
    