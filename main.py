
# Program to Show how to create a switch  
# import kivy module     
import kivy   
import random
import numpy as np  
import matplotlib.pyplot as mat

# base Class of your App inherits from the App class.     
# app:always refers to the instance of your application

from kivy.app import App  
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

# this restrict the kivy version i.e   
# below this kivy version you cannot   
# use the app or software   
kivy.require('1.9.0') 
  
# Builder is used when .kv file is 
# to be used in .py file 
from kivy.lang import Builder 
  
# The screen manager is a widget 
# dedicated to managing multiple screens for your application. 
from kivy.uix.screenmanager import ScreenManager, Screen 
   
# You can create your kv code in the Python file 
Builder.load_file('main.kv')
   
# Create a class for all screens in which you can include 
# helpful methods specific to that screen

class Ventana_Menu(Screen): 
    pass
   
class EUOptionWindow(Screen): 
    pass
  
class EFOptionWindow(Screen): 
    pass
  
class EUNormType(Screen, Widget):
    def inputN(self):
        #Taking values front the input to the codeb
        nParsed = int(self.n.text)
        pParsed = int(self.p.text)
        menor_valor = -500
        mayor_valor = 500
        #Random array
        arr = np.zeros(nParsed)
        for i in range(nParsed):
            valor_aleatorio = random.randint(menor_valor,mayor_valor)
            arr[i] = valor_aleatorio
        print(arr)

        # TIPOS DE NORMA
        # |X|1
        # Norma de la Suma
        x1 = np.linalg.norm(arr,1)
        # |X|2
        # Norma Euclidiana 
        x2 = np.linalg.norm(arr,2)
        # |X|inf
        # Norma del Maximo
        x3 = np.linalg.norm(arr,np.inf)
        # |X|p
        # Norma P
        xp = np.linalg.norm(arr,pParsed)
        
        self.output_vector.text = str(arr) 
        self.output_x1.text = str(x1)  
        self.output_x2.text = str(x2)
        self.output_x3.text = str(x3)
        self.output_xp.text = str(xp)  

class ScreenFive(Screen): 
    pass
   
class Producto_Vectorial (Screen, Widget):
    def inputN(self):
        #Taking values front the input to the codeb
        x1Parsed = int(self.x1.text)
        x2Parsed = int(self.x2.text)
        x3Parsed = int(self.x3.text)
        y1Parsed = int(self.y1.text)
        y2Parsed = int(self.y2.text)
        y3Parsed = int(self.y3.text)
        vector_1=[x1Parsed,x2Parsed,x3Parsed]
        vector_2=[y1Parsed,y2Parsed,y3Parsed]
        print(vector_1)
        sub_mat_i=([x2Parsed,x3Parsed],[y2Parsed,y3Parsed])
        sub_mat_j=([x1Parsed,x3Parsed],[y1Parsed,y3Parsed])
        sub_mat_k=([x1Parsed,x2Parsed],[y1Parsed,y2Parsed])
        i=(np.linalg.det(sub_mat_i))*1
        j=(np.linalg.det(sub_mat_j))*-1
        k=(np.linalg.det(sub_mat_k))*1

        self.output_i.text = str(i)
        self.output_j.text = str(j)
        self.output_k.text = str(k)  


class Grafico_N_R2 (Screen):
        #mat.plot(arr)
        #mat.show()
	pass

class Producto_Interno (Screen, Widget):
        pass
    #def inputN(self):
        #cantidad_vectores=3
        #vector= np.zeros(n)
        #arreglo_vectores = np.zeros((cantidad_vectores,n))
        #pivote=1
        #resultado=0
        #for i in range(cantidad_vectores):
        #    for j in range(n):
	#	valor_aleatorio = random.randint(menor_valor,mayor_valor)
	#	arreglo_vectores[i][j]=valor_aleatorio
        #print(arreglo_vectores)

        #for j in range(n):
        #    for i in range(cantidad_vectores):
	#	pivote=arreglo_vectores[i][j]*pivote
         #   resultado=pivote+resultado
         #   print("Multiplicacion")	
        #    print(pivote)
        #    print("Suma")
        #    print(resultado)
        #    pivote=1
        #print(resultado)
        
        #nParsed = int(self.n.text)

class Producto_Mixto (Screen, Widget):
        pass
    #def inputN(self):
        #Taking values front the input to the codeb
        #x1=9
        #x2=8
        #x3=7
        #y1=3
        #y2=4
        #y3=5
        #z1=1
        #z2=2
        #z3=3
        #i=0
        #j=0
        #k=0

        #vector_1=[x1,x2,x3]
        #vector_2=[y1,y2,y3]
        #vector_3=[z1,z2,z3]

        #sub_mat_i=([y2,y3],[z2,z3])
        #sub_mat_j=([y1,y3],[z1,z3])
        #sub_mat_k=([y1,y2],[z1,z2])

        #i=(np.linalg.det(sub_mat_i))
        #j=(np.linalg.det(sub_mat_j))
        #k=(np.linalg.det(sub_mat_k))

        #resultado=((x1*i)-(x2*j)+(x3+k))

        #print(resultado)

class Grafico_N_R3 (Screen):
	pass

class Producto_Interno_Funciones_Continuas(Screen):
        pass

class Norma_Espacio_Funciones_Continuas(Screen):
        pass

# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager ancontent_width supply a name 
# that is used to switch screens 
screen_manager.add_widget(Ventana_Menu(name ="main_window")) 
screen_manager.add_widget(EUOptionWindow(name ="eu_option_window"))
screen_manager.add_widget(EUNormType(name ="eu_norm_type")) 
screen_manager.add_widget(EFOptionWindow(name ="ef_option_window")) 
screen_manager.add_widget(ScreenFive(name ="screen_five"))
screen_manager.add_widget(Producto_Vectorial(name ="vectorial"))
screen_manager.add_widget(Grafico_N_R2(name ="grafico_r2"))
screen_manager.add_widget(Producto_Interno(name ="interno"))
screen_manager.add_widget(Producto_Mixto(name ="mixto"))
screen_manager.add_widget(Grafico_N_R3(name ="grafico_r3"))
screen_manager.add_widget(Producto_Interno_Funciones_Continuas(name ="interno_funciones"))
screen_manager.add_widget(Norma_Espacio_Funciones_Continuas(name ="norma_funciones"))




# Create the App class 
class CalculoNumericoApp(App): 
    def build(self):
        self.title = 'Calculo Numerico Proyecto 1, 2019' 
        return screen_manager 
  
# run the app  
sample_app = CalculoNumericoApp() 
sample_app.run() 
