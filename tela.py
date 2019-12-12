from tkinter import *

import principal


class Application:
    def __init__(self, master=None):
        self.fonte1 = ("Arial"), ("10")

        self.espaco1 = Frame(master)
        self.espaco1["pady"] = 10
        self.espaco1.pack()

        self.espaco12 = Frame(master)
        self.espaco12["padx"] = 20
        self.espaco12.pack()

        self.espaco13 = Frame(master)
        self.espaco13["padx"] = 20
        self.espaco13.pack()

        self.espaco2 = Frame(master)
        self.espaco2["padx"] = 20
        self.espaco2.pack()

        self.espaco3 = Frame(master)
        self.espaco3["padx"] = 20
        self.espaco3.pack()

        self.espaco4 = Frame(master)
        self.espaco4["padx"] = 20
        self.espaco4.pack()

        self.espaco5 = Frame(master)
        self.espaco5["padx"] = 20
        self.espaco5.pack()

        self.espaco6 = Frame(master)
        self.espaco6["padx"] = 20
        self.espaco6.pack()

        self.nome = Label(self.espaco1, text="CALCULO DO IMC-Indice de massa corporal")
        self.nome["font"] = ("Arial", "10", "bold")
        self.nome.pack()

        self.nome1Label = Label(self.espaco12, text="NOME DO PACIENTE", font=self.fonte1)
        self.nome1Label.pack(side=LEFT)

        self.nome1 = Entry(self.espaco12)
        self.nome1["width"] = 30
        self.nome1["font"] = self.fonte1
        self.nome1.pack(side=LEFT)

        self.nome2Label = Label(self.espaco13, text="ENDERECO COMPLETO:", font=self.fonte1)
        self.nome2Label.pack(side=LEFT)

        self.nome2 = Entry(self.espaco13)
        self.nome2["width"] = 33
        self.nome2["font"] = self.fonte1
        self.nome2.pack(side=LEFT)

        self.digitoLabel = Label(self.espaco2, text="PESO", font=self.fonte1)
        self.digitoLabel.pack(side=LEFT)

        self.digito = Entry(self.espaco2)
        self.digito["width"] = 17
        self.digito["font"] = self.fonte1
        self.digito.pack(side=LEFT)

        self.digito2Label = Label(self.espaco3, text="ALTURA", font=self.fonte1)
        self.digito2Label.pack(side=LEFT)

        self.digito2 = Entry(self.espaco3)
        self.digito2["width"] = 19
        self.digito2["font"] = self.fonte1
        self.digito2.pack(side=LEFT)

        # Desifindo a caixa de texto "IMC"
        self.imcLabel = Label(self.espaco4, text="IMC", font=self.fonte1)
        self.imcLabel.pack(side=LEFT)

        self.imcValor = Label(self.espaco5, text="", font=self.fonte1)
        self.imcValor.pack(side=RIGHT)

        # Definindo o botao
        self.calcular = Button(self.espaco6)
        self.calcular["text"] = "CALCULAR"
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["width"] = 12
        self.calcular["command"] = self.calcula
        self.calcular.pack()

    # Calculando
    def calcula(self):
        if self.nome1.get() == "" or self.nome2.get() == "" or self.digito.get() == "" or self.digito2.get() == "":
           self.imcValor["text"] = "Digite todos os dados"
        else:
                peso = self.digito.get()
                altura = self.digito2.get()
                resp = (float(peso)) / (float(altura) * float(altura))
                principal.create(self.nome1.get(), self.nome2.get(), self.digito.get(), self.digito2.get(), resp)
                if peso:
                    self.imcValor["text"] = resp


root = Tk()
Application(root)
root.mainloop()

#principal.read()