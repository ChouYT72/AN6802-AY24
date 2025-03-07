from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("name")    
    return(render_template("main.html",name=name))
@app.route("/ethical_test",methods=["GET","POST"])
def ethical_test():   
    return(render_template("ethical_test.html"))
@app.route("/test_result",methods=["POST","GET"])
def test_result():
    answer = request.form.get("answer")
    if answer=="false": 
        return(render_template("pass.html"))
    if answer=="true": 
        return(render_template("fail.html"))
@app.route("/end",methods=["GET","POST"])
def end():  
    return(render_template("end.html"))
if __name__ == "__main__":
    app.run()
