from tkinter import * 
from tkinter import ttk

class hapus:
    def restart():
        if Year.get() == '':
            eror.destroy()
            tombolrefresh['state']=DISABLED
            gas['state']=NORMAL
            pilih['state']="readonly"
        elif jawaban :
            jawaban.destroy()
            tombolrefresh['state']=DISABLED
            gas['state']=NORMAL
            
        else:
            pass

def exit():
    top.destroy()
        
def hilangin():
    hapus.restart()

def submit():
    if Year.get() == '':
        global eror
        eror = Label(top, text="ERROR!", bg='black', fg='red',  font=('Times New Roman',12,'bold'))
        eror.place(x=170,y=110)
        tombolrefresh['state']=NORMAL
        gas['state']=DISABLED
        pilih['state']=DISABLED
    else :
        global jawaban
        jawaban = Label(top, text="1 Ramadhan " + Year.get() + " H bertepatan dengan " + hitung(), font=('Times New Roman',12,'bold'))
        jawaban.place(x=13,y=112)
        tombolrefresh['state']=NORMAL
        gas['state']=DISABLED

def hitung():
    Y = int(Year.get())
    Y = Y-1
    A1 = Y//30
    A2 = Y%30

    if A2 == 0:
        x = 0
    if A2 == 1:
        x = 354
    if A2 == 2:
        x = 709
    if A2 == 3:
        x = 1063
    if A2 == 4:
        x = 1417
    if A2 == 5:
        x = 1772
    if A2 == 6:
        x = 2126
    if A2 == 7:
        x = 2481
    if A2 == 8:
        x = 2835
    if A2 == 9:
        x = 3189
    if A2 == 29:
        x = 10277

    A3 = A1*10631
    A4 = x
    A5 = 237+1
    A6 = A3+A4+A5
    A61 = A6+227016+13
    A7 = A61//1461
    A8 = A61%1461
    A9 = A7*4
    A10 = A8//365
    A11 = A8%365 
  
    if A11 == 17:
        B = 0
        D = 17
    if A11 == 29:
        B = 0
        D = 29
    if A11 == 40:
        B = 1
        D = 9
    if A11 == 50:
        B = 1
        D = 19
    if A11 == 61:
        B = 2
        D = 2
    if A11 == 72:
        B = 2
        D = 12   
    if A11 == 83:
        B = 2
        D = 24
    if A11 == 94:
        B = 3
        D = 4
    if A11 == 104:
        B = 3
        D = 14
    if A11 == 116:
        B = 3
        D = 25
    if A11 == 127:
        B = 4
        D = 7

    while (D==0):
       B = B-1
       D = 31

    if B == 0:
        B = 'Januari'
    if B == 1:
        B = 'Februari'
    if B == 2:
        B = 'Maret'
    if B == 3:
        B = 'April'
    if B == 4:
        B = 'Mei'
    
    BB = B
    DD = D-1
    dd = str(DD)
    Tahun = A9+A10+1
    tahun = str(Tahun)
    hasil = (dd + ' ' + BB + ' ' + tahun)
    return hasil

top = Tk()  
top.geometry("400x150")
top.title("Program Penentuan awal Ramadhan")

#label
bg = PhotoImage(file="D:\File Razmi\Sekolah\Kuliah\Semester\Semester 2\Prak. DKP\Tugas Akhir\part 1\\212.png")
monas = Label(top, image=bg)
tmii = bg.subsample(1,1)
monas.configure(image=tmii )
monas.place(x=0, y=0)

arab = PhotoImage(file="D:\\File Razmi\\Sekolah\\Kuliah\\Semester\\Semester 2\\Prak. DKP\\Tugas Akhir\\Ramadhan 1.png")
foto = Label(top, image=arab, bg='white')
foto.pack()
tmi = arab.subsample(8,6)
foto.configure(image=tmi )
foto.place(x=10, y=10)

tahun = Label(text = "Tahun :",bg='white', font=('Times New Roman',12)).place(x=120, y=52)
hijriyah = Label(text = "Hijriyah",bg='white', font=('Times New Roman',12)).place(x=240, y=52)
judul = Label(text = "PROGRAM PENENTUAN AWAL RAMADHAN", fg='white' ,bg='green', font=('Times New Roman', 12,'bold')).place(x=50, y=10)

#combobox
Year = StringVar(value='') 
pilih = ttk.Combobox(top, width = 6, textvariable = Year, state="readonly")
pilih.place(x=175, y=55)
pilih['values'] = ('1440','1441','1442','1443','1444','1445','1446','1447','1448','1449','1450')

#button
gas= Button(top, text="إرسال" , command=submit, borderwidth=3)
gas.pack()
gas.place(x=185,y=80)

refresh = PhotoImage(file="D:\File Razmi\Sekolah\Kuliah\Semester\Semester 2\Prak. DKP\Tugas Akhir\part 1\\restart.png")
tombolrefresh = Button(top, image=refresh, bg='white' , command=hilangin)
tombolrefresh.pack()
tmiii = refresh.subsample(25,25)
tombolrefresh.configure(image=tmiii )
tombolrefresh.place(x=300, y=55)
tombolrefresh['state']=DISABLED

fotos= PhotoImage(file="D:\\keluar.png")
keluar = Button(top, image=fotos, bg='white', command = exit, borderwidth=0)
tmiiii = fotos.subsample(25,25)
keluar.configure(image=tmiiii )
keluar.place(x=360, y=49)

top.mainloop() 
