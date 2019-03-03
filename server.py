from flask import  Flask, render_template, Response, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


# @app.route('/get_data',methods=["POST","GET"])
# def get_data():
#     """Video streaming home page."""
#     # data = request.form["hello"]
#     # print(data)


#     return "Hello world"



if __name__ == '__main__':
    app.run(port=5555 ,threaded=True,ssl_context='adhoc',debug=True) #host='66.85.77.82',
