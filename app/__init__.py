from flask import Flask
from flask.json import jsonify
from flask import Response
from flask import json
from flask import render_template
from datetime import datetime

#our playground imports
from bikes import Mtb
from bikes import Bmx
import posts

def create_app(config_name):

    #create a new flask instance
    app = Flask(__name__)

    #using python decorators to extend functions without modifing them
    @app.route('/')
    def home():

        #lets render a template for an example
    	return render_template("index.html", time=str(datetime.now()))

    @app.route('/about')
    def about():

        #lets render a template for an example
        return render_template("about.html", time=str(datetime.now()))

    @app.errorhandler(404)
    def not_found(error=None):
        message = {
                'status': 404,
                'message': 'Not Found Amigo',
        }
        resp = jsonify(message)
        resp.status_code = 404

        return resp

    #an example of grabbing url params
    @app.route('/users/<userid>', methods = ['GET'])
    def api_users(userid):
        users = {'1':'john', '2':'steve', '3':'bill'}

        if userid in users:
            return jsonify({userid:users[userid]})
        else:
            return not_found()

    #an example of manually returning a flask response
    @app.route('/hello', methods = ['GET'])
    def api_hello():
        data = {
            'hello'  : 'world',
            'number' : 3
        }

        #Serialize obj to a JSON format #https://docs.python.org/2/library/json.html
        myjson = json.dumps(data)

        resp = Response(myjson, status=200, mimetype='application/json')
        resp.headers['Link'] = 'http://www.onefastsnail.com'

        return resp

    #an example of using custom modules and classes
    @app.route('/bikes')
    def bikes():

    	# Create an object of Mtb class
    	myMtb = Mtb()
    	myBmx = Bmx()

    	merge = myMtb.brands + myBmx.brands

    	merge.sort()

        #jsonify returns a flask response object
    	return jsonify(merge)

    #using our custom module that returns a local file of json
    @app.route('/posts')
    def api_posts():

    	allPosts = posts.getposts()

        #as we have json lets return a flask response object
    	return Response(allPosts, status=200, mimetype='application/json')

    #finally return the flask app instance to our entry file
    return app