from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

json_rest = {
   "code":200,
   "data":[
      {
         "videos_idvideos":1,
         "name":"Dunas",
         "thumbnail":"https://i3.ytimg.com/vi/hwH7nx8xZCs/maxresdefault.jpg"
      },
      {
         "videos_idvideos":2,
         "name":"Balneario",
         "thumbnail":"https://i3.ytimg.com/vi/hwH7nx8xZCs/maxresdefault.jpg"
      }
   ]
}

class Hello(Resource):
    def get(self, name):
        return json_rest
    
api.add_resource(Hello, '/sistema_recomendacion/<name>')

if __name__ == '__main__':
 app.run(debug=True)