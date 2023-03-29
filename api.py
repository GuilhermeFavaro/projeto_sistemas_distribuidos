
from webbrowser import get
from flask import Flask, request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

filmes_data ={
    1: {
        "id": 1,
        "name": "Insterestelar",
        "genero":"Aventura",
        "duração/h":2,
    },
    2: {
        "id": 2,
        "name": "Piratas do Caribe",
        "genero": "Aventura",
        "duração/h":3,
    }
}

def response_filmes():
    return {"filmes": list(filmes_data.values())}

#recurso 1 get by id
@app.route("/recurso1/<int:filme_id>", methods=["GET"])
def get(filme_id: int):
    filme = filmes_data.get(filme_id)
    
    if filme:
         filmes_data.get[filme_id]

    return response_filmes()

#recurso 1.1 POST
@app.route("/recurso1", methods=["POST"])
def create_filme():
    body = request.json

    ids = list(filmes_data.keys())

    if ids:
        new_id = ids[-1] + 1
    else:
        new_id = 1

    filmes_data[new_id] = {
        "id": new_id,
        "name": body["name"],
        "genero": body["genero"]
    }   
    return response_filmes()

#Recurso 2
@app.route("/recurso2")
def list_filmes():
    return response_filmes()


#recurso 3 delete
@app.route("/recurso3/<int:filme_id>", methods=["DELETE"])
def delete(filme_id: int):
    filme = filmes_data.get(filme_id)
    
    if filme:
        del filmes_data[filme_id]

    return response_filmes()

#recurso 3.1 put
@app.route("/recurso3/<int:filme_id>", methods=["PUT"])
def putmethod(filme_id: int):
    body = request.json
    name = body.get("name")

    if filme_id in filmes_data:
        filmes_data[filme_id]["name"] = name

    return response_filmes()


#recurso 4 Patch
@app.route("/recurso4/<int:filme_id>", methods=["PATCH"])
def attpatch(filme_id: int):
    body = request.json
    genero = body.get("genero")

    if filme_id in filmes_data:
        filmes_data[filme_id]["genero"] = genero

    return response_filmes()


#recurso 5 get by duration
@app.route("/recurso5/<int:filme_dur>", methods=["GET"])
def getbydur(filme_dur: int):
    filme = filmes_data.get(filme_dur)
    
    if filme:
         filmes_data.get[filme_dur]

    return response_filmes()

app.run(debug=True)


