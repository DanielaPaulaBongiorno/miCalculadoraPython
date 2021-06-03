import tkinter as tk
from tkinter.constants import END 

i=0

def convertir(dato):
    if dato.isdecimal() == False:
        dato = "error"
    else:
        dato = int(dato)
    return dato
def click(num):
    global i
    cresul.insert(i, num)
    i += 1
    return
def delet():
    cresul.delete(0, END)
    i=0

def operar():
    ecuacion = cresul.get()
    resultado = eval(ecuacion)
    cresul.delete(0, END)
    cresul.insert(0, resultado)
    i=0
def cerrar():
    exit()

ventana = tk.Tk()
ventana.title("Calculadora")
ventana.config(height=430,width=370)
ventana.config(background="Skyblue4")

bc = tk.Button(text="Cerrar", width=10, height=3, bg="white", fg="blue", command=lambda:cerrar())
bc.place(x=20,y=40)

b7 = tk.Button(text="7", width=10, height=3, bg="white", command=lambda:click(7))
b7.place(x=20,y=100)

b8 = tk.Button(text="8", width=10, height=3, bg="white", command=lambda:click(8))
b8.place(x=105,y=100)

bmas = tk.Button(text="+", width=10, height=3, bg="gray", fg="white", command=lambda:click("+"))
bmas.place(x=105,y=40)

b9 = tk.Button(text="9", width=10, height=3, bg="white", command=lambda:click(9))
b9.place(x=190,y=100)

bmenos = tk.Button(text="-", width=10, height=3, bg="gray", fg="white", command=lambda:click("-"))
bmenos.place(x=190,y=40)

bx = tk.Button(text="X", width=10, height=3, bg="gray", fg="white", command=lambda:click("x"))
bx.place(x=275,y=100)

bdividir = tk.Button(text="/", width=10, height=3, bg="gray", fg="white", command=lambda:click("/"))
bdividir.place(x=275,y=40)

b4 = tk.Button(text="4", width=10, height=3, bg="white", command=lambda:click(4))
b4.place(x=20,y=160)

b5 = tk.Button(text="5", width=10, height=3, bg="white", command=lambda:click(5))
b5.place(x=105,y=160)

b6 = tk.Button(text="6", width=10, height=3, bg="white", command=lambda:click(6))
b6.place(x=190,y=160)

bporcentaje = tk.Button(text="%", width=10, height=3, bg="gray", fg="white", command=lambda:click("%"))
bporcentaje.place(x=275,y=160)

b1 = tk.Button(text="1", width=10, height=3, bg="white", command=lambda:click(1))
b1.place(x=20,y=220)

b2 = tk.Button(text="2", width=10, height=3, bg="white", command=lambda:click(2))
b2.place(x=105,y=220)

b3 = tk.Button(text="3", width=10, height=3, bg="white", command=lambda:click(3))
b3.place(x=190,y=220)

bdele = tk.Button(text="cls", width=10, height=3, bg="gray", fg="white", command=lambda:delet())
bdele.place(x=275,y=220)

b0 = tk.Button(text="0", width=22, height=3, bg="white", command=lambda:click(0))
b0.place(x=20,y=280)

bigual = tk.Button(text="=", width=10, height=3, bg="gray", fg="white", command=lambda:operar())
bigual.place(x=275,y=280)

bdecimal = tk.Button(text=".", width=10, height=3, bg="gray", fg="white", command=lambda:click("."))
bdecimal.place(x=190,y=280)


cresul = tk.Entry(text="", font="Arial 25")
cresul.place(x=20,y=350, width=335, height=50)




ventana.mainloop()