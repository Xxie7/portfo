from flask import Flask, render_template, url_for, request, redirect
import csv

#venv\Scripts\activate

#flask --app sever run
#flask --app sever --debug run

app = Flask(__name__)
print(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)  

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject}\n{message}')

def write_to_csv(data):
    with open('database.csv', newline = '', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter= ',', quotechar='"' , quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'someting went wrong. try again pls.'


#git config --global user.name "Xxie7"
#git config --global user.email "xxie7@buffalo.edu"

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)