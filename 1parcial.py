from flask import Flask, request
import time
app = Flask(__name__, static_folder='.', static_url_path='')


class Singleton:
	__instance = None
	@staticmethod 
	def getInstance():
		""" Static access method. """
		if Singleton.__instance == None:
			Singleton()
		return Singleton.__instance
	def __init__(self):
		""" Virtually private constructor. """
		if Singleton.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			Singleton.__instance = self
	def saveData(ti,te,hu):
		time_string = time.strftime("%m%d%Y", time.localtime())

		file_=open(time_string+".csv","a")

		file_.write(str(time.strftime("%H:%M:%S", time.localtime()))+","+str(ti)+","+str(te)+","+str(hu)+"\n")
		file_.close()

@app.route("/log", methods=["GET", "POST"])
def log():
	ti=request.args.get("time")
	te=request.args.get("temp")
	hu=request.args.get("hum")
	
	save=Singleton()
	save.saveData(ti,te,hu)

	return "Success"

if __name__ == "__main__":
    app.run(debug=False)