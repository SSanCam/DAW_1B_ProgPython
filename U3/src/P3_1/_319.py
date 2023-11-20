"""Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""


def cuenta_vocales(palabra: str):
    
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    for letras in palabra.lower():
        
        for vocal in letras:
            