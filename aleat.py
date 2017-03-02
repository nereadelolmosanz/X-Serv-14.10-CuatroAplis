#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 14.10

Clase para el recurso /aleat
Devuelve URL aleatorias
"""

import webapp
import random


class aleatApp (webapp.app):

    def process(self, parsedRequest):
        randomURL = ("http://localhost:1234/aleat/" +
                     str(1000000000 * random.random()))
        htmlAnswer = ("<html><h2>App id: /aleat </h2>" +
                      "<a href=" + randomURL +
                      ">'Dame otra'</a><html>")
        return ("200 OK", htmlAnswer)
