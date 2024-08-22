import tkinter as tk
def Fahrenheit_Celsius():
    Fahrenheit = float(EntradaFahrenheit.get())
    Celsius = (Fahrenheit-32)*5/9
    EntradaCelsius.delete(0,tk.END)
    EntradaCelsius.insert(0, f"{Celsius: .2f}")

ventana = tk.Tk()
ventana.title("Actividad 03 - Conversor de temperatura en python")

#titulo_texto = tk.Label(ventana, texto="CONVERSOR FAHRENHEIT/CELCIUS", anchor=CENTER, fg="purpurle", bg="#8623e8")
#titulo_texto.config(font=("comic sans",15))
#titulo_texto.grid(row=0, column=0, columnspaw=4, pady=5)

TextoFahrenheit = tk.Label(ventana, text="Fatenheit: ")
TextoFahrenheit.grid(row=0, column=0)

EntradaFahrenheit = tk.Entry(ventana)
EntradaFahrenheit.grid(row=0, column=1)

BotonFahrenheit = tk.Button(ventana, text= "Fº a Cº", command=Fahrenheit_Celsius)
BotonFahrenheit.grid(row=0, column=2)

def Celsius_Fahrenheit():
    Celsius = float(EntradaCelsius.get())
    Fahrenheit = (Celsius*9/5)+32
    EntradaFahrenheit.delete(0,tk.END)
    EntradaFahrenheit.insert(0, f"{Fahrenheit:.2f}")

TextoCelsius = tk.Label(ventana, text="Celsius: ")
TextoCelsius.grid(row=1, column=0)

EntradaCelsius = tk.Entry(ventana)
EntradaCelsius.grid(row=1, column=1)

BotonCelsius = tk.Button(ventana, text= "C a F", command=Celsius_Fahrenheit)
BotonCelsius.grid(row=1, column=2)

ventana.mainloop()