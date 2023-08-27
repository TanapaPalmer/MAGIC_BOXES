from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/box')
def one_box():
    return render_template("playground.html",num=1, color="lightblue")

@app.route('/box/<int:num>')
def box_by_num(num):
    return render_template("playground.html", num=num, color="lightblue")

@app.route('/box/<int:num>/<string:color>')
def box_by_num_and_color(num,color):
    return render_template("playground.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)