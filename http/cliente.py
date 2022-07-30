from time import process_time_ns
from requests import request
import flask

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def root_post():
    print(flask.request.form)
    return 'ok\n'

if __name__ == '__main__':
    app.run(debug=True)