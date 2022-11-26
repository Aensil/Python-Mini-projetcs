#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import sqlite3
# ataque por SQL Injection
# INSERT INTO personas VALUES ('Ale',30); DELETE FROM personas; --', 30
 
# >> Ingrese su nombre: Ale',30); DELETE FROM personas;--
# >> Ingrese su edad: 30
 
# ¿Como queda la consulta?
# "INSERT INTO personas VALUES('Ale',30); DELETE FROM personas;--,30)"
 
conn = sqlite3.connect("base.sqlite")
 
cursor = conn.cursor()
 
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
 
 
# add the data to the TABLE
cursor.executescript(f"INSERT INTO personas VALUES('{nombre}',{edad})")
conn.commit()
 
 
cursor.execute("SELECT * FROM personas")
valores = cursor.fetchall()
print(valores)
 
 
conn.close()