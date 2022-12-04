from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
def connect():
    try:
        urllib.request.urlopen('http://google.com') 
        return True
    except:
        return False

    
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)





def Tikla():
    if connect() == True:
        gun=gunSecimi.get()
        ay=aySecimi.get()
        yil=yilSecimi.get()
        
        
    
        
        
        driver.get("https://www.x-rates.com/historical/?from=USD&amount=1&date={}-{}-{}".format(yil,ay,gun))
        driver.implicitly_wait(5)
        dolar=driver.find_element("xpath",'/html/body/div[2]/div/div[3]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[52]/td[2]/a').text
        driver.get("https://www.x-rates.com/historical/?from=EUR&amount=1&date={}-{}-{}".format(yil,ay,gun))
        euro=driver.find_element("xpath",'/html/body/div[2]/div/div[3]/div[1]/div/div[1]/div[1]/table[2]/tbody/tr[51]/td[2]/a').text 
        driver.get("https://altin.in/arsiv/{}/{}/{}".format(yil,ay,gun))
        altin=driver.find_element("xpath",'/html/body/div[4]/div[1]/div[2]/div[11]/ul/li[2]').text

        veriGirisi=Entry(sayfa,width=17,font=("Arial",10))
        veriGirisi.grid(row=6,column=1)
        veriGirisi.insert(0,altin)

        veriGirisi=Entry(sayfa,width=17,font=("Arial",10))
        veriGirisi.grid(row=7,column=1)
        veriGirisi.insert(0,dolar)

        veriGirisi=Entry(sayfa,width=17,font=("Arial",10))
        veriGirisi.grid(row=8,column=1)
        veriGirisi.insert(0,euro)
    else:
        messagebox.showerror("showerror", "İnternet Bağlantınız Yok")
        




sayfa=Tk()

sayfa.title("Döviz Kuru")
sayfa.iconbitmap('C:\\Users\\NigraSpe\\Desktop\\BTK\\Proje\\dollar.ico')
sayfa.geometry("400x200")
gun=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
gunSecimi = ttk.Combobox(sayfa,state="readonly", width = 17,values=gun)
  
# Adding combobox drop down list

  
gunSecimi.grid(column = 1, row = 0)
L1 = Label(sayfa, text="Gun girin: ")
L1.grid(column=0,row=0)
ay=['01', '02',
                          '03',
                          '04',
                          '05',
                          '06',
                          '07',
                          '08',
                          '09',
                          '10',
                          '11',
                          '12'] 
aySecimi = ttk.Combobox(sayfa, state="readonly", width = 17,values=ay)
  
# Adding combobox drop down list

  
aySecimi.grid(column = 1, row = 1)
L2 = Label(sayfa, text="Ay girin: ")
L2.grid(column=0,row=1)


L3 = Label(sayfa, text="Yıl girin: ")
L3.grid(column=0,row=2)
yil=['2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022']
yilSecimi = ttk.Combobox(sayfa, state="readonly",width = 17,values=yil)
  
# Adding combobox drop down list

  
yilSecimi.grid(column = 1, row = 2)

altınLabel=Label(sayfa,text="Altın:")
dolarLabel=Label(sayfa,text="Dolar:")
euroLabel=Label(sayfa,text="Euro:")
altınLabel.grid(column=0,row=6, )
dolarLabel.grid(column=0,row=7, )
euroLabel.grid(column=0,row=8, )



buton= Button(sayfa,text="Değerleri Getir",command=Tikla,font=("Arial", 10))
buton.grid(row=5,column=1)





sayfa.mainloop()