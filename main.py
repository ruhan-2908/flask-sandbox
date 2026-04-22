from flask import Flask, request, render_template
app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    myvalue = 'Ruhan'
    myresult = 10+20
    mylist = [10,20,30,40,50]
    sample = 20
    return render_template('index.html',myvalue=myvalue,myresult = myresult,mylist=mylist, mysample = sample)


@app.template_filter('reverse')
def reverse_string(str):
    return str[::-1]


if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug = True)