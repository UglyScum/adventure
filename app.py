#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, json, request
from urlparse import parse_qs
app = Flask(__name__)
game = {}

@app.route("/")
def page_main():
    return "Привет!"

@app.route("/game",methods=['POST','GET'])
def page_game():
	query=parse_qs(request.query_string)
	#return json.dumps(game['questions'][query['question'][0]])
	if 'question' in query:
		question = game['questions'][query['question'][0]]
	else:
		question = game['questions']['direction']
	return render_template('game.html', 
			game=game, 
			question=question,
			query=query, 
			request=request.form)

if __name__ == "__main__":
	game = json.load(open('levels/level2.json', "r"))
	app.run()
