from flask import Flask
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        print("get is called")
        return {"data": "Hellow World"}

class AllDevices(Resource):
    def get(self):
        print("Gettings devices info")
        return {"Devices":["1.1.1.1", "1.1.1.2"]}
class Ips(Resource):
    def get(self):
        print("Gettings devices info")
        return {"Devices":["1.1.1.1", "1.1.1.2"]}
class DeviceInfo(Resource):
    def get(self, name):
        return {"IP":"1.1.1.2", "S/w version": 1.1}

class DeviceInfoWithVendor(Resource):
    def get(self, name, vendor):
        return {"IP":"1.1.1.2", "S/w version": 1.1, "vendor":vendor}
    
api.add_resource(HelloWorld, "/helloworld")
api.add_resource(Ips, "/ips")
api.add_resource(AllDevices, "/devices")
api.add_resource(DeviceInfo, "/devices/<string:name>")
api.add_resource(DeviceInfoWithVendor, "/devices/<string:name>/<string:vendor>")

if __name__ == "__main__":
    app.run(debug=True)
