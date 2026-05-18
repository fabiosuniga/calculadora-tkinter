#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importando biblioteca
import tkinter as tk


# In[2]:


# Funções chamada, limpar e calcular
def click(num):
    entry.insert(tk.END, num)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result=eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")


# In[3]:


#Cria a janela principal e o título
root = tk.Tk()
root.title("Calculadora Simples")


# In[4]:


# Cria o campo de entrada e o campo dos resultados
entry=tk.Entry(root, width=20, borderwidth=5, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4)

# Lista com os rotulos de cada botão
buttons = [
    '7', '8', '9', '+', 
    '4', '5', '6', '-', 
    '1', '2', '3', '*', 
    '0', 'C', '=', '/', 
]

row, col = 1,0


# In[5]:


# loop que cria o posiciona cada botão
for b in buttons:
    if b == 'C':
        action=clear
    elif b =='=':
        action=calculate
    else:
        action=lambda x=b: click(x)

    btn=tk.Button(root, text=b, width=5, height=2, command=action)
    btn.grid(row=row, column=col)

    col+=1          # avança uma coluna para a direita
    if col>3:       # se já passou da última coluna (0,1,2,3 -> total 4 colunas)
        col=0       # volta para a primeira coluna
        row+=1      # descer para a próxima linha

root.mainloop()

