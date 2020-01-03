import kivy
import random
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

from kivy.app import App
from sympy import Symbol
from sympy import integrate
from kivy.lang import Builder
from kivy.uix.widget import Widget
from mpl_toolkits.mplot3d import Axes3D
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from math import sin, cos
from matplotlib import cm
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
  
class MAOptionWindow(Screen, Widget): 
    def calcular(self):
        Ecuacion = self._ecuacion.text
        L = list(Ecuacion)
        LInf = int(self._LInf_.text)
        LSup = int(self._LSup_.text)
        Nparticiones = int(self._NParticiones_.text)

        
        def f(x):
            str1 = ""
            j = 0
            for j, item in enumerate(L):
                if item == "X":
                    L[j] = x
                    item = x
                if item == "^":
                    L[j] = '**'
                    item = '**'
                str1 += item
            return eval(str1)
        
        def rectangulos():
            i = 0
            a = LInf
            dx = (LSup-LInf)/Nparticiones
            resultado = 0
            vectorx = []
            vectordatos = []
            while a <= LSup :
                if a == LInf:
                    vectorx.append(a)
                    i = i+1
                    a = a+dx  
                if a == LSup:
                    a = a+dx   
                    i = i+1
                else:
                    vectorx.append(a) 
                    i = i+1
                    a = a+dx    

            #print (len(vectorx))
            for num in range(0,len(vectorx)):
                aux = vectorx[num]
                aux2 = f(aux)
                vectordatos.append(aux2)

            #print(vectordatos)
            aux4 = 0
            for num in range(0,len(vectordatos)):
                aux3 = vectordatos[num]
                aux4 = aux4 + aux3
                resultado = aux4
            
            resultado = resultado * dx
            #print (resultado)
            self._rectangulos_result.text = str(resultado)
        
        def rectangulosInf():
            i = 0
            a = LInf
            resultado = 0
            dx = (LSup-LInf)/Nparticiones
            vectorx = []
            vectordatos = []
            while a <= LSup:
                if a == LInf:
                    i = i+1
                    a =round( a+dx, 2)
                elif a == LSup:
                    vectorx.append(a)
                    a =round( a+dx, 2)
                    i = i+1
                else:
                    vectorx.append(a) 
                    i = i+1
                    a =round( a+dx, 2) 

            print ((vectorx))
            for num in range(0,len(vectorx)):
                aux = vectorx[num]
                aux2 = f(aux)
                vectordatos.append(aux2)

            #print(vectordatos)
            aux4 = 0
            for num in range(0,len(vectordatos)):
                aux3 = vectordatos[num]
                aux4 = aux4 + aux3
                resultado = aux4
            
            resultado = resultado * dx
            #print (resultado)
            self._rectangulosInf_result.text = str(resultado)
        
        def trapecios():
            a = LInf
            resultado = 0
            dx = (LSup-LInf)/(Nparticiones)
            dx2 = (LSup-LInf)/(2*Nparticiones)
            round(dx, 2)
            vectorx = []
            vectordatos = []
            while a <= LSup:
                if a == LInf:
                    vectorx.append(a)
                    a = round(a+dx, 2)
                else:
                    vectorx.append(a) 
                    a = round(a+dx, 2) 

            #print ((vectorx))
            i = 0
            for num in vectorx:
                aux = num
                if (aux == LSup or i == 0):
                    aux2 = f(aux)
                    i = i +1
                else:
                    aux = 2 * f(aux)
                    aux2 = aux

                vectordatos.append(aux2)

            #print(vectordatos)
            aux4 = 0
            for num in range(0,len(vectordatos)):
                aux3 = vectordatos[num]
                aux4 = aux4 + aux3
                resultado = aux4
            #print (resultado)
            
            resultado = resultado * dx2
            #print (resultado)
            self._trapecios_result.text = str(resultado)
        
        def simpson():
            a = LInf
            resultado = 0
            dx = (LSup-LInf)/Nparticiones
            vectorpar = []
            vectorpar2 = []
            vectorimpar = []
            vectorimpar2 = []
            primero:int
            ultimo:int
            primero = 0
            ultimo = 0
            i = 0

            while a <= LSup :
                if i%2 == 0:
                    if i == 0:
                        primero = a
                        i=i+1
                        a=a+dx
                    else:
                        vectorpar.append(a)
                        i = i+1
                        a = a+dx
                        
                else: 
                    vectorimpar.append(a) 
                    i = i+1
                    a = a+dx    
            if a > LSup :
                ultimo = a
            
            primero = f(primero)
            ultimo = f(ultimo)
            for num in range(0,len(vectorpar)):
                aux = vectorpar[num]
                aux2 = f(aux)
                vectorpar2.append(aux2)
            for num in range(0,len(vectorimpar)):
                aux = vectorimpar[num]
                aux2 = f(aux)
                vectorimpar2.append(aux2)

            aux4 = 0
            aux5 = 0
            aux6 = 0
            for num in range(0,len(vectorpar2)):
                aux3 = vectorpar2[num]
                aux4 = aux4 + aux3
                pares = aux4
            for num in range(0,len(vectorimpar2)):
                aux5 = vectorimpar2[num]
                aux6 = aux6 + aux5
                impares = aux6

            resultado = (4*impares+2*pares+primero + ultimo) * dx/3
           
            self._simpson_result.text = str(resultado)

        rectangulos()
        rectangulosInf()
        trapecios()
        simpson()
        

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
        for plot in self.graph.plots:
            self.graph.remove_plot(plot)
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
            while i < 6:
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
    def Create_Graph(self):
        pParsed = int(self.p.text)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        N=50
        stride=2
        u = np.linspace(0, 2 * np.pi, N)
        v = np.linspace(0, np.pi, N)

        """
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))   
        """

        x = np.outer(((1 - u**(pParsed) - u**(pParsed))**(1/pParsed)), ((1 - v**(pParsed) - v**(pParsed))**(1/pParsed)))
        y = np.outer(((1 - u**(pParsed) - u**(pParsed))**(1/pParsed)), ((1 - v**(pParsed) - v**(pParsed))**(1/pParsed)))
        z = np.outer(np.ones(np.size(u)), ((1 - v**(pParsed) - v**(pParsed))**(1/pParsed)))
        
        
        ax.plot_surface(x, y, z, linewidth=0.0, cstride=stride, rstride=stride)

        """
        x = y = np.arange(-2.0, 2.0, 0.1)
        X, Y = np.meshgrid(x, y)
        zs = np.array([(1-(x)**pParsed - (y)**pParsed)**(1/pParsed) for x,y in zip(np.ravel(X), np.ravel(Y))])
        Z = zs.reshape(X.shape)
        ax.plot_surface(X, Y, Z)
        ax.set_xlabel('Eje X')
        ax.set_ylabel('Eje Y')
        ax.set_zlabel('Eje Z')
        """

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

class I_N_ventana(Screen, Widget):
    pass

class I_N_Rectangulos(Screen, Widget):
    def metodorectangulos(self):
        nParsed = int(self.n.text)
        aParsed = int(self.a.text)
        bParsed = int(self.b.text)

        a = aParsed
        dx = (bParsed-aParsed)/nParsed
        vectorx = []
        vectordatos = []
        i = 0

        while a <= bParsed :
            if i == 0:
                vectorx.append(a)
                i = i+1
            else:
                vectorx.append(a+dx) 
                i = i+1
                a = a+dx    

        print (vectorx)
        for num in range(0,len(vectorx)):
            aux = vectorx[num]
            aux2 = f(aux)
            vectordatos.append(aux2)

        print(vectordatos)
        aux4 = 0
        for num in range(0,len(vectordatos)):
            aux3 = vectordatos[num]
            aux4 = aux4 + aux3
            resultado = aux4
        
        resultado = resultado * dx
        print (resultado)
        self.output_t.text = str(resultado)
"""
def f(x):
    resultado = (x**2)+x+6
    return resultado
"""   

class I_N_Simpson(Screen, Widget):
    def metodosimpson(self):
        nParsed = int(self.n.text)
        aParsed = int(self.a.text)
        bParsed = int(self.b.text)

        a = aParsed
        dx = (bParsed-aParsed)/nParsed
        vectorpar = []
        vectorpar2 = []
        vectorimpar = []
        vectorimpar2 = []
        primero:int
        ultimo:int
        primero = 0
        ultimo = 0
        i = 0

        while a <= bParsed :
            if i%2 == 0:
                if i == 0:
                    primero = a
                    i=i+1
                    a=a+dx
                else:
                    vectorpar.append(a)
                    i = i+1
                    a = a+dx
                    
            else: 
                vectorimpar.append(a) 
                i = i+1
                a = a+dx    
        if a > bParsed :
            ultimo = a
        print (vectorpar)
        print(primero)
        print (ultimo)
        print(vectorimpar)
        primero = f(primero)
        ultimo = f(ultimo)
        for num in range(0,len(vectorpar)):
            aux = vectorpar[num]
            aux2 = g(aux)
            vectorpar2.append(aux2)
        for num in range(0,len(vectorimpar)):
            aux = vectorimpar[num]
            aux2 = g(aux)
            vectorimpar2.append(aux2)

        print(vectorimpar2)
        print(vectorpar2)
        print(primero)
        print(ultimo)

        aux4 = 0
        aux5 = 0
        aux6 = 0
        for num in range(0,len(vectorpar2)):
            aux3 = vectorpar2[num]
            aux4 = aux4 + aux3
            pares = aux4
        for num in range(0,len(vectorimpar2)):
            aux5 = vectorimpar2[num]
            aux6 = aux6 + aux5
            impares = aux6

        resultado = (4*impares+2*pares+primero + ultimo) * dx/3
        print (resultado)
        self.output_t.text = str(resultado)

def g(x):
    resultado = (x**2)+x+6
    return resultado


screen_manager = ScreenManager()

screen_manager.add_widget(MAOptionWindow(name ="ma_option_window")) 
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
screen_manager.add_widget(I_N_Rectangulos(name="INRectangulos"))
screen_manager.add_widget(I_N_ventana(name="INventanas"))
screen_manager.add_widget(I_N_Simpson(name="INSimpson"))

class CalculoNumericoApp(App):
    def build(self):
        self.title = 'Calculo Numerico Proyecto 1, 2019'
        return screen_manager


sample_app = CalculoNumericoApp()
sample_app.run()
