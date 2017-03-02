#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 14.10

Método principal
"""

import webapp
import hola
import suma
import aleat


if __name__ == "__main__":
    appAleat = aleat.aleatApp()
    appHola = hola.holaApp()
    appSuma = suma.sumaApp()
    appAleat = aleat.aleatApp()
    testWebApp = webapp.webApp("localhost", 1234, {'/hola': appHola,
                                                   '/adios': appHola,
                                                   '/suma': appSuma,
                                                   '/aleat': appAleat})
