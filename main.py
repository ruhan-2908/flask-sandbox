from flask import Flask ,render_template, request
import pandas as pd
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
        

@app.route('/file_upload',methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    elif file.content_type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' or file.content_type == 'application/vnd.ms-excel':
        df = pd.read_excel(file)
        return df.to_html()


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)