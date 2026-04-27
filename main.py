from flask import Flask ,render_template, request, Response, send_from_directory
import pandas as pd
import os
import uuid
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


@app.route("/convert_csv",methods=['POST'])
def convert_csv():
    file = request.files['file']
    df = pd.read_excel(file)

    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers={
            'Content_Disposition': 'attachment; filename=result.csv'
        }
    )
    return response


@app.route("/convert_csv_two",methods=['POST'])
def convert_csv_two():
    file = request.files['file']
    df = pd.read_excel(file)

    if not os.path.exist('downloads'):
        os.makedirs('downloads')
    
    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))
    return render_template('download.html',filename=filename)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads',filename,download_name='result.csv')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)