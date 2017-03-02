#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Nerea Del Olmo Sanz - GITT
Ejercicio 14.10

Clase para el recurso /hola
Devuelve hola o adios
"""

import webapp


class holaApp (webapp.app):

    def parse(self, request, rest):
        parsedReq = request.split()[1][1:]
        return parsedReq

    def process(self, parsedRequest):
        htmlAnswer = ("<html><h2>App id: /hola </h2><p>"
                      + str(parsedRequest) + "</p></html>")
        return ("200 OK", htmlAnswer)
