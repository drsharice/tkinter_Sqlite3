from tkinter import *
import sqlite3

root = Tk()
root.title('GuiAPP')
root.geometry("400x400")

# Databases

#Create edit functions to Update a record

def update():
    # Create a database or connect to one
    conn = sqlite3.connect

