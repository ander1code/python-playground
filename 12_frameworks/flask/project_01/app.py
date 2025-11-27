from flask import (
    Flask, 
    render_template, 
    request, 
    session,
    url_for,
    redirect,
    abort
) 

from json import dumps

# app = Flask(__name__)

app = Flask(__name__, static_folder='static', template_folder="templates")

app.secret_key = 'chave!' # para usar session!

@app.route("/", methods=['GET','POST'])
def index():
    session['name'] = 'Anderson'
    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            return f"Hello, {(request.get_json(silent=True) or {}).get("name")}!"
        return f"Hello, {request.form.get("name")}!"    
    else:
        return render_template('index.html', people=['Anderson', 'Mara', 'Sarah', 'Lucy'])

# ------------

@app.route("/home")
@app.route("/home/")
def home():
    return "<h1 style=\"color:red;\">Learning Flask!</h1>"

@app.route("/greeting/") # sempre com barra no final!
@app.route("/greeting/<name>")
def greeting(name=None):
    return f"<h1 style=\"color:blue;\">Hello, {name}!</h1>" 
        

@app.route("/age/<int:age>")
def show_age(age=0):
    return f"Age: {age}"

@app.route("/hello/")
@app.route("/hello/<string:name>")
def hello(name):
    return f"Hello, {name}!"

# REDIRECTS

@app.route("/redirect1")
def redirect_01():
    return redirect(url_for("home"))

@app.route("/redirect2/<string:name>")
def redirect_02(name):
    return redirect(url_for("hello", name=name))

@app.route("/google")
def redirect_to_google():
    return redirect("https://www.google.com.br")

@app.route("/greeting_post", methods=["POST", "GET"])
def greeting_post():
    if request.method == "POST":
        # return f"<h1 style=\"color:blue;\"><b style=\"background-color:brown;\">POST:</b> Hello {request.form.get("name")}!</h1>" 
        print(dumps(request.form))  # {"name": "Anderson", "btn_send": "SEND"}
        return render_template("form.html", name=request.form.get("name"))
    return render_template("form.html", name=None)

@app.route("/getargs", methods=["GET"])
def get_args():
    # http://127.0.0.1/getargs?name=Anderson&age=44
    print(request.args.to_dict())
    print(dict(request.args))
    return f"args: {dumps(request.args)} / Name: {request.args["name"]} or {request.args.get("name")}"

@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        # return redirect(url_for("to_success"), code=200) # TESTAR OS CODIGOS DE RETORNO AQUI!
        return redirect(url_for("to_success"), code=302) # automaticamente!
    else:
        abort(403) # forbidden

@app.route("/to_success")
def to_success():
    return f'Successfully!'

@app.route("/table")
def show_args_table():
    query=request.args.to_dict()
    return render_template("table.html", query=query)

@app.route("/showpost", methods=["POST", "GET"])
def show_post():
    from json import dumps
    if request.method == "POST":
        args = [str (v) for v in request.form.to_dict().values()]
        return args
    else:
        return render_template("forms/form.html")

@app.route("/sumnotas", methods=["POST", "GET"])
def sum_notas():
    if request.method == "POST":
        _sum = sum([int(v) for v in request.form.to_dict().values()])
        _avg = _sum/3
        if _avg >= 7:
            return "Aprovado"
        if _avg >= 5 and _avg < 7:
            return "Recuperação"
        if _avg < 5:
            return "Reprovado"
    else:
        return render_template("sum.html")


from flask import make_response

@app.route("/setcookie", methods=['POST','GET'])
def set_cookie():
    resp = make_response(render_template("cookie_form.html"))
    if request.method == 'POST':
        if request.form.get("name") or request.form.get("name").strip():
            name = request.form.get("name")
            resp.set_cookie("name", name)
        else:
            make_response(render_template("cookie_form.html"))     
    return resp
    
@app.route("/getcookie")
def get_cookie():
    if request.cookies.get("name"):
        return f"Hello, {request.cookies.get("name")}!"
    return "Hello, World!"

@app.route("/clearcookie")
def clear_cookie():
    repo = make_response(f"Cookie cleaned!")
    repo.set_cookie("name", "", expires=0)
    return repo

@app.route("/helloresp")
def hello_resp():
    repo = make_response("Hello, World!")
    return repo

@app.route("/helloresponse")
def render_resp():
    repo = make_response(render_template("temp_resp.html", message="Hello, World!"))
    return repo


@app.route("/setsession", methods=['POST','GET'])
def set_session():
    resp = make_response(render_template("session_form.html"))
    if request.method == "POST":
        if request.form.get("name") or request.form.get("name").strip():
            session["name"] = request.form.get("name")
            return f"Session created!"
    return resp
    
@app.route("/getsession")
def get_session():
    return make_response(render_template("session.html"))

@app.route("/clnsession")
def cln_session():
   session.pop("name", None)
   return make_response(f"Session cleaned!")


import os
UPLOAD_FOLDER = 'pictures'

from werkzeug.utils import secure_filename

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        path = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
        file.save(path)
        return "Successfully uploaded."
    return render_template("upload.html")

from flask import send_file

@app.route("/shwimg/<filename>")
def show_img(filename):
    file = os.path.join(UPLOAD_FOLDER, filename + ".jpg")
    return send_file(file, mimetype="image/jpg")
    
app.add_url_rule("/home", "home", home)
app.add_url_rule("/greeting", "greeting", greeting)
app.add_url_rule("/age", "age", show_age)
app.add_url_rule("/hello", "hello", hello)
app.add_url_rule("/redirect1", "redirect1", redirect_01)
app.add_url_rule("/redirect2", "redirect2", redirect_02)
app.add_url_rule("/google", "google", redirect_to_google)
app.add_url_rule("/greeting_post", "greeting_post", greeting_post)
app.add_url_rule("/getargs", "getargs", get_args)
app.add_url_rule("/post", "post", post)
app.add_url_rule("/to_success", "to_success", to_success)
app.add_url_rule("/table", "table", show_args_table)
app.add_url_rule("/showpost", "showpost", show_post)
app.add_url_rule("/sumnotas", "sumnotas", sum_notas)

# cookies
app.add_url_rule("/setcookie", "setcookie", set_cookie)
app.add_url_rule("/getcookie", "getcookie", get_cookie)
app.add_url_rule("/clearcookie", "clearcookie", clear_cookie)
# make_response
app.add_url_rule("/helloresp", "helloresp", hello_resp)
app.add_url_rule("/renderresp", "renderresp", render_resp)

# session
app.add_url_rule("/setsession", "setsession", set_session)
app.add_url_rule("/getsession", "getsession", get_session)
app.add_url_rule("/clnsession", "clnsession", cln_session)

# upload files:
app.add_url_rule("/upload", "upload", upload)
app.add_url_rule("/shwimg", "shwimg", show_img)


# ----------------------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=80)

