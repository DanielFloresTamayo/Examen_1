from tkinter import *

def perimetro():
    
    lbllado1=Label(ventana,text="Ingrese la medida del lado: "+ entradaL.get(),
                   font=("Agency FB",14)).place(x=10,y=150)
    txtLad1=Entry(ventana,textvariable=entradaL).place(x=10,y=200)

    lbllad2=Label(text="Ingrese el numero de lados: "+ entradaN.get(),
                  font=("Agency FB",14)).place(x=10,y=220)
    txtLad2=Entry(ventana,textvariable=entradaN).place(x=10,y=250)
    bnt3 = Button(ventana, text="Calcular perímetro",command=calculoper,font=("Agency FB",14),
              width = 35).place(x=100,y=300)
    bnt4 = Button(ventana, text="Calcular área",command=calculoper,font=("Agency FB",14),
              width = 35).place(x=100,y=350)
def calculoper():
    resultado=StringVar()
    entradaN*entradL
    return resultado
    lbllado1=Label(ventana,text="Ingrese la medida del lado: "+ entradaL.get(),
                   font=("Agency FB",14)).place(x=10,y=150)
    txtLad1=Entry(ventana,textvariable=entradaL).place(x=10,y=200)

    lbllad2=Label(text="Ingrese el numero de lados: "+ entradaN.get(),
                  font=("Agency FB",14)).place(x=10,y=220)
    txtLad2=Entry(ventana,textvariable=entradaN).place(x=10,y=250)
    
ventana = Tk()
ventana.geometry("640x480+100+100")
ventana.title("CALCULADORA")

entradaN=StringVar()
entradaL=StringVar()

ventana.title("Calcular el area y perimetro")

bnt1 = Button(ventana, text="Opcion1",command=perimetro,font=("Agency FB",14),
              width = 10).place(x=300,y=20)
bnt2 = Button(ventana, text="Opcion2",font=("Agency FB",14),
              width = 10).place(x=300,y=70)

ventana.mainloop()
