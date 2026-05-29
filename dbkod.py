import sqlite3 as sql
vt=sql.connect("veritabani.db")
imlec=vt.cursor()
"""İŞLEM FONKSİYONLARI"""
def baslangicmenu():
    soru=input(""" 
    1-Hasta Üyeliği
    2-Hasta Girişi
    3-Doktor Girişi
    4-Çıkış
    TUŞLAYINIZ : 
    """)
    return soru

def hastamenu():
    soru=input("""
    Hasta Menüsü
    1-Randevu al
    2-Randevu güncelle
    3-Randevu sil
    4-Randevu listele
    5-Çıkış
    TUŞLAYINIZ :
    """)
    return soru

def doktormenu():
    soru=input("""
    Doktor Menüsü
    1-Randevu sil
    2-üye sayısı
    3-Çıkış
    TUŞLAYINIZ :
    """)
    return soru



""" VERİTABANI FONKSİYONLARI"""
"""
1.kısım
"""
"""giris işlem"""
def tabloyap():
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    imlec.execute(""" CREATE TABLE IF NOT EXISTS hastabilgi(ID integer PRIMARY KEY,ad TEXT,tel TEXT,tc TEXT,sifre TEXT )""")
    imlec.execute(""" CREATE TABLE IF NOT EXISTS doktorbilgi(ID integer PRIMARY KEY,ad TEXT,tel TEXT,tc TEXT,sifre TEXT )""")
    imlec.execute(""" CREATE TABLE IF NOT EXISTS randevubilgi(tc TEXT,ad TEXT,tel TEXT,hastane_ad TEXT,hastane_poliklinik TEXT,doktor_ad TEXT,randevu_tarih TEXT,randevu_saat TEXT)""")
    vt.commit()
    vt.close()

def kayit(ad,tel,tc,sifre):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ekleme="""INSERT INTO hastabilgi(ad,tel,tc,sifre) VALUES {}"""
    veri=(ad,tel,tc,sifre)
    imlec.execute(ekleme.format(veri))
    vt.commit()
    vt.close()

def hastagiris(ad,sifre):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    arama="""SELECT *FROM hastabilgi where ad = '{}' and sifre='{}'"""
    imlec.execute(arama.format(ad,sifre))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return liste[1],liste[2],liste[3]   
    else:
        bos=" "
        vt.close()
        return bos,bos,bos

def doktorgiris(ad,sifre):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    arama="""SELECT *FROM doktorbilgi where ad = '{}' and sifre='{}'"""
    imlec.execute(arama.format(ad,sifre))
    liste=imlec.fetchone()
    
    if liste!=None:
        vt.close()
        return liste[1],liste[2],liste[3]    
    else:
        bos=""
        vt.close()
        return bos,bos,bos
    
"""
2.kısım
"""
"""hasta işlem"""
def randevukayit(ad,tel,tc,hastanead,poliklinik,doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    rkayit="""INSERT INTO randevubilgi(tc,ad,tel,hastane_ad,hastane_poliklinik,doktor_ad,randevu_tarih,randevu_saat) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')"""
    imlec.execute(rkayit.format(tc,ad,tel,hastanead,poliklinik,doktorad,tarih,saat))
    vt.commit()
    vt.close()

def guncelara(tc,doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ara="""SELECT *FROM randevubilgi where tc='{}'and doktor_ad='{}'and randevu_tarih='{}'and randevu_saat='{}'"""
    imlec.execute(ara.format(tc,doktorad,tarih,saat))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return 1
    else:
        vt.close()
        return 0
    
def randevuguncelle(ad,tel,tc,hastanead,poliklinik,doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    guncelle="""UPDATE randevubilgi SET hastane_ad='{}' , hastane_poliklinik='{}' , doktor_ad='{}' , randevu_tarih='{}' , randevu_saat='{}' where tc='{}' and ad='{}' and tel='{}'"""
    imlec.execute(guncelle.format(hastanead,poliklinik,doktorad,tarih,saat,tc,ad,tel))
    vt.commit()
    vt.close()

def silmeara(tc,doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ara="""SELECT *FROM randevubilgi where tc='{}'and doktor_ad='{}'and randevu_tarih='{}'and randevu_saat='{}'"""
    imlec.execute(ara.format(tc,doktorad,tarih,saat))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return 1
    else:
        vt.close()
        return 0
    
def randevusilme(tc,doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    silme="""DELETE FROM randevubilgi where tc='{}' and doktor_ad='{}' and randevu_tarih='{}' and randevu_saat='{}' """
    imlec.execute(silme.format(tc,doktorad,tarih,saat))
    vt.commit()
    vt.close()

def listele(ad,tel,tc):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    gorme="""SELECT *FROM randevubilgi where ad='{}' and tel='{}' and tc='{}'"""
    imlec.execute(gorme.format(ad,tel,tc))
    liste=imlec.fetchone()
    vt.close()
    return liste 

"""3.kısım"""
"""doktor"""
def doktorsilmeara(doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    ara="""SELECT *FROM randevubilgi where doktor_ad='{}'and randevu_tarih='{}'and randevu_saat='{}'"""
    imlec.execute(ara.format(doktorad,tarih,saat))
    liste=imlec.fetchone()
    if liste!=None:
        vt.close()
        return 1
    else:
        vt.close()
        return 0

def doktorrandevusilme(doktorad,tarih,saat):
    vt=sql.connect("veritabani.db")
    imlec=vt.cursor()
    silme="""DELETE FROM randevubilgi where doktor_ad='{}' and randevu_tarih='{}' and randevu_saat='{}' """
    imlec.execute(silme.format(doktorad,tarih,saat))
    vt.commit()
    vt.close()

