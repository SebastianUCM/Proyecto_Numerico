
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
        #Random array
        arr = np.random.randint(low=0, high=nParsed, size=nParsed)
        print(arr)
        x1 = sum(arr)
        #label_one = str(x1)
        #print(output_one)
        #print(x1)
        x2 = sum(arr**2)
        #print(x2)
        x2 = np.sqrt(x2)
        #print(x2)
        x3 = np.amax(arr)
        #print(x3)
        x4 = sum(arr**pParsed)
        x4 = x4**(1.0/pParsed)
        #print(x4)
        #change texts! 
        mat.plot(arr)
        mat.show()   
        self.output_x1.text = str(x1)  



class ScreenFive(Screen): 
    pass
   
class Producto_Vectorial (Screen):
	pass

class Grafico_N_R2 (Screen):
	pass

class Producto_Interno (Screen):
	pass

class Producto_Mixto (Screen):
	pass

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
