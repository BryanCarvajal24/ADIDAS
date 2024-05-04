import pandas as pd
import matplotlib.pyplot as ply
import seaborn as sns  




#dataset = pd.read_csv('G:/Mi unidad/UAO/INGENIERÍA DE DATOS E I.A/SEMESTRE 2/PROGRAMACIÓN/dset.csv', header = None)
dataset= pd.read_excel('G:/Mi unidad/UAO/INGENIERÍA DE DATOS E I.A/SEMESTRE 2/PROGRAMACIÓN/datasetadidas.xlsx')  

print(dataset)  # muestra el dataset y columnas y filas

print(dataset.shape)  # muestra columnas y filas

dataset.head()  #muestra los 5 primeros registros


dataset.info() #cuales son variable categoricas y las numericas
                # int= numericas  #object= categoricas
                
                


# 2 LIMPIEZA

'''
datos faltantes
datos irrelevantes
registros repretidos: filas con la misma informacion
valores extremos aveces: columnas con datos no reales, pueden haberse digitado mal
errores de estructuras en variables categoricas
'''


#datos incompletos: eliminar los datos faltantes

dataset.dropna(inplace=True) # elimina la fila completa con los datos faltantes y el inplace lo reescribe
dataset.info() # verificar la misma cantidad de filas


#columnas irrelevantes: eliminarlas 

del dataset['Retailer ID']
dataset.info()


#cambiar nombre de columnas

dataset=dataset.rename(columns= {'Retailer':'Minorista', 'Invoice Date':'Fecha de facturación', 'Region':'Región', 'State': 'Estado', 'City':'Cuidad', 'Product':'Producto', 'Price per Unit':'Precio por Unidad', 'Units Sold':'Unidades Vendidas', 'Total Sales':'Ventas Totales', 'Operating Profit':'Beneficio operativo', 'Operating Margin':'Margen operativo', 'Sales Method':'Método de venta'})
print(dataset)




#3. Interfaz Grafica de Usuario

import tkinter
from tkinter import*
from PIL import ImageTk, Image



window= tkinter.Tk()

window.title('Adidas US Sales Dataset')

window.geometry('1600x850')



# imagen de adidas

imagen= ImageTk.PhotoImage(Image.open('C:/Users/braya/OneDrive/Imágenes/adidas.jpg').resize((1600,850)))
labelimg= tkinter.Label(image=imagen)
labelimg.pack()




#interfaz


button1= Button(window, text='Salir', command=window.quit, activebackground='Darkblue', bg='Snow')
#button1.pack(side=('bottom'))
button1.place(x=720, y=620, height=30, width=100)


button2= Button(window, text='Iniciar', height=30, width=15, activebackground='Darkblue', bg='Snow' )
#button2.pack(side=('bottom'))
button2.place(x=720, y=545, height=30, width=100)
















window.mainloop()



























