from flask import Flask

app = Flask(_name_)

@app.route("/")
def hello_world():

    return "<p>Product Gone Live!! </p>"

    port_number = 8080

    if _name_ == '_main_':
        app.run(debug=True, host='0.0.0.0' , port=port_number)
