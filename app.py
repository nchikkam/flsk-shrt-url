from flask import Flask, request, render_template, redirect
from database import Urls, Session
import sys
import random
import string
import sqlalchemy

app = Flask(__name__)
modules = {
    'python': sys.version,
    'flask': 'Flask 3.1.1',
    'db sqlalchemy': sqlalchemy.__version__
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_link']
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        
        new_entry = create_entry(short_url, original_url)

        with Session() as session:
            session.add(new_entry)
            session.commit()

    return render_template('index.html', entries = Session().query(Urls), versions = modules)


def create_entry(short_url, original_url):
    return Urls(short_url = short_url, original_url = original_url)

@app.route("/<short_url>", methods=['GET'])
def direct_to_original(short_url):
    with Session() as session:
        entry = session.query(Urls).filter(Urls.short_url == short_url).first()
        if entry:
            return redirect(entry.original_url)
        else:
            return render_template('index.html', versions = modules)
