import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import tkinter as tk 



class app:
    
    def __init__(self):
        self.janela = tk.Tk("teste")
        self.df = pd.read_csv("diabetes.csv").drop(["DiabetesPedigreeFunction"], axis=1)
        self.X = self.df[self.df.columns[:-1]].values
        self.y = self.df[self.df.columns[-1]].values
        X_train, X_test, y_train, y_test = train_test_split(self.X, self.y)
        self.svm_model = SVC()
        self.svm_model.fit(X_train, y_train)
        self.configuracao()
        self.texto(self.janela)


        self.janela.mainloop()
    
    def configuracao(self):
        self.janela.title("Janela_da_Cori")
        self.janela.geometry("400x400")
    
    def texto(self, window):
        self.titulo = tk.Label(window, text="IA PARA PREVER DIABETES", font=('Arial', 16))
        self.titulo.place(x=50, y=10)
        self.lab_idade = tk.Label(window, text="idade")
        self.lab_idade.place(x=115, y=60)
        self.idade = tk.Entry(window, width=20)
        self.idade.place(x=150, y=60)

        self.lab_gestacao = tk.Label(window, text="Numero de gestações")
        self.lab_gestacao.place(x=30, y=90)
        self.lab_entrygestacao = tk.Entry(window, width=20)
        self.lab_entrygestacao.place(x=150, y=90)

        self.lab_glicose = tk.Label(window, text="Glicose")
        self.lab_glicose.place(x=100, y=115)
        self.lab_entryglicose = tk.Entry(window, width=20)
        self.lab_entryglicose.place(x=150, y=115)

        self.lab_pressaosague = tk.Label(window, text="Pressão Sanguinea")
        self.lab_pressaosague.place(x=45, y=140)
        self.lab_entrypressaosangue = tk.Entry(window, width=20)
        self.lab_entrypressaosangue.place(x=150, y=140)

        self.lab_pele = tk.Label(window, text="Espessura da Pele")
        self.lab_pele.place(x=40, y=165)
        self.lab_entrypele = tk.Entry(window, width=20)
        self.lab_entrypele.place(x=150, y=165)

        self.lab_insulina = tk.Label(window, text="insulina")
        self.lab_insulina.place(x=100, y=190)
        self.lab_entryinsulina = tk.Entry(window, width=20)
        self.lab_entryinsulina.place(x=150, y=190)

        self.lab_imc = tk.Label(window, text="IMC")
        self.lab_imc.place(x=120, y=215)
        self.lab_entryimc = tk.Entry(window, width=20)
        self.lab_entryimc.place(x=150, y=215)


        self.botao_prever = tk.Button(window, text="Prever", width=5, height=2, command=self.iniciar)
        self.botao_prever.place(x=180, y=240)
        self.previsao = tk.Label(window, text="", font=('Arial', 12))
        self.previsao.place(x=100, y=300)
    
    def iniciar(self):
        
        self.array = np.array([float(self.idade.get()), float(self.lab_entrygestacao.get()), float(self.lab_entryglicose.get()), float(self.lab_entrypressaosangue.get()), float(self.lab_entrypele.get()), float(self.lab_entryinsulina.get()), float(self.lab_entryimc.get())]).reshape((1, -1))
        y_predict = self.svm_model.predict(self.array)

        if y_predict == 0: 
            self.previsao.configure(text="Não tem diabete")
        else:
            self.previsao.configure(text="tem diabete")

aplicativo = app()
