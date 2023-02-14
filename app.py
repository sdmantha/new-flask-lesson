# Import the 'Flask' class from the 'flask' library.
from flask import Flask, request, jsonify


# Initialize Flask
# We'll use the pre-defined global '__name__' variable to tell Flask where it is. 
# More on this below.
app = Flask(__name__)

# Define our route
# This syntax is using a Python decorator, which is essentially a succinct way to wrap a function in another function.
@app.route('/')
def index():
  return "Hello, world!"

#   how to set up a route and the slug will be the <> then you have to define the function(and pass in the variable from the route)
@app.route('/say-hello/<name>')
def say_hello(name):
    return f'Hello, {name} !'

# lets differenciate the request names, we need to import request, we will check in postman
@app.route('/endpoint', methods=['GET', 'PUT', 'POST', 'DELETE'])
def endpoint():
  # you can check get by typing 'http://127.0.0.1:3030/endpoint' in the web
  if request.method == 'GET':
    return 'GET request'

  if request.method == 'PUT':
    return 'PUT request'

  if request.method == 'POST':
    return 'POST request'

  if request.method == 'DELETE':
    return 'DELETE request'


# we want to handle json, so we imorted it on top with jsonify
@app.route('/get-json')
# get request function
def get_json():
  return jsonify({
    "name": "Garfield",
    "hatesMondays": True,
    "friends": ["Sheldon", "Wade", "Orson", "Squeak"]
  })
# how to see if the json will show up on the web 'http://127.0.0.1:3030/get-json'

# lets make a new json
@app.route('/route')
def route():
  return 'people who pronounce data like data and not data are the worst people in the world'


# Run our application, by default on port 5000, you can change it to any number if u want  if you add a debug mode on then you can make changes and the website automatically makes the changes without having to exit out and restarting the server
app.run(port=3030, debug=True)












# from flask import Flask, request, jsonify
# from peewee import *
# from playhouse.shortcuts import model_to_dict, dict_to_model

# # make sure you change the pw you created
# db = PostgresqlDatabase('people', user='postgres', password='123', host='localhost', port=5432)

# class BaseModel(Model):
#   class Meta:
#     database = db

# class Person(BaseModel):
#   name = CharField()
#   age = IntegerField()

# db.connect()
# db.drop_tables([Person])
# db.create_tables([Person])

# Person(name='Raul', age=1000).save()
# Person(name='Chris', age=2000).save()
# # below, you can also write it like this
# johdan =Person(name='Johdan', age =300)
# johdan.save()

# app = Flask(__name__)

# @app.route('/person/', methods=['GET', 'POST'])
# @app.route('/person/<id>', methods=['GET', 'PUT', 'DELETE'])
# def endpoint(id=None):
#   if request.method == 'GET':
#     if id:
#         return jsonify(model_to_dict(Person.get(Person.id == id)))
#     else:
#         people_list = []
#         for person in Person.select():
#             people_list.append(model_to_dict(person))
#         return jsonify(people_list)

#   if request.method =='PUT':
#     body = request.get_json()
#     Person.update(body).where(Person.id == id).execute()
#     return "Person " + str(id) + " has been updated."

#   if request.method == 'POST':
#     new_person = dict_to_model(Person, request.get_json())
#     new_person.save()
#     return jsonify({"success": True})

#   if request.method == 'DELETE':
#     Person.delete().where(Person.id == id).execute()
#     return "Person " + str(id) + " deleted."

# app.run(debug=True, port=9000)

# how to check in the web if this works run ' http://localhost:9000/person/ '