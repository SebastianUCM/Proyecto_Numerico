
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
Builder.load_string(""" 
<MainWindow>: 
    name: 'Accordion'

    fullscreen: True

    canvas.before:
        Color:
            rgb: .2, .2, .5
        Rectangle:
            size: self.size
            source: 'data/background.png'
    
    BoxLayout:
        orientation: 'vertical'

        Label:
            text: 'Espacios Normados'
            font_size: '72dp'

    BoxLayout:
        size_hint_y: None
        height: '60dp'
        
        Button:
            text: 'Espacio Euclidiano R^n'
            group: 'accordion'
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.transition.duration = 1 
                root.manager.current = 'eu_option_window'

        Button:
            text: 'Espacio de funciones Continuas en [a,b]'
            group: 'accordion'
            on_press: 
                root.manager.transition.direction = 'left' 
                root.manager.transition.duration = 1 
                root.manager.current = 'ef_option_window'
   
<EUOptionWindow>: 
    name: 'EU Option Window'
    fullscreen: True

    canvas.before:
        Color:
            rgb: .5, .2, .2
        Rectangle:
            size: self.size
            source: 'data/background.png'
    
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Espacio Euclidiano R^n'
                font_size: '48dp'

            BoxLayout:
                orientation: 'horizontal'
                padding: 10
                #size_hint_y: None


                #Left side buttons
                BoxLayout:
                    orientation: 'vertical'
                    padding: 5

                    Button:
                        text: 'Tipos de Normas en R^n'
                        on_press: 
                            root.manager.transition.direction = 'right' 
                            root.manager.transition.duration = 1 
                            root.manager.current = 'eu_norm_type'
                        #background_color: .5,.1,.1,6
                    Button:
                        text: 'Producto Vectorial en R^3'
                    Button:
                        text: 'Grafico Norma P en R^2'

                #right side buttons
                BoxLayout:
                    orientation: 'vertical'
                    padding: 5

                    Button:
                        text: 'Producto Interno en R^n'
                    Button:
                        text: 'Producto Mixto en R^3'
                    Button:
                        text: 'Grafico Norma P en R^3'

        BoxLayout:
            size_hint_y: None
            height: '48dp'
            
            Button:
                text: 'Volver al Menu Principal'
                group: 'accordion'
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'main_window'
  
<EFOptionWindow>: 
    name: 'EF Option Window'
    fullscreen: True

    canvas.before:
        Color:
            rgb: .2, .5, .2
        Rectangle:
            size: self.size
            source: 'data/background.png'
    
    BoxLayout:
        orientation: 'vertical'

        BoxLayout:
            orientation: 'vertical'

            Label:
                text: 'Espacio de Funciones Continuas en [a, b]'
                font_size: '32dp'

        BoxLayout:
            orientation: 'horizontal'
            padding: 10

            height: '60dp'

            Button:
                text: 'Producto Interno en espacio de funciones continuas'
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'main_window'
                #background_color: .5,.1,.1,6
            Button:
                text: 'Norma en espacio de funciones continuas'
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'main_window'

        BoxLayout:
            size_hint_y: None
            height: '48dp'
            
            Button:
                text: 'Volver al Menu Principal'
                group: 'accordion'
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'main_window'

<EUNormType>: 
    name: 'Accordion'
    fullscreen: True
    n: n
    p: p
    output_x1: _id_lbl_x1

    canvas.before:
        Color:
            rgb: .9, .2, .5
        Rectangle:
            size: self.size
            source: 'data/background.png'
    
    BoxLayout:
        orientation: 'vertical'
        AnchorLayout:
            anchor_y: 'bottom'
            anchor_x: 'center'

            Label:
                text: 'Tipos de Normas en R^n'
                font_size: '48dp'
            
            Label:
                id: _id_lbl_x1
                text: "AQUI"
                height: 40
                size_hint_y: None
                text_size: self.width, None
                height: self.texture_size[1]

        BoxLayout:
            orientation: 'horizontal'
            padding: 10

            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                padding: 10
                Label:
                    text: 'N: '
                    font_size: 60
                TextInput:
                    id: n
                    font_size: 60
                    height: 60

            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                padding: 10
                Label:
                    text: 'P: '
                    font_size: 60
                TextInput:
                    id: p
                    font_size: 60
                    height: 60

            BoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                Button:
                    text: 'Calcular'
                    on_press: root.inputN()

        BoxLayout:
            size_hint_y: None
            height: '60dp'
            
            Button:
                text: 'Espacio Euclidiano R^n'
                group: 'accordion'
                on_press: 
                    root.manager.transition.direction = 'right' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'eu_option_window'

            Button:
                text: 'Espacio de funciones Continuas en [a,b]'
                group: 'accordion'
                on_press: 
                    root.manager.transition.direction = 'left' 
                    root.manager.transition.duration = 1 
                    root.manager.current = 'ef_option_window'
  
<ScreenFive>: 
    BoxLayout: 
        Button: 
            text: "Go to Screen 1" 
            background_color : 1, 0, 0, 1 
            on_press: 
                root.manager.transition.direction = 'right' 
                root.manager.current = 'main_window' 
  
  
""") 
   
# Create a class for all screens in which you can include 
# helpful methods specific to that screen 
class MainWindow(Screen): 
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
   
   
# The ScreenManager controls moving between screens 
screen_manager = ScreenManager() 
   
# Add the screens to the manager ancontent_width supply a name 
# that is used to switch screens 
screen_manager.add_widget(MainWindow(name ="main_window")) 
screen_manager.add_widget(EUOptionWindow(name ="eu_option_window"))
screen_manager.add_widget(EUNormType(name ="eu_norm_type")) 
screen_manager.add_widget(EFOptionWindow(name ="ef_option_window")) 
screen_manager.add_widget(ScreenFive(name ="screen_five")) 
  
# Create the App class 
class CalculoNumericoApp(App): 
    def build(self):
        self.title = 'Calculo Numerico Proyecto 1, 2019' 
        return screen_manager 
  
# run the app  
sample_app = CalculoNumericoApp() 
sample_app.run() 
