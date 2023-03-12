import tkinter as tk
import customtkinter as ctk
import sqlite3 as sql
from tkinter import messagebox as mb

# Conexión a la base y armado de tabla.
conn = sql.connect('Base1.db')
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS Base_1 (
    username TEXT NOT NULL PRIMARY KEY,
    password TEXT NOT NULL,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL
)""")
cursor.close()
conn.close()

# Ventana principal.
window = tk.Tk()
window.title('Log in')
window.iconbitmap(r'C:\Users\Lucas\OneDrive\Imágenes\login-image.ico') # Dirección en mis archivos
window.resizable(False, False)
window.geometry('300x375+525+150')
color1 = '#B8FFB9'
window.config(bg=color1)

ctk.CTkLabel(
    window, 
    text='Login', 
    fg_color=color1,
    text_color='#000000',
    font=("Calibri Black", 22)
).pack(side='top', pady=5)

ctk.CTkLabel(
    window, 
    text='Username:', 
    fg_color=color1,
    text_color='#000000', 
    font=("Calibri Black",18)
).pack()

username_entry = ctk.CTkEntry(
    window, 
    font=("Calibri",14),
    fg_color='#FFFFFF',
    text_color='#000000',
    border_color='#000000'
)
username_entry.pack(pady=5)

ctk.CTkLabel(
    window,
    text='Password:',
    fg_color=color1,
    text_color='#000000',
    font=("Calibri Black",18)
).pack()

password_entry = ctk.CTkEntry(
    window,
    show='*',
    font=("Calibri",14),
    fg_color='#FFFFFF',
    text_color='#000000',
    border_color='#000000'
)
password_entry.pack(pady=5)

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if username == '' or password == '' :
        mb.showerror('Error', 'Missing data, make sure you fill in all the fields')
    else :
        conn = sql.connect('Base1.db')
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Base_1 WHERE username="{username}" AND password="{password}"')
        if cursor.fetchall():
            mb.showinfo('Login', 'Login successful! Correct username and password.')
        else:
            mb.showerror('Error', 'Wrong username or password, please try again.')
        
        cursor.close()
        conn.close()

# Ventana de registro
def registerWindow():
    register_window = tk.Toplevel(window)
    register_window.title('Register_stage')
    register_window.iconbitmap(r'C:\Users\Lucas\OneDrive\Imágenes\login-image.ico') # Dirección en mis archivos
    register_window.geometry('280x500+525+125')
    color2 = '#C9FFFD'
    register_window.config(bg=color2)
    
    ctk.CTkLabel(
        register_window, 
        text='Register',
        text_color='#000000',
        fg_color=color2, 
        font=("Arial", 22)
    ).pack(side='top', pady=5)
    
    ctk.CTkLabel(
        register_window, 
        text='Name(s):',
        text_color='#000000', 
        fg_color=color2, 
        font=("Arial",18)
    ).pack(pady=5)

    name_entry = ctk.CTkEntry(
        register_window, 
        font=("Arial",14),
        fg_color='#FFFFFF',
        border_color='#000000',
        text_color='#000000'
    )
    name_entry.pack(pady=5)

    ctk.CTkLabel(
        register_window, 
        text='Last name(s):',
        text_color='#000000', 
        fg_color=color2, 
        font=("Arial",18)
    ).pack(pady=5)

    surname_entry = ctk.CTkEntry(
        register_window, 
        font=("Arial",14),
        fg_color='#FFFFFF',
        border_color='#000000'
    )
    surname_entry.pack(pady=5)
    
    ctk.CTkLabel(
        register_window, 
        text='Username:',
        text_color='#000000', 
        fg_color=color2, 
        font=("Arial",18)
    ).pack(pady=5)

    regstr_user = ctk.CTkEntry(
        register_window, 
        font=("Arial",14),
        fg_color='#FFFFFF',
        border_color='#000000'
    )
    regstr_user.pack(pady=5)
    
    ctk.CTkLabel(
        register_window, 
        text='Password:',
        text_color='#000000', 
        fg_color=color2, 
        font=("Arial",18)
    ).pack(pady=5)

    regstr_pass = ctk.CTkEntry(
        register_window, 
        show='*', 
        font=("Arial",14),
        fg_color='#FFFFFF',
        border_color='#000000'
    )
    regstr_pass.pack(pady=5)
    
    ctk.CTkLabel(
        register_window, 
        text='Repeat password:',
        text_color='#000000', 
        fg_color=color2, 
        font=("Arial",18)
    ).pack(pady=5)

    regstr_pass2 = ctk.CTkEntry(
        register_window, 
        show='*', 
        font=("Arial",14),
        fg_color='#FFFFFF',
        border_color='#000000'
    )
    regstr_pass2.pack(pady=5)

    # Función de registro.
    def register():
        name = name_entry.get()
        last_name = surname_entry.get()
        user_reg = regstr_user.get()
        passwd_reg = regstr_pass.get()
        passwd2 = regstr_pass2.get()
        
        if name == '' or last_name == '' or user_reg == '' or passwd_reg == '' or passwd2 == '' :
            mb.showerror('Error', 'Missing data, make sure you fill in all the fields')
        else :
            conn = sql.connect('Base1.db')
            cursor = conn.cursor()
            cursor.execute(f'SELECT * FROM Base_1 WHERE username="{user_reg}"')
            if cursor.fetchall():
                mb.showerror('Error', f'The username "{user_reg}" is already in use.')
            elif cursor.fetchall() != True and passwd_reg == passwd2:
                cursor.execute(f"INSERT INTO Base_1 VALUES('{user_reg}', '{passwd_reg}', '{name}', '{last_name}')")
                conn.commit()
                mb.showinfo('Registration.', 'The user has been registered successfully!')
            elif passwd_reg != passwd2:
                mb.showerror('Error', 'The passwords do not match, try again.')
            
            cursor.close()
            conn.close()
    
    ctk.CTkButton(
        register_window, 
        text='Register', 
        font=("Arial", 18),
        border_color='#000000',
        hover_color='#C2C3C2',
        fg_color='#FFFFFF',
        text_color='#000000',
        border_width=1.5,
        command=register
    ).pack(ipadx=38, ipady=3, pady=12)

ctk.CTkButton(
    window, 
    text='Enter', 
    font=("Calibri Black",18),
    border_color='#000000',
    hover_color='#C2C3C2',
    fg_color='#FFFFFF',
    text_color='#000000',
    border_width=1.5,
    command=login
).pack(ipadx=38, ipady=3, pady=15)

ctk.CTkLabel(
    window, 
    text='Not registered yet? Click bellow!',
    text_color='#000000',
    fg_color=color1, 
    font=("Calibri Black",18)
).pack()

ctk.CTkButton(
    window, 
    text='Register',
    text_color='#000000',
    font=("Calibri Black",18),
    border_color='#000000',
    hover_color='#C2C3C2',
    border_width=1.5,
    fg_color='#FFFFFF',
    command=registerWindow
).pack(ipadx=34, ipady=3, pady=15)

window.mainloop()
