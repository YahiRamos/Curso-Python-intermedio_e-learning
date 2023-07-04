from tkinter import * 
#Ventana principal
Window=Tk()
Window.title("Interface_Prueba")
Window.config(bg="#20B2AA")
#Frame
fr=Frame()
fr.pack()
fr.config(bg="#3CB371")
fr.config(width="300",height="500")
fr.config(bd=10)
fr.config(relief="ridge")
#Agregaremos un label y una imagen
#label
lbl=Label(fr,text="Texto en la interface", font=("Cooper Black",17),bg="#3CB371")
lbl.grid(row=0,column=0)
#imagen
img=PhotoImage(file="python.png")
Label(fr,image=img,).grid(row=1,column=0,)
#Ahora agregaremos un cuadro para que puedan introducir datos
cuadroname=Entry(fr)
cuadroname.grid(row=5,column=0,sticky="e")
#
cuadroapellido=Entry(fr)
cuadroapellido.grid(row=6,column=0,sticky="e")
#
cuadrotel=Entry(fr)
cuadrotel.grid(row=7,column=0,sticky="e")
#crearemos un label para que sea el titulo de la caja de texto
lblname=Label(fr,text="Nombre:",bg="#3CB371",)
lblname.grid(row=5,column=0,sticky="w")
#
lblapellido=Label(fr,text="Apellidos:",bg="#3CB371")
lblapellido.grid(row=6,column=0,sticky="w")
#
lbltel=Label(fr,text="Telefono:",bg="#3CB371")
lbltel.grid(row=7,column=0,sticky="w")
#Pondrémos la función text con su label
lblcom=Label(fr,text="Comentario:",bg="#3CB371")
lblcom.grid(row=8,column=0,sticky="w")
#
txtcom=Text(fr,width=15,height=5)
txtcom.grid(row=8,column=0,sticky="e")
#Finalmente Crearemos un boton de envio
btnenvio=Button(Window,text="Enviar",width=38,height=5)
btnenvio.pack()

Window.mainloop()