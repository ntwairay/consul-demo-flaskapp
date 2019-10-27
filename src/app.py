#! /usr/bin/env python
import os
import re
from flask import Flask, render_template, url_for, redirect, request, flash, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456!234'

CORS(app)

@app.route('/')
def index():
    return redirect(url_for('timer', num=25*60))

@app.route('/<int:num>s')
@app.route('/<int:num>')
def timer(num):
    return render_template('index.html', num=num)

@app.route('/custom', methods=['GET', 'POST'])
def custom():
    time = request.form.get('time', 180)
    # use re to validate input data
    m = re.match('\d+[smh]?$', time)
    if m is None:
        flash(u'please enter a time 34、20s、15m、2h')
        return redirect(url_for('index'))
    if time[-1] not in 'smh':
        return redirect(url_for('timer', num=int(time)))
    else:
        type = {'s': 'timer', 'm': 'minutes', 'h': 'hours'}
        return redirect(url_for(type[time[-1]], num=int(time[:-1])))

@app.route('/<int:num>m')
def minutes(num):
    return redirect(url_for('timer', num=num*60))


@app.route('/<int:num>h')
def hours(num):
    return redirect(url_for('timer', num=num*3600))

# todo pomodoro mode: loop a 25-5 minutes cycle
@app.route('/pomodoro')
def pomodoro():
    return render_template('index.html')

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
