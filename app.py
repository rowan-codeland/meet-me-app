import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
from dateutil.parser import parse
from datetime import datetime
if path.exists("env.py"):
    import env 

app = Flask(__name__)

app.config["MONGODB_NAME"] = os.environ.get('MONGODB_NAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/view_meetings')
def view_meetings():
    return render_template("view_meetings.html", meetings=mongo.db.meetings.find())

@app.route('/insert_meeting', methods=['POST'])
def insert_meeting():
    meetings = mongo.db.meetings

    meeting_name = request.form['meeting_name']
    meeting_duration = request.form['meeting_duration']
    meeting_description = request.form['meeting_description']
    meeting_date = parse(request.form['meeting_date'])

    meeting_form = {
        'meeting_name': meeting_name,
        'meeting_duration': meeting_duration,
        'meeting_description': meeting_description,
        'meeting_date': meeting_date
    }


    meetings.insert_one(meeting_form)
    return redirect(url_for('view_meetings'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)