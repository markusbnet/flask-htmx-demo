from flask import Flask, render_template, request

data = ["Mark", "John"]

app = Flask(__name__)


@app.route("/name/create", methods=["POST"])
def name_create():
    name = request.form["create"]
    data.append(name)
    response = f"""
    <tr>
        <td><input readonly type="text" name='{name}' value='{name}'></td>
    </tr>
    """
    return response


@app.route("/")
def index():
    return render_template("index.html", items=data)
