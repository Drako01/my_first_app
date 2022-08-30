
import sqlite3
import requests
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return HttpResponse("¡Hola, mundo...!")


def acerca_de(request):
    return HttpResponse('Hola a todos, esto es Acerca de.!')


def cursos(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    html = """   
        <html>    
            <title>Lista de Cursos</title>
            <table style="border: 1px solid #000">
                <thead>
                    <tr>
                        <th>Curso</th>
                        <th>Inscriptos</th>
                    </tr>
                </thead>
    """
    for nombre, inscriptos in cursor.fetchall():
        html += f"""
        <tr>
            <td>{nombre}</td>
            <td>{inscriptos}</td>
        </tr>
        """
    html += "</table></html>"
    conn.close()
    return HttpResponse(html)


def cursos_json(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscriptos FROM cursos")
    response = JsonResponse(cursor.fetchall(), safe=False)
    conn.close()
    return response


def cotizacion_dollar(request):
    r = requests.get('https://api.recursospython.com/dollar')
    dollar = r.json()
    html = """
            <html>
                <head>
                <title> Valor del Dolar </title>
                </head>
                <body>
                <h1>El Valor del Dolar hoy:</h1>
                    <h3><strong>Para la Compra: </strong> ${compra} </h3>
                    <h3><strong>Para la Venta: </strong> ${venta}</h3>
                </body>
            """.format(compra=dollar["buy_price"], venta=dollar["sale_price"])
    return HttpResponse(html)


def aeropuertos(request):
    f = open("aeropuertos.csv", encoding="utf8")
    html = """
        <html>
        <title>Lista de aeropuertos</title>
        <table style="border: 1px solid">
        <thead>
            <tr>
            <th>Aeropuerto</th>
            <th>Ciudad</th>
            <th>País</th>
            <th>Siglas</th>
            </tr>
        </thead>
    """
    for linea in f:
        datos = linea.split(",")
        nombre = datos[1].replace('"', "")
        ciudad = datos[2].replace('"', "")
        pais = datos[3].replace('"', "")
        siglas = datos[4].replace('"', "")
        html += f"""
            <tr>
            <td>{nombre}</td>
            <td>{ciudad}</td>
            <td>{pais}</td>
            <td>{siglas}</td>
            </tr>
        """
    f.close()
    html += "</table></html>"
    return HttpResponse(html)


def aeropuertos_json(request):
    f = open("aeropuertos.csv", encoding="utf8")
    aeropuertos = []
    for linea in f:
        datos = linea.split(",")
        aeropuerto = {
            "nombre": datos[1].replace('"', ""),
            "ciudad": datos[2].replace('"', ""),
            "pais": datos[3].replace('"', ""),
            "siglas": datos[4].replace('"', "")
        }
        aeropuertos.append(aeropuerto)
    f.close()
    return JsonResponse(aeropuertos, safe=False)
