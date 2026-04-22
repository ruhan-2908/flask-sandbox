from flask import Flask ,render_template, request

app = Flask(__name__,template_folder='templates')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':

        if 'username' in request.form.keys() and 'password' in request.form.keys():
            username = request.form['username']
            password = request.form['password']
            if username == 'Ruhan' and password == 'hello@123A':
                return "Success"
            else:
                return "Failure from bad credentials"
        else:
            return "Failure from no input"



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)