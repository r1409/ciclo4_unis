from tkinter import *
from sqlite3 import *
path = r'C:\imc_rudieron'
conn = connect(path+'\dados.db')
c = conn.cursor()

prog = Tk()

prog.title("Cálculo do IMC - Índice de Massa Corporal")

bdResultN = StringVar()
bdResultN.set("IMC")

lbNome = Label(prog, text="Nome do Paciente:")
lbNome.place(x=20, y=20)

lbEnd = Label(prog, text="Endereço Completo:")
lbEnd.place(x=20, y=45)

lbAlt = Label(prog, text="Altura (0.00)")
lbAlt.place(x=20, y=70)

lbPeso = Label(prog, text="Peso (kg)")
lbPeso.place(x=20, y=95)

entNome = Entry(prog,  width=70)
entNome.place(x=150, y=20)

entEnd = Entry(prog, width=70)
entEnd.place(x=150, y=45)

entAlt = Entry(prog, width=20)
entAlt.place(x=150, y=70)

entPeso = Entry(prog, width=20)
entPeso.place(x=150, y=95)

def bt_click_calc():
    if(str(entAlt.get()).isascii() and str(entPeso.get()).isnumeric()):
        Alt = float(entAlt.get())
        Peso = int(entPeso.get())
        IMC = float(Peso / (Alt * Alt))
        lbResulN["text"] = round(IMC, 2)
        if IMC < 17:
            lbResulSit["text"] = "MUITO ABAIXo DO PESO"
            lbResulSit.config(bg="yellow")
            lbResulN.config(bg="yellow")
        elif IMC < 18.5:
            lbResulSit["text"] = "ABAIXO DO PESO"
            lbResulSit.config(bg="yellow")
            lbResulN.config(bg="yellow")
        elif IMC < 25:
            lbResulSit["text"] = "PESO NORMAL :)"
            lbResulSit.config(bg="green")
            lbResulN.config(bg="green")
        elif IMC < 30:
            lbResulSit["text"] = "ACIMA DO PESO"
            lbResulSit.config(bg="cyan")
            lbResulN.config(bg="cyan")
        elif IMC < 35:
            lbResulSit["text"] = "OBESIDADE I"
            lbResulSit.config(bg="magenta")
            lbResulN.config(bg="magenta")
        elif IMC < 40:
            lbResulSit["text"] = "OBESIDADE II (SEVERA)"
            lbResulSit.config(bg="magenta")
            lbResulN.config(bg="magenta")
        elif IMC >= 40:
            lbResulSit["text"] = "OBESIDADE III (MÓRBIDA)"
            lbResulSit.config(bg="red")
            lbResulN.config(bg="red")
        else:
            lbResulSit["text"] = "Situação"
    else:
        lbResulN["text"] = "Digite os valores de Altura e Peso corretamente."

    sql = '''CREATE TABLE IF NOT EXISTS Paciente
    (   pacienteNome VARCHAR(100),
        pacienteEmail VARCHAR(100),
        pacientePeso VARCHAR(100),
        pacienteAltura FLOAT,
        pacienteIMC FLOAT)'''
    c.execute(sql)
    c.execute('INSERT INTO Paciente (pacienteNome, pacienteEndereco, pacientePeso, pacienteAltura, pacienteIMC) VALUES ("' + entNome.get() + '",\
    "' + entEnd.get() + '","' + entPeso.get() + '","' + entAlt.get() + '","' + bdResultN.get()+'")')
    conn.commit()





def bt_click_reini():
    entNome.delete(0, END)

    entEnd.delete(0, END)

    entAlt.delete(0, END)

    entPeso.delete(0, END)

    lbResulN.config(text="-", bg="gray")

    lbResulSit.config(text="Informe os dados", bg="gray")


def bt_click_sair():
    prog.quit()



btCalc = Button(prog, width=15, text="Calcular", command=bt_click_calc)
btCalc.place(x=20, y=310)

btSair = Button(prog, width=15, text="Sair", command=bt_click_sair)
btSair.place(x=468, y=310)

btReini = Button(prog, width=15, text="Reiniciar", command=bt_click_reini)
btReini.place(x=150, y=310)

lbResulN = Label(prog, text="IMC", width=11, height=5, bg="gray", font="arial 20 bold")
lbResulN.place(x=390, y=130)

lbResulSit = Label(prog, text="SITUAÇÃO", width=20, height=5, bg="gray", font="arial 20 bold")
lbResulSit.place(x=20, y=130)


prog.geometry("600x350+350+100")


#def cadastro_imc_BD():
#    sql = '''CREATE TABLE IF NOT EXISTS Paciente
#    (   pacienteNome VARCHAR(100),
#        pacienteEmail VARCHAR(100),
#        pacientePeso VARCHAR(100),
#        pacienteAltura FLOAT,
#        pacienteIMC FLOAT)'''
#    c.execute(sql)
#    c.execute('INSERT INTO Paciente (pacienteNome, pacienteEndereco, pacientePeso, pacienteAltura, pacienteIMC) VALUES ("' + entNome.get() + '",\
#    "' + entEnd.get() + '","' + entPeso.get() + '","' + entAlt.get() + '","' + bdResulN.get()+'")')

#    conn.commit()

prog.mainloop()