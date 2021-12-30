from tkinter import *
import os
import subprocess
from tkinter import scrolledtext    
parent = Tk()
parent.geometry("700x600")
path=os.getcwd()

txt = scrolledtext.ScrolledText(parent,width=80,height=30)
txt.place(x=20, y=60)


def saveJava():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./JAVA/Main.java"):
        os.remove("./JAVA/Main.java")
    fl = open("./JAVA/Main.java", "w")
    fl.write(stxt)
def RJava():
    os.chdir('./JAVA')
    os.system('docker build -t javaprogram .')
    os.system('docker run --rm -it javaprogram')
    os.chdir(path)


def saveCpp():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./c++/main.cpp"):
        os.remove("./c++/main.cpp")
    fl = open("./c++/main.cpp", "w")
    fl.write(stxt)
def RCpp():
    os.chdir('./c++')
    os.system('docker build -t cppprogram .')
    os.system('docker run --rm -it cppprogram')
    os.chdir(path)


def savePy():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./Python/main.py"):
        os.remove("./Python/main.py")
    fl = open("./Python/main.py", "w")
    fl.write(stxt)
def RPy():
    os.chdir('./Python')
    os.system('docker build -t pythonprogram .')
    os.system('docker run --rm -it pythonprogram')
    os.chdir(path)

def saveRuby():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./Ruby/main.rb"):
        os.remove("./Ruby/main.rb")
    fl = open("./Ruby/main.rb", "w")
    fl.write(stxt)
def RRuby():
    os.chdir('./Ruby')
    os.system('docker build -t rubyprogram .')
    os.system('docker run --rm -it rubyprogram')
    os.chdir(path)

def savePerl():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./Perl/main.pl"):
        os.remove("./Perl/main.pl")
    fl = open("./Perl/main.pl", "w")
    fl.write(stxt)
def RPerl():
    os.chdir('./Perl')
    os.system('docker build -t perlprogram .')
    os.system('docker run --rm -it perlprogram')
    os.chdir(path)

def savePHP():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./PHP/main.php"):
        os.remove("./PHP/main.php")
    fl = open("./PHP/main.php", "w")
    fl.write(stxt)
def RPHP():
    os.chdir('./PHP')
    os.system('docker build -t phplprogram .')
    os.system('docker run --rm -it phplprogram')
    os.chdir(path)

def saveRust():
    stxt=txt.get(1.0,END)
    if os.path.isfile("./Rust/main.rs"):
        os.remove("./Rust/main.rs")
    fl = open("./Rust/main.rs", "w")
    fl.write(stxt)
def RRust():
    os.chdir('./Rust')
    os.system('docker build -t rustlprogram .')
    os.system('docker run --rm -it rustlprogram')
    os.chdir(path)
savers=Button(parent,text="SRust",command=saveRust)
savers.grid(column=6,row=1)
runrs=Button(parent,text="RRust",command=RRust)
runrs.grid(column=6,row=2)

savej=Button(parent,text="SJAVA",command=saveJava)
savej.grid(column=0,row=1)
runj=Button(parent,text="RJAVA",command=RJava)
runj.grid(column=0,row=2)

savec=Button(parent,text="SC++",command=saveCpp)
savec.grid(column=1,row=1)
runc=Button(parent,text="RC++",command=RCpp)
runc.grid(column=1,row=2)

savep=Button(parent,text="SPython",command=savePy)
savep.grid(column=2,row=1)
runp=Button(parent,text="RPython",command=RPy)
runp.grid(column=2,row=2)

saver=Button(parent,text="SRuby",command=saveRuby)
saver.grid(column=3,row=1)
runr=Button(parent,text="RRuby",command=RRuby)
runr.grid(column=3,row=2)

savepl=Button(parent,text="SPerl",command=savePerl)
savepl.grid(column=4,row=1)
runpl=Button(parent,text="RPerl",command=RPerl)
runpl.grid(column=4,row=2)

savephp=Button(parent,text="SPHP",command=savePHP)
savephp.grid(column=5,row=1)
runphp=Button(parent,text="RPHP",command=RPHP)
runphp.grid(column=5,row=2)


parent.mainloop()