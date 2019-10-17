import kivy
import random
import numpy as np
import matplotlib.pyplot as plt

from kivy.app import App
from sympy import Symbol
from sympy import integrate
from kivy.lang import Builder
from kivy.uix.widget import Widget
from mpl_toolkits.mplot3d import Axes3D
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from math import sin,cos
from kivy.garden.graph import Graph, MeshLinePlot
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty

kivy.require('1.9.0')
Builder.load_file('main.kv')


class Ventana_Menu(Screen):
    pass


class EUOptionWindow(Screen):
    pass


class EFOptionWindow(Screen):
    pass


class EUNormType(Screen, Widget):
    def inputN(self):

        nParsed = int(self.n.text)
        pParsed = int(self.p.text)

        menor_valor = -500
        mayor_valor = 500

        arr = np.zeros(nParsed)

        for i in range(nParsed):
            valor_aleatorio = random.randint(menor_valor, mayor_valor)
            arr[i] = valor_aleatorio

        # TIPOS DE NORMA
        # |X|1
        # Norma de la Suma
        x1 = np.linalg.norm(arr, 1)
        # |X|2
        # Norma Euclidiana
        x2 = np.linalg.norm(arr, 2)
        # |X|inf
        # Norma del Maximo
        x3 = np.linalg.norm(arr, np.inf)
        # |X|p
        # Norma P
        xp = np.linalg.norm(arr, pParsed)

        self.output_vector.text = str(arr)
        self.output_x1.text = str(x1)
        self.output_x2.text = str(x2)
        self.output_x3.text = str(x3)
        self.output_xp.text = str(xp)


class Producto_Vectorial (Screen, Widget):
    def inputN(self):

        x1Parsed = int(self.x1.text)
        x2Parsed = int(self.x2.text)
        x3Parsed = int(self.x3.text)
        y1Parsed = int(self.y1.text)
        y2Parsed = int(self.y2.text)
        y3Parsed = int(self.y3.text)

        vector_1 = [x1Parsed, x2Parsed, x3Parsed]
        vector_2 = [y1Parsed, y2Parsed, y3Parsed]

        sub_mat_i = ([x2Parsed, x3Parsed], [y2Parsed, y3Parsed])
        sub_mat_j = ([x1Parsed, x3Parsed], [y1Parsed, y3Parsed])
        sub_mat_k = ([x1Parsed, x2Parsed], [y1Parsed, y2Parsed])

        i = (np.linalg.det(sub_mat_i))*1
        j = (np.linalg.det(sub_mat_j))*-1
        k = (np.linalg.det(sub_mat_k))*1

        self.output_i.text = str(i)
        self.output_j.text = str(j)
        self.output_k.text = str(k)


class Grafico_N_R2 (Screen):
    graph = ObjectProperty(None)

    def Create_Graph(self):
        n = int(self.p.text)
        if ((n % 2) == 0):
            list_b = []
            i = -1
            while i < 1:
                list_b.append(i)
                i = i + 0.1
            data = [(x, (abs(1-(x**n)))**(1/n)) for x in list_b]
            data += [(x, ((abs(1-(x**n)))**(1/n)*-1)) for x in list_b]

        else:
            list_a = []
            i = -4
            while i < 1:
                list_a.append(i)
                i = i + 0.1

            list_b = []
            i = 1
            while i < 4:
                list_b.append(i)
                i = i + 0.1

            data = [(x, (abs(1-(x**n)))**(1/n)) for x in list_a]
            data += [(x, ((abs(1-(x**n)))**(1/n))*-1) for x in list_b]

        plot = MeshLinePlot(color=[1, 0, 0, 1])
        plot.points = data
        self.graph.add_plot(plot)


class Producto_Interno (Screen, Widget):
    def inputN(self):

        nParsed = int(self.n.text)
        vector_x = np.zeros(nParsed)
        vector_y = np.zeros(nParsed)
        menor_valor = -10
        mayor_valor = 10
        resultado = 0

        for i in range(nParsed):
            valor_aleatorio = random.randint(menor_valor, mayor_valor)
            vector_x[i] = valor_aleatorio

        for i in range(nParsed):
            valor_aleatorio = random.randint(menor_valor, mayor_valor)
            vector_y[i] = valor_aleatorio

        print(vector_x)
        print(vector_y)

        for i in range(nParsed):
            resultado = vector_x[i]*vector_y[i]+resultado
            print(vector_x[i]*vector_y[i])
        print(resultado)

        self.output_vector_x.text = str(vector_x)
        self.output_vector_y.text = str(vector_y)
        self.output_resultado.text = str(resultado)


class Producto_Mixto (Screen, Widget):
    def inputN(self):

        x1Parsed = int(self.x1.text)
        x2Parsed = int(self.x2.text)
        x3Parsed = int(self.x3.text)
        y1Parsed = int(self.y1.text)
        y2Parsed = int(self.y2.text)
        y3Parsed = int(self.y3.text)
        z1Parsed = int(self.z1.text)
        z2Parsed = int(self.z2.text)
        z3Parsed = int(self.z3.text)

        matriz = ([x1Parsed, x2Parsed, x3Parsed], [
                  y1Parsed, y2Parsed, y3Parsed], [z1Parsed, z2Parsed, z3Parsed])

        resultado = (np.linalg.det(matriz))

        self.output_resultado.text = str(resultado)


class Grafico_N_R3 (Screen):
    def inputN(self):

        pParsed = int(self.p.text)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = y = np.arange(-3.0, 3.0, 0.01)
        X, Y = np.meshgrid(x, y)
        zs = np.array([abs(x)**pParsed + abs(y)**pParsed for x,
                       y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)
        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_zlabel('Eje Z')

        plt.show()


class Producto_Interno_Funciones_Continuas(Screen, Widget):
    def inputN(self):

        fParsed = str(self.f.text)
        gParsed = str(self.g.text)
        aParsed = int(self.a.text)
        bParsed = int(self.b.text)
        
        print(fParsed)
        print(gParsed)
        print(aParsed)
        print(bParsed)

        inte = int(self.fParsed)*int(self.gParsed)
        print (inte)
      


class Norma_Espacio_Funciones_Continuas(Screen):
    pass


screen_manager = ScreenManager()

screen_manager.add_widget(Ventana_Menu(name="main_window"))
screen_manager.add_widget(EUOptionWindow(name="eu_option_window"))
screen_manager.add_widget(EUNormType(name="eu_norm_type"))
screen_manager.add_widget(EFOptionWindow(name="ef_option_window"))
screen_manager.add_widget(Producto_Vectorial(name="vectorial"))
screen_manager.add_widget(Grafico_N_R2(name="grafico_r2"))
screen_manager.add_widget(Producto_Interno(name="interno"))
screen_manager.add_widget(Producto_Mixto(name="mixto"))
screen_manager.add_widget(Grafico_N_R3(name="grafico_r3"))
screen_manager.add_widget(
    Producto_Interno_Funciones_Continuas(name="interno_funciones"))
screen_manager.add_widget(
    Norma_Espacio_Funciones_Continuas(name="norma_funciones"))


class CalculoNumericoApp(App):
    def build(self):
        self.title = 'Calculo Numerico Proyecto 1, 2019'
        return screen_manager


sample_app = CalculoNumericoApp()
sample_app.run()
