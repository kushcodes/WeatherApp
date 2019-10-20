#!/usr/bin/env python
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from flask_s3 import FlaskS3


app = Flask(__name__)
app.config['FLASKS3_BUCKET_NAME'] = 'ilovekushti'
s3 = FlaskS3(app)

@app.route('/')
def index():
    return render_template(
        'weather.html',
        data=[{'name': 'Old Bridge'},
              {'name': 'New York'},
              {'name': 'Philadelphia'},
              {'name': 'Miami'},
              {'name': 'San Diego'},
              {'name': 'Mexico City'},
              {'name': 'London'},
              {'name': 'Tokyo'},
              {'name': 'New Delhi'},
              {'name': 'Sydney'}]
    )


@app.route("/result", methods=['GET', 'POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template('result.html', data=data, error=error)


if __name__ == '__main__':
    app.run(debug=True)


