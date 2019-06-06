from flask import Flask, redirect, request


app = Flask(__name__)

@app.route('/capstone',methods=['POST'])
def hello():
	data = request.get_json()
	print(data);
	####
	# Insert proper code in here
	####
	return "hi"


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000,debug=True)
