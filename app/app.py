from detector import *
from admin import *

app = Flask(__name__)
api = Api(app)

api.add_resource(detector, '/detect')
api.add_resource(classes, '/classes')


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5050)
    # app.run()