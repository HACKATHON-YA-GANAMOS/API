from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps, loads
from flask.ext.jsonpify import jsonify
import recognition
import flask
import time
import requests
import utilities
import json
#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)
global counter
counter = 1
class Recognition(Resource):
    def get(self):
      #  conn = db_connect.connect() # connect to database
        #query = conn.execute("select * from employees") # This line performs query and returns json result
        #return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID
        print(time.time())
        return recognition.predict_with_url("http://assets.blog.foodnetwork.ca/wp-content/uploads/sites/6/2016/01/poutine-weeek.jpg").text

    def post(self):
        global counter
        #image = request.json["image"]
        #recibir la imagen y guardarla en un directorio en local
        #image_path = image_path
        #image = recognition.predict_with_url(image)
        #print(image)
        #print(prediction["probabilities"])
        #sorted_predictions = [prediction]
        #sorted_predictions = sorted(sorted_predictions, key=lambda k: k['probability'], reverse=True)
        image = request.files["picture"]
        image_path = "images/" + str(counter) + ".jpg"
        image.save(image_path)
        prediction = recognition.predict_with_url(utilities.get_image_url(image_path)).text
        prediction = loads(prediction)

        label = prediction["probabilities"][0]["label"]
        prob = prediction["probabilities"][0]["probability"]

        print(label, prob)
        d= utilities.jsonToDict("data_new.json")
        counter += 1
        try:
            return jsonify({"label": label, "probability": prob, "other_data":d[label] })
        except:
            return jsonify({"label": label, "probability": prob, "other_data": {}})
class TagFilter(Resource):
    def post(self):
        ingredients = request.json["ingredientes"]
        d1= utilities.jsonToDict("data_new.json")
        listeichon = []
        for recipe in d1:
            name = recipe.replace("+", "_")
            ingreds = d1[name]['ingredients']
            if ingreds is not None:
                eljoin = " ".join(ingreds)
                eljoin = eljoin.lower()
                contador = 0
                for i in ingredients:
                    if i not in eljoin:
                        break
                    else:
                        contador +=1
                if contador >= len(ingredients)    :
                    listeichon.append({"name": name, "recipe": d1[recipe]})
                    return jsonify(listeichon)
            else:
                continue
                


        #return jsonify(listeichon)
        


class Employees_Name(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Recognition, '/recognition') # Route_1
api.add_resource(TagFilter, '/tagfilter') # Route_2
#api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3


if __name__ == '__main__':
     app.run(host= "172.20.3.81", port='5002')