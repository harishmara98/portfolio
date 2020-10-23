from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


def write_to_file(data):
    name = data['username']
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('database.txt', 'a') as database:
        database.write(f'\n{name},{email},{subject},{message}')


def write_to_csv(data):
    name = data['username']
    email = data['email']
    subject = data['subject']
    message = data['message']

    with open('database.csv', 'a', newline='') as database:

        csvwriter = csv.writer(database, delimiter=',',
                               quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csvwriter.writerow([name, email, subject, message])


@app.route('/submitform', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return render_template('thankyou.html', name=data['username'])
    else:
        return 'Something went wrong.Please try again!!!'


@app.route('/<path:pagename>')
def my_generic(pagename):
    try:
        return render_template(pagename)
    except:
        return render_template('urlnotfound.html')


# @app.route('/index.html')
# def my_index():
#     return render_template('index.html')


# @app.route('/about.html')
# def my_about():
#     return render_template('about.html')


# @app.route('/contact.html')
# def my_contact():
#     return render_template('contact.html')


# @app.route('/works.html')
# def my_works():
#     return render_template('works.html')


# @app.route('/work.html')
# def my_work():
#     return render_template('work.html')


# @app.route('/components.html')
# def my_components():
#     return render_template('components.html')
