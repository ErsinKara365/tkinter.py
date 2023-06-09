import tkinter as tk
import base64 as bs
import time
from tkinter import messagebox as ms 

defaultFirst = open("defaultFirst", "r+" ).read()
defaultSecond = open("defaultSecond", "r+" ).read()


def bs_encode () :
    def geri_don ():
        bs_encode.withdraw()
        pen.deiconify()
    def metni_cevir():
        def kayit ():
            yeniisim =str(time.time())[1:10] + str(".txt")
            yeni = open(yeniisim,"w+")
            yeni.write(donus2)
            yeni.close()
            ms.showwarning("Kayit Edildi","{} olarak kayit edildi".format(yeniisim))
            
        donus2 = bs.b64encode(ustmetin.get(1.0, tk.END).encode("utf-8")).decode("utf-8")
        son_hali["text"] = donus2
        ustmetin.delete(1.0 , tk.END)

        kayit = tk.Button(bs_encode, text="Kaydet", bg="green", fg="red", command=kayit) 
        kayit.place(x=155,y=480)

    pen.withdraw() 
    bs_encode = tk.Toplevel()
    bs_encode.title("Base64 ile Şifrele")
    bs_encode.geometry("400x600+1000+100")

    anasayfa = tk.Button(bs_encode, text="Anasayfa", command=geri_don, bg="blue", fg="white" )
    anasayfa.place(x=155, y=10)
    
    ustmetin = tk.Text(bs_encode, width=45, height=10, wrap=tk.WORD, bg="white" , fg="black", pady=5, padx=5)
    ustmetin.place(x=10 ,y=50)

    cevir = tk.Button(bs_encode, text="Cevir", command=metni_cevir, bg="green", fg="black")
    cevir.place(x=155, y=280)

    son_hali = tk.Label(bs_encode, text="", wraplength=390)
    son_hali.place(x=10, y=310)

    

    
   
def bs_decode ():
    def geri_don ():
        bs_decode.withdraw()
        pen.deiconify()
    def metni_cevir():
        def kayit ():
            yeniisim =str(time.time())[1:10] + str(".txt")
            yeni = open(yeniisim,"w+")
            yeni.write(donus2)
            yeni.close()
            ms.showwarning("Kayit Edildi","{} olarak kayit edildi".format(yeniisim))
            
        donus2 = bs.b64decode(ustmetin.get(1.0, tk.END).encode("utf-8")).decode("utf-8")
    
        son_hali["text"] = donus2
        ustmetin.delete(1.0 , tk.END)

        kayit = tk.Button(bs_decode, text="Kaydet", bg="green", fg="red", command=kayit)
        kayit.place(x=155,y=480)

    pen.withdraw() 
    bs_decode = tk.Toplevel()
    bs_decode.title("Base64 ile Şifre Çöz")
    bs_decode.geometry("400x600+1000+100")

    anasayfa = tk.Button(bs_decode, text="Anasayfa", command=geri_don, bg="blue", fg="white" )
    anasayfa.place(x=155, y=10)
    
    ustmetin = tk.Text(bs_decode, width=45, height=10, wrap=tk.WORD, bg="white" , fg="black", pady=5, padx=5)
    ustmetin.place(x=10 ,y=50)

    cevir = tk.Button(bs_decode, text="Cevir", command=metni_cevir, bg="green", fg="black")
    cevir.place(x=155, y=280)

    son_hali = tk.Label(bs_decode, text="", wraplength=390)
    son_hali.place(x=10, y=310)

     
def benim_encode ():
    def geri_don ():
        bs_decode.withdraw()
        pen.deiconify()
    def metni_cevir():
        def kayit ():
            yeniisim =str(time.time())[1:10] + str(".txt")
            yeni = open(yeniisim,"w+")
            yeni.write(donus2)
            yeni.close()
            ms.showwarning("Kayit Edildi","{} olarak kayit edildi".format(yeniisim))
        try :
            
            kelime = ustmetin.get(1.0, tk.END)
            tamam = kelime.maketrans(defaultFirst , defaultSecond)
            donus2 = kelime.translate(tamam)     
                
            son_hali["text"] = donus2
            ustmetin.delete(1.0 , tk.END)
            kayit = tk.Button(bs_decode, text="Kaydet", bg="green", fg="red", command=kayit)
            kayit.place(x=155,y=480)
        except ValueError :
           son_hali["text"]= "Hata olustu\nKarakter Sayilari Uyuşmazliği olabilir \nilk metin -> {}\nikinci metin ->{} ".format(len(defaultFirst),len(defaultSecond))



    pen.withdraw() 
    bs_decode = tk.Toplevel()
    bs_decode.title("Benim Algoritma ile Şifrele")
    bs_decode.geometry("400x600+1000+100")

    anasayfa = tk.Button(bs_decode, text="Anasayfa", command=geri_don, bg="blue", fg="white" )
    anasayfa.place(x=155, y=10)
    
    ustmetin = tk.Text(bs_decode, width=45, height=10, wrap=tk.WORD, bg="white" , fg="black", pady=5, padx=5)
    ustmetin.place(x=10 ,y=50)

    cevir = tk.Button(bs_decode, text="Cevir", command=metni_cevir, bg="green", fg="black")
    cevir.place(x=155, y=280)

    son_hali = tk.Label(bs_decode, text="", wraplength=390)
    son_hali.place(x=10, y=310)

     
def benim_decode ():
    def geri_don ():
        bs_decode.withdraw()
        pen.deiconify()
    def metni_cevir():
        def kayit ():
            yeniisim =str(time.time())[1:10] + str(".txt")
            yeni = open(yeniisim,"w+")
            yeni.write(donus2)
            yeni.close()
            ms.showwarning("Kayit Edildi","{} olarak kayit edildi".format(yeniisim))

        try:
            kelime = ustmetin.get(1.0, tk.END)
            tamam = kelime.maketrans(defaultSecond , defaultFirst)
            donus2 = kelime.translate(tamam)   
        
            son_hali["text"] = donus2
            ustmetin.delete(1.0 , tk.END)
            kayit = tk.Button(bs_decode, text="Kaydet", bg="green", fg="red", command=kayit)
            kayit.place(x=155,y=480)
        except ValueError :
             son_hali["text"]= "Hata olustu\nKarakter Sayilari Uyuşmazliği olabilir \nilk metin -> {}\nikinci metin ->{} ".format(len(defaultFirst),len(defaultSecond))

       

    pen.withdraw() 
    bs_decode = tk.Toplevel()
    bs_decode.title("Benim Algoritma ile Şifre Çöz")
    bs_decode.geometry("400x600+1000+100")

    anasayfa = tk.Button(bs_decode, text="Anasayfa", command=geri_don, bg="blue", fg="white" )
    anasayfa.place(x=155, y=10)
    
    ustmetin = tk.Text(bs_decode, width=45, height=10, wrap=tk.WORD, bg="white" , fg="black", pady=5, padx=5)
    ustmetin.place(x=10 ,y=50)

    cevir = tk.Button(bs_decode, text="Cevir", command=metni_cevir, bg="green", fg="black")
    cevir.place(x=155, y=280)

    son_hali = tk.Label(bs_decode, text="", wraplength=390)
    son_hali.place(x=10, y=310)
    
    
    
        


    





pen = tk.Tk()
pen.geometry("300x350+1200+100")
pen.title("KRIPTO")

b_encode = tk.Button(pen, text="Base64 ile Şifrele", bg="green", fg="black", command=bs_encode,wraplength=80)
b_encode.place(x=35, y=50)

b_decode = tk.Button(pen, text="Base64 ile Şifre Çöz", bg="blue", fg="white", command=bs_decode,wraplength=80)
b_decode.place(x=150, y=50)

benim_encode = tk.Button(pen, text="Benim algoritma ile şifrele", bg="green", fg="black", wraplength=80, command=benim_encode)
benim_encode.place(x=35, y=115)

benim_decode = tk.Button(pen, text="Benim algoritma ile Şifre Çöz", bg="blue", fg="white", wraplength=80, command=benim_decode)
benim_decode.place(x=150, y=115)



tk.Label(pen, text="To be Continued!", fg="red").place(x=75, y=200)







pen.mainloop()
