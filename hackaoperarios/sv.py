
from flask import Flask
from flask import request
from flask import jsonify
from scipy.optimize import linprog
import numpy as np
import json
import csv
import openpyxl
import sys
import os
import jwt
import datetime

app = Flask(__name__)

@app.route('/getToken', methods=['GET'])
def getToken():
    dia = float(request.headers["dia"])
    noche = float(request.headers["noche"])
    print("dia: ",dia)
    precios = {"dia" : dia, "noche": noche}

    consumo_maquinas = [150 ,10 ,25 ,30 ,100 ,40 ,15 ,10 ,3 ,200 ,25 ,15 ,400 ,35 ,3 ,250 ,50 ,30 ,
                        300 ,30 ,60 ,10 ,120 ,3 ,60 ,20 ,80 ,70 ,200 ,60 ,90 ,70 , 3]
    produccion_maxima = [150, 150, 150, 150, 110, 110, 110, 110, 110, 90, 90, 90, 90, 90, 90, 
                        80, 80, 80, 80, 80, 80, 80, 80, 66, 66, 66, 66, 66, 66, 60, 60, 60, 60]

    i = 4

    produccion = 2680

    c = np.array([-(precios["dia"] * consumo_maquinas[i]), -(precios["noche"] * consumo_maquinas[i])])

    a = [-produccion_maxima[i + 1], -produccion_maxima[i + 1]]
    b = [produccion_maxima[i], produccion_maxima[i]]

    A = np.array([[-1, -1], [-1, -0], [-0, -1], a, b])
    b = np.array([-18, -12, -12, -produccion, produccion])

    res = linprog(c, A_ub=A, b_ub=b,bounds=(0, None))

    print('Optimal value:', res.fun, '\nX:', res)
    return  json.dumps(abs(res.fun)),200

if __name__ == '__main__':
    generatedFilesFolder="models"

    app.run(debug=True, port=4000, host='0.0.0.0')