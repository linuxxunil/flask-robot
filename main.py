from flask import Flask, jsonify
from flask import request
import time
app = Flask(__name__)

count = 0
@app.route("/MCS/api/clearCount", methods=['GET'])
def clearCount():
	global count
	count = 0
	return jsonify({"code":"0000"})


@app.route("/MCS/api/shutDown", methods=['POST'])
def shutDown():
	rep = {"code":"0000",
		"msg":"Success",
		"data":1}
	return jsonify(rep)

@app.route("/MCS/api/getLocation", methods=['GET'])
def getLocation():
	global count 
	count += 1
	print count
	if count > 10 :
		ip = request.args.get('ip', '')
		rep = {"code": "0000", 
				"msg": "Success", 
				"data": {
					"ip": "192.168.1.6",
					"mapName": "gridMap3.txt",
					"targetPoseX": 570,
					"targetPoseY": 1469,
					"targetPoseTheta": 2.9328134,
					"robotState": 0,
					"execId": 0,
					"robotStateName": "Running"
					}
				}

	else : 
		ip = request.args.get('ip', '')
		rep = {"code": "0000", 
				"msg": "Success", 
				"data": {
					"ip": "192.168.1.6",
					"mapName": "gridMap3.txt",
					"targetPoseX": 570,
					"targetPoseY": 1469,
					"targetPoseTheta": 2.9328134,
					"robotState": 1,
					"execId": 1,
					"robotStateName": "Running"
					}
				}

	return jsonify(rep)


@app.route("/MCS/api/getTaskByScanType", methods=['GET'])
def getTaskByScanType():
	if request.method == 'GET':
		'''
		scanType = request.args.get('scanType', '')
		if scanType == "1":
			rep = {"code": "0000" }
		else :
			rep = {"code": "0000" }

		return jsonify(rep)
		'''
		scanType = request.args.get('scanType', '')
		if scanType == "1":
			rep = {"code": "0000", 
					"msg": "Success", 
					"data": [{
						"pkTaskinfoId": "1",
						"taskName": "Task1",
						"taskType": 1,
						"appendOpType": 0,
						"pkAppendPoseId": 0,
						"mapName": "gridMap3.txt",
						"scanType": 1},
						{
						"pkTaskinfoId": "2", 
						"taskName": "Task2", 
						"taskType": 2, 
						"appendOpType": 0, 
						"pkAppendPoseId": 0, 
						"scanType": 1,
						"mapName": "gridMap3.txt"
						}] 
					}
		else :
			rep = {"code": "0000", 
					"msg": "Success", 
					"data": [{
						"pkTaskinfoId": "3",
						"taskName": "Task3",
						"taskType": 3,
						"appendOpType": 0,
						"pkAppendPoseId": 0,
						"mapName": "gridMap3.txt",
						"scanType": 2},
						{
						"pkTaskinfoId": "4", 
						"taskName": "Task4", 
						"taskType": 4, 
						"appendOpType": 0, 
						"pkAppendPoseId": 0, 
						"scanType": 2,
						"mapName": "gridMap3.txt"
						}] 
					}
		return jsonify(rep)
@app.route("/MCS/api/fixedPosition", methods=['GET'])
def fixedPosition():
	time.sleep(5)
	rep = {"code":"0000",
			"msg":"Success",
			"data":1}
	return jsonify(rep)


@app.route("/MCS/api/startExec", methods=['GET'])
def startExec():
	rep = {"code":"0000",
			"msg":"Success",
			"data":33}
	return jsonify(rep)

@app.route("/MCS/api/getLatestResult", methods=['GET'])
def getLastestResult():
	rep = {"code": "000",
		"msg":"Success",
		"data":3}
	return jsonify(rep)


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=9001)
