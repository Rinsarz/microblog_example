# -*- coding: utf-8 -*-

from microblog_app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Alexander'}
	posts = [
		{
			'author':{'username':'Andrew'},
			'body':'What a nice weather in the California!'
		},
		{
			'author':{'username':'Max'},
			'body':'I like to swim in the Poland waterpools!'
		},
		{
			'author':{'username':'Sergei'},
			'body':'Have a nice day, Karl!!'
		},
		{
			'author':{'username':'Karl'},
			'body':'ВСЕМ ПРЕВЕД!!'
		}
	]
	return render_template('index.html', posts=posts, user=user)
