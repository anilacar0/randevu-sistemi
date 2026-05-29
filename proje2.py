import sqlite3
from dbkod import *



tabloyap()

istemci=0
""" 
istemci = '1'hasta girişi
istemci = '2'doktor girişi
"""
sayi=0
dosya=open("uyelik.txt","r")
sayi=int(dosya.read())
dosya.close()
bilgi=[]
while(1):
    if istemci!=1 and istemci!=2:
        sorgu=int(baslangicmenu())
        if sorgu==1:
            while 1:
                Hasta_ad=input("Adınızı giriniz : ")
                Hasta_tel=input("Telefon no giriniz : ")
                Hasta_tc=input("TC no giriniz : ")
                Hasta_sifre=input("Şifre giriniz : ")
                if Hasta_ad!="" and len(Hasta_tc)==11 and Hasta_sifre!="":
                    kayit(Hasta_ad,Hasta_tel,Hasta_tc,Hasta_sifre)
                    print("kayıt başarılı")
                    dosya1=open("uyelik.txt","w")
                    sayi+=1
                    dosya1.write(str(sayi))
                    dosya1.close()
                    break
                else:
                    print("dikkatli giriniz bilgileri")
        elif sorgu==2:
            while 1:
                giris_ad=input("Adınızı giriniz : ")
                giris_sifre=input("Şifrenizi giriniz : ")
                if giris_ad!="" and giris_sifre!="":
                    ad_bilgi,tel_bilgi,tc_bilgi=hastagiris(giris_ad,giris_sifre)
                    if ad_bilgi!=None:
                        print("girişiniz başarıyla yapılmıştır sayın {}".format(ad_bilgi))
                        istemci=1
                        break
                    else:
                        print("böyle bir hesap bulunamadı")
                else:
                    print("isim veya şifre boş geçilemez ")
                
        elif sorgu==3:
            while 1:
                giris_ad=input("Adınızı giriniz : ")
                giris_sifre=input("Şifrenizi giriniz : ")
                if giris_ad!="" and giris_sifre!="":
                    ad_bilgi,tel_bilgi,tc_bilgi=doktorgiris(giris_ad,giris_sifre)
                    if ad_bilgi!=None:
                        print("girişiniz başarıyla yapılmıştır sayın {}".format(ad_bilgi))
                        istemci=2
                        break
                    else:
                        print("böyle bir hesap bulunamadı")
                else:
                    print("isim veya şifre boş geçilemez ")
        elif sorgu==4:
            break
        else:
            print("yanlış tuşlama yaptınız tekrar deneyiniz")
    else:
        break


if istemci==1:
    while 1:
        sorgu=int(hastamenu())
        if sorgu==1:           
            randevu_hastanead=input("Hastane adı giriniz : ")
            randevu_hastanepoliklinik=input("Poliklinik giriniz : ")
            randevu_doktorad=input("Doktor adı giriniz : ")
            randevu_tarih=input("Randevu tarihi giriniz : ")
            randevu_saat=input("Randevu saati giriniz : ")
            if randevu_hastanead!=None and randevu_hastanepoliklinik!=None and randevu_doktorad!=None and randevu_tarih!=None and randevu_saat!=None :
                randevukayit(ad_bilgi,tel_bilgi,tc_bilgi,randevu_hastanead,randevu_hastanepoliklinik,randevu_doktorad,randevu_tarih,randevu_saat)
                print("randevunuz oluşturuldu")
            else:
                print("yanlış giriş yaptınız menüye yönlendiriliyorsunuz : ")

        elif sorgu==2:
            print("hangi randevuyu güncellemek istiyorsanız ona ait bilgileri giriniz . ")
            randevu_doktorad=input("Doktor adı giriniz : ")
            randevu_tarih=input("Randevu tarihi giriniz : ")
            randevu_saat=input("Randevu saati giriniz : ")
            onay=int(guncelara(tc_bilgi,randevu_doktorad,randevu_tarih,randevu_saat))
            if onay==1:
                print("YENİ BİLGİLERİ GİR")
                randevu_hastanead=input("Hastane adı giriniz : ")
                randevu_hastanepoliklinik=input("Poliklinik giriniz : ")
                randevu_doktorad=input("Doktor adı giriniz : ")
                randevu_tarih=input("Randevu tarihi giriniz : ")
                randevu_saat=input("Randevu saati giriniz : ")
                randevuguncelle(ad_bilgi,tel_bilgi,tc_bilgi,randevu_hastanead,randevu_hastanepoliklinik,randevu_doktorad,randevu_tarih,randevu_saat)
                print("randevunuz güncellendi")
            else: 
                print("bu bilgilere sahip randevu bulunamadı . ")  

        elif sorgu==3:              
            print("hangi randevuyu silmek istiyorsanız ona ait bilgileri giriniz . ")
            randevu_doktorad=input("Doktor adı giriniz : ")
            randevu_tarih=input("Randevu tarihi giriniz : ")
            randevu_saat=input("Randevu saati giriniz : ")
            onay=int(silmeara(tc_bilgi,randevu_doktorad,randevu_tarih,randevu_saat))
            print("a")
            if onay==1:
                randevusilme(tc_bilgi,randevu_doktorad,randevu_tarih,randevu_saat)
                print("randevunuz silindi")
            else: 
                print("bu bilgilere sahip randevu bulunamadı . ")  

        elif sorgu==4:
            liste=listele(ad_bilgi,tel_bilgi,tc_bilgi)
            if liste!=None:
                print("Sayın {} , Randevu bilgileriniz ; Hastane adı : {} , Poliklinik : {} , Doktor adı : {} , Tarih : {} , Saat : {} ".format(liste[1],liste[3],liste[4],liste[5],liste[6],liste[7]))
            else:
                print("malesef randevunuz bulunamadı")
        elif sorgu==5:
            break
        else:
            print("düzgün tuşlayınız")

if istemci==2:
    while 1:
        sorgu=int(doktormenu())
        if sorgu==1:
            print("hangi randevuyu silmek istiyorsanız ona ait bilgileri giriniz . ")
            randevu_tarih=input("Randevu tarihi giriniz : ")
            randevu_saat=input("Randevu saati giriniz : ")
            onay=int(doktorsilmeara(ad_bilgi,randevu_tarih,randevu_saat))
            print("a")
            if onay==1:
                doktorrandevusilme(ad_bilgi,randevu_tarih,randevu_saat)
                print("randevunuz silindi")
            else: 
                print("bu bilgilere sahip randevu bulunamadı . ")  

        elif sorgu==2:
            dosya2=open("uyelik.txt","r")
            sayi=dosya2.read()
            print("şu ana kadar üye olan kişi sayısı : {}".format(sayi))
            dosya2.close()
            
        else:
            break