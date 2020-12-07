'''
UNIVERSIDAD DE GUADALAJARA 
MAESTRIA EN CIENCIA DE LOS DATOS 
PROGRAMACIÓN I 
PROYECTO FINAL 

CAROL DESIREÉ RAMIREZ DURÁN
MÓNICA ALONSO SORIA 
MANUEL CHRISTIAN ALBERTO DIAZ 

########################################
##      CONVERTIDOR DE DIVISAS        ##
#########################################
'''
# Instalar en terminal tkinter y requests
# pip install tkinter 
# pip install requests


# Importamos todas las funciones de tkinter 
from tkinter import *

TK_SILENCE_DEPRECATION=1 
  
# Creaamos la ventana del GUI 
root = Tk() 
  
# Creamos las variables globales  
variable1 = StringVar(root) 
variable2 = StringVar(root) 
  
# Inicializamos las variables  
variable1.set("divisa") 
variable2.set("divisa") 
  
      
# Función para traer la conversión de tipo de cambio de una divisa a otra  
def RealTimeCurrencyConversion(): 
  
    # importar bibliotecas necesarias 
    import requests, json  # Asegurarse de instalar pip install request 
    
    # codigo de la divisa 
    from_currency = variable1.get() 
    to_currency = variable2.get()
  
    # url base 
    base_url = r"https://api.ratesapi.io/api/latest?"
  
    # url completa, para convertir de una moneda base a otra divisa
    main_url = base_url + "base=" + from_currency + "&symbols=" + to_currency 

    # obtener la info de la API 
    response = requests.get(main_url)
  
    # convertir a json para acceder a los diccionarios 
    result = response.json()

    # parsing 
    Exchange_Rate = float(result["rates"][to_currency])
  
    # Obtener el monto 
    amount = float(Amount1_field.get()) 
  
    # calcular la conversion 
    new_amount = round(amount * Exchange_Rate, 3) 
  
    # Insertar método  
    Amount2_field.insert(0, str(new_amount)) 

  
# Limpiar el campo 
def clear_all() : 
    Amount1_field.delete(0, END)  
    Amount2_field.delete(0, END) 
     

# Customización del programa  
if __name__ == "__main__" : 
  
    # Establecer el color de fondo  
    root.configure(background = 'light blue')  
    
    # Configuaración de la ventana 
    root.geometry("400x175")  
    
    # Crear etiqueta de bienvenia 
    headlabel = Label(root, text = 'Convertidor de Divisas ', fg = 'white', bg = "blue")  
  
    # Crear etiqueta de monto 
    label1 = Label(root, text = "Monto :", 
                 fg = 'white', bg = 'blue') 
      
    # Crear etiqueta de divisa base 
    label2 = Label(root, text = "Convertir de",  
                   fg = 'white', bg = 'blue')  
    
    # Crear etiqueta de divisa a convertir  
    label3 = Label(root, text = "Convertir a :",  
                   fg = 'white', bg = 'blue') 
  
    # Crear etiqueta de monto convertido   
    label4 = Label(root, text = "Monto convertido :",  
                   fg = 'white', bg = 'blue') 
  
    # Posiciones    
    headlabel.grid(row = 0, column = 1)  
    label1.grid(row = 1, column = 0)  
    label2.grid(row = 2, column = 0) 
    label3.grid(row = 3, column = 0) 
    label4.grid(row = 5, column = 0) 
      
    # Crear campo de texto   
    Amount1_field = Entry(root)  
    Amount2_field = Entry(root) 
       
    # Ancho del campo 
    Amount1_field.grid(row = 1, column = 1, ipadx ="25")  
    Amount2_field.grid(row = 5, column = 1, ipadx ="25") 
  
    # Lista de las divisas disponibles 
    CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","MXN"] 
  
    # Crear el menú 
    FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list) 
    ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list) 
      
    FromCurrency_option.grid(row = 2, column = 1, ipadx = 10) 
    ToCurrency_option.grid(row = 3, column = 1, ipadx = 10) 
      
    # Crear botón para convertir y ejecute la función 
    button1 = Button(root, text = "Convertir", bg = "red", fg = "black", 
                                command = RealTimeCurrencyConversion) 
      
    button1.grid(row = 4, column = 1) 
  
    # Crear un botón para limpiar con una función para eliminar 
    button2 = Button(root, text = "Clear", bg = "red",  
                     fg = "black", command = clear_all) 
    button2.grid(row = 6, column = 1) 


    # Ejecutar el GUI   
    root.mainloop() 
