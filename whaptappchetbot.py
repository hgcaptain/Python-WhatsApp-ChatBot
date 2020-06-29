from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import os 
import pyautogui 
import clipboard 
import time 
import sqlite3 

def copy ()  :
    pyautogui.doubleClick(560,765)
    pyautogui.click(560,765) 
    pyautogui.hotkey("ctrl", "c")


bulusmaVerisi = sqlite3.connect("bulusmaİstekleri.sqlite")
konusmaVerisi = sqlite3.connect("konusmaİstekleri.sqlite") 

imA = bulusmaVerisi.cursor() 
imB = konusmaVerisi.cursor() 

def bulusma ()  :
    mesajlist = []
    bbosluk = gelenMesaj.split() 
    mesajlist.append(bbosluk)
    imA.execute("CREATE TABLE IF NOT EXISTS bulusmaİstekleri (isim, soyisim , tarih" )
    imA.execute("INSERT INTO bulusmaİstekleri VALUES (mesajlist[0],mesajlist[1],mesajlist[2]")


def konusma ()  :
    mesajlist1 =[] 
    kbosluk = gelenMesaj.split()
    mesajlist1.append(kbosluk) 
    imB.execute("CREATE TABLE IF NOT EXISTS konusmaİstekleri (isim, soyisim " )
    imB.execute("INSERT INTO konusmaİstekleri VALUES (mesajlist1[0],mesajlist1[1]")


    


os.startfile("geckodriver.exe") 

driver = webdriver.Firefox() 
driver.get("https://web.whatsapp.com/" ) 

wait = WebDriverWait(driver, 600)
driver.maximize_window()

driver.switch_to_window(driver.window_handles[0])
input("Kare Kod okuttuktan sonra Enter'a basınız.") 

mode = input("1-Spam mode \n 2-Auto mode" ) 

if int(mode) ==  1  :
    while True : 
       
        isim = input("Kime mesaj yollamak istiyosunuz ? ") 
        mesaj = input("Mesajda ne yazmasını istiyorsunuz ?")
        sayac = input("Mesajı kaç kez göndermek istiyorsunuz ? ") 
        sayı = 0 
       
        while sayı < int(sayac)  :
           
            grup = driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
            grup.click()
            box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]") 
            box.send_keys(mesaj + Keys.ENTER)
            sayı += 1 
        print("Gönderme işlemi başarılı :)" ) 
        tercih = input("Başka bir mesaj yollamak istiyor musunuz ? E/H")  

        if tercih == "E" : 
            continue 

        elif tercih == "H"  :
            break 

        else : 
            print("Lütfen belirtilen komutlardan birini giriniz :) ")  
            
            
elif int(mode) == 2 : 
    isim = input("Otomatik modu kimin için açmak istiyorsunuz ?") 
    grup = driver.find_element_by_xpath('//span[@title = "{}"]'.format(isim))
    grup.click()
    

    while True  : 
        
        
        copy()
        gelenMesaj = clipboard.paste() 

        while True : 
            if gelenMesaj != ""  :
                break 
        
        print("Mesaj kopyalandı") 
        print(gelenMesaj) 

        if gelenMesaj.lower() == "nasılsın" or gelenMesaj.lower() == "merhaba" : 
            gidecekMesaj = "Merhaba ben Berke bey tarafından geliştirilmiş bir bot olan SPAK. Berke bey şu an müsait değil size ben yardımcı olacağım :) . Eğer sadece Nasılsın diye sormak için yazdıysanız bilinki iyi. Sohbet için yazdıysanız 1'e , Bir buluşma ayarlamak için yazdıysanız 2'ye basıp yollayın :)  " 
            box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]") 
            box.send_keys(gidecekMesaj + Keys.ENTER)
            time.sleep(20) 
            
            

        elif gelenMesaj == "1"  :
            gidecekMesaj = "Ona haber vereceğim en kısa zamanda size dönecektir :)" 
            box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]") 
            box.send_keys(gidecekMesaj + Keys.ENTER)
            konusma() 


        elif gelenMesaj == "2"  :
            gidecekMesaj = "Tarih ve zamanı yazın ben ona ileteceğim :)" 
            box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]") 
            box.send_keys(gidecekMesaj + Keys.ENTER)
            bulusma() 
       

        else  :
            gidecekMesaj = "Üzgünüm Berke Bey beni hala bu mesaja cevap verecek şekilde programlamadı :(" 
            box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]") 
            box.send_keys(gidecekMesaj + Keys.ENTER)
      


            



        











