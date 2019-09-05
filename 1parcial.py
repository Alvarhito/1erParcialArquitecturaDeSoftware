from flask import Flask, request
import time
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route("/log", methods=["GET", "POST"])
def log():
	ti=request.args.get("time")
	te=request.args.get("temp")
	hu=request.args.get("hum")
	
	time_string = time.strftime("%m%d%Y", time.localtime())

	file_=open(time_string+".csv","a")

	file_.write(str(time.strftime("%H:%M:%S", time.localtime()))+","+str(ti)+","+str(te)+","+str(hu)+"\n")
	file_.close()

	return "Success"

if __name__ == "__main__":
    app.run(debug=False)