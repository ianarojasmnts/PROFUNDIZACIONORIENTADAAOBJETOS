import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from openpyxl import Workbook

# =========================
# CONEXION MYSQL
# =========================

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="banco"
)

cursor = conexion.cursor()

# =========================
# CLIENTES
# =========================

def guardar_cliente():
    try:

        cursor.callproc("sp_InsertCliente",(
            tipo.get(),
            nombre.get(),
            documento.get(),
            telefono.get(),
            correo.get()
        ))

        conexion.commit()

        messagebox.showinfo("Correcto","Cliente guardado")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# =========================
# CUENTAS
# =========================

def guardar_cuenta():
    try:

        cursor.callproc("sp_InsertCuenta",(
            codigo.get(),
            tipo_cuenta.get(),
            moneda.get(),
            sucursal.get(),
            saldo.get(),
            estado.get()
        ))

        conexion.commit()

        messagebox.showinfo("Correcto","Cuenta creada")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# =========================
# CREDITOS
# =========================

def guardar_credito():
    try:

        cursor.callproc("sp_InsertCredito",(
            codigo.get(),
            monto.get(),
            plazo.get(),
            interes.get(),
            estado_credito.get()
        ))

        conexion.commit()

        messagebox.showinfo("Correcto","Crédito registrado")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# =========================
# TRANSACCIONES
# =========================

def guardar_transaccion():
    try:

        cursor.callproc("sp_InsertTransaccion",(
            origen.get(),
            destino.get(),
            tipo_t.get(),
            monto_t.get(),
            canal.get()
        ))

        conexion.commit()

        messagebox.showinfo("Correcto","Transacción guardada")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# =========================
# EXPORTAR CLIENTES
# =========================

def exportar_clientes_excel():

    try:

        cursor.execute("SELECT * FROM clientes")
        datos = cursor.fetchall()

        if len(datos) == 0:
            messagebox.showwarning("Aviso","No hay clientes para exportar")
            return

        libro = Workbook()
        hoja = libro.active
        hoja.title = "Clientes"

        hoja.append([
            "Codigo",
            "Tipo Cliente",
            "Nombre",
            "Documento",
            "Telefono",
            "Correo"
        ])

        for fila in datos:
            hoja.append(fila)

        libro.save("clientes.xlsx")

        messagebox.showinfo("Excel","Clientes exportados correctamente")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# =========================
# EXPORTAR TRANSACCIONES
# =========================

def exportar_transacciones():

    try:

        cursor.execute("SELECT * FROM transacciones")
        datos = cursor.fetchall()

        if len(datos) == 0:
            messagebox.showwarning("Aviso","No hay transacciones para exportar")
            return

        libro = Workbook()
        hoja = libro.active
        hoja.title = "Transacciones"

        hoja.append([
            "Codigo",
            "Cuenta Origen",
            "Cuenta Destino",
            "Tipo",
            "Monto",
            "Canal",
            "Fecha"
        ])

        for fila in datos:
            hoja.append(fila)

        libro.save("transacciones.xlsx")

        messagebox.showinfo("Excel","Transacciones exportadas")

    except Exception as e:
        messagebox.showerror("Error",str(e))


# =========================
# VENTANA PRINCIPAL
# =========================

root = tk.Tk()
root.geometry("900x500")
root.title("BankSys - Sistema Financiero")

notebook = ttk.Notebook(root)

tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

notebook.add(tab1, text="Clientes")
notebook.add(tab2, text="Cuentas")
notebook.add(tab3, text="Créditos")
notebook.add(tab4, text="Transacciones")

notebook.pack(expand=True, fill="both")

# =========================
# CLIENTES
# =========================

titulo = tk.Label(tab1,text="FORMULARIO CLIENTES",
font=("Arial",16,"bold"),fg="blue")
titulo.pack(pady=20)

form1 = tk.Frame(tab1)
form1.pack()

tk.Label(form1,text="Codigo Cliente").grid(row=0,column=0)
codigo = tk.Entry(form1)
codigo.grid(row=0,column=1)

tk.Label(form1,text="Tipo Cliente").grid(row=1,column=0)
tipo = tk.Entry(form1)
tipo.grid(row=1,column=1)

tk.Label(form1,text="Nombre").grid(row=2,column=0)
nombre = tk.Entry(form1)
nombre.grid(row=2,column=1)

tk.Label(form1,text="Documento").grid(row=3,column=0)
documento = tk.Entry(form1)
documento.grid(row=3,column=1)

tk.Label(form1,text="Telefono").grid(row=4,column=0)
telefono = tk.Entry(form1)
telefono.grid(row=4,column=1)

tk.Label(form1,text="Correo").grid(row=5,column=0)
correo = tk.Entry(form1)
correo.grid(row=5,column=1)

tk.Button(tab1,text="Guardar Cliente",
bg="green",fg="white",
command=guardar_cliente).pack(pady=10)

tk.Button(tab1,text="Exportar Clientes Excel",
bg="purple",fg="white",
command=exportar_clientes_excel).pack(pady=5)

# =========================
# CUENTAS
# =========================

titulo2 = tk.Label(tab2,text="CUENTAS BANCARIAS",
font=("Arial",16,"bold"),fg="green")
titulo2.pack(pady=20)

form2 = tk.Frame(tab2)
form2.pack()

tk.Label(form2,text="Tipo Cuenta").grid(row=0,column=0)
tipo_cuenta = tk.Entry(form2)
tipo_cuenta.grid(row=0,column=1)

tk.Label(form2,text="Moneda").grid(row=1,column=0)
moneda = tk.Entry(form2)
moneda.grid(row=1,column=1)

tk.Label(form2,text="Sucursal").grid(row=2,column=0)
sucursal = tk.Entry(form2)
sucursal.grid(row=2,column=1)

tk.Label(form2,text="Saldo").grid(row=3,column=0)
saldo = tk.Entry(form2)
saldo.grid(row=3,column=1)

tk.Label(form2,text="Estado").grid(row=4,column=0)
estado = tk.Entry(form2)
estado.grid(row=4,column=1)

tk.Button(tab2,text="Guardar Cuenta",
bg="green",fg="white",
command=guardar_cuenta).pack(pady=20)

# =========================
# CREDITOS
# =========================

titulo3 = tk.Label(tab3,text="CREDITOS",
font=("Arial",16,"bold"),fg="red")
titulo3.pack(pady=20)

form3 = tk.Frame(tab3)
form3.pack()

tk.Label(form3,text="Monto").grid(row=0,column=0)
monto = tk.Entry(form3)
monto.grid(row=0,column=1)

tk.Label(form3,text="Plazo").grid(row=1,column=0)
plazo = tk.Entry(form3)
plazo.grid(row=1,column=1)

tk.Label(form3,text="Interes").grid(row=2,column=0)
interes = tk.Entry(form3)
interes.grid(row=2,column=1)

tk.Label(form3,text="Estado").grid(row=3,column=0)
estado_credito = tk.Entry(form3)
estado_credito.grid(row=3,column=1)

tk.Button(tab3,text="Registrar Credito",
bg="green",fg="white",
command=guardar_credito).pack(pady=20)

# =========================
# TRANSACCIONES
# =========================

titulo4 = tk.Label(tab4,text="TRANSACCIONES",
font=("Arial",16,"bold"),fg="purple")
titulo4.pack(pady=20)

form4 = tk.Frame(tab4)
form4.pack()

tk.Label(form4,text="Cuenta Origen").grid(row=0,column=0)
origen = tk.Entry(form4)
origen.grid(row=0,column=1)

tk.Label(form4,text="Cuenta Destino").grid(row=1,column=0)
destino = tk.Entry(form4)
destino.grid(row=1,column=1)

tk.Label(form4,text="Tipo").grid(row=2,column=0)
tipo_t = tk.Entry(form4)
tipo_t.grid(row=2,column=1)

tk.Label(form4,text="Monto").grid(row=3,column=0)
monto_t = tk.Entry(form4)
monto_t.grid(row=3,column=1)

tk.Label(form4,text="Canal").grid(row=4,column=0)
canal = tk.Entry(form4)
canal.grid(row=4,column=1)

tk.Button(tab4,text="Registrar Transaccion",
bg="green",fg="white",
command=guardar_transaccion).pack(pady=10)

tk.Button(tab4,text="Exportar Transacciones Excel",
bg="purple",fg="white",
command=exportar_transacciones).pack(pady=10)

root.mainloop()