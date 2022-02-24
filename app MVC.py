from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document



app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model2 = []


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    datos= [(i.id_person, i.name, i.last_name) for i in model]
    print(datos)
    return render_template('people.html', value=datos)

@app.route('/obras')
def obras():
    datos2 = [(

        j.id_obras,
        j.titulo,
        j.autores,
        j.publico_dato,
        j.editorial,
        j.numero_paginas
    ) for j in model2]
    print(datos2)
    return render_template('obras.html', value=datos2)


@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')

@app.route('/document_detail', methods=['POST'])
def document_detail():
    id_obras  = request.form['id_obras']
    titulo = request.form['titulo']
    autores = request.form['autores']
    publico_datos = request.form['publico_datos']
    editorial = request.form['editorial']
    numero_paginas = request.form['numero_paginas']
    document= document(id_obras = id_obras, titulo = titulo, autores = autores, publico_datos =publico_datos, editorial = editorial, numero_paginas = numero_paginas)
    model2.append(document)
    print(document)
    return render_template('document_detail.html', value=document)

@app.route("/person_delete/<id>")
def delete_person(id):
    for i in model:
        if i.id_person == id:
            temp = i
            model.remove(i)

    return "Eliminado la persona: " + temp.id_person + temp.name

@app.route("/person_update/<id>")
def update_person(id):
    return render_template("person_view_update.html", value=id)

@app.route("/person_update_for_real", methods=["POST"])
def persona_update_for_real():
    id_person = request.form['id_estatica_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']

    for i in model:
        if i.id_person == id_person:
            model.remove(i)
            new_i = Person(id_person=id_person, name=first_name, last_name=last_name)
            model.append(new_i)
            return people()



@app.route("/document_delete/<id>")
def delete_document(id):
    for i in model2:
        if i.id_obras == id:
            temp = i
            model2.remove(i)

    return "Eliminado el documento: " + temp.id_obras + temp.titulo

@app.route("/document_update/<id>")
def update_document(id):
    return render_template('document_view_update.html', value=id)

@app.route("/document_update_for_real", methods=['POST'])
def document_update_for_real():
    id_obras  = request.form['id_estatica']
    titulo = request.form['titulo']
    autores = request.form['autores']
    publico_datos = request.form['publico_datos']
    editorial = request.form['editorial']
    numero_paginas = request.form['numero_paginas']

    for i in model2:
        if i.id_obras == id_obras:
            model2.remove(i)
            new_i = document(id_obras = id_obras, titulo =titulo, autores = autores, publico_datos = publico_datos, editorial = editorial, numero_paginas = numero_paginas)
            model2.append(new_i)
            return obras()





if __name__ == '__main__':
    app.run(debug=True)
