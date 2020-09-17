from flask import Flask, jsonify, request

app = Flask(__name__)
car= [{	"id":1,
      "Name":"chevrolet chevelle malibu",
   },
   {	"id":2,
      "Name":"buick skylark 320",
      
   },
   {	"id":3,
      "Name":"plymouth satellite",
      
   },
   {	"id":4,
      "Name":"amc rebel sst",
      
   }
]
bike=[
      {
         
         "id":10,
         "Name":"PR3 125 Enduro"
      },
      {
         
         "id":11,
         "Name":"PR3 125 Supermoto"
      },
      {
         
         "id":12,
         "Name":"PR3 240 Enduro"
      },
      {
         
         "id":13,
         "Name":"PR3 240 Supermoto"
      },
      {
         
         "id":14,
         "Name":"PR4 125 Enduro"}
]
@app.route('/', methods=['GET'])
def hello_world():
   resp = jsonify("Hello")
   resp.headers['Access-Control-Allow-Origin']='*'
   return resp
@app.route('/test1', methods=['GET','POST','OPTION'])
def send_data():
   
   
   if request.method=='POST':
      recived_data=request.data
      print(recived_data)
      recived_data=recived_data.decode("utf-8") 
      print(type(recived_data))
      if recived_data=="1":
         resp=jsonify(car)
         
      elif recived_data=="2":
         resp=jsonify(bike)
      else :
         resp=jsonify("Not found")
         resp.headers['Access-Control-Allow-Origin']='*'
         return resp
      
      resp.headers['Access-Control-Allow-Origin']='*'
      return resp
   else:
      resp = jsonify({'Product_price':0})
      resp.headers['Access-Control-Allow-Origin']='*'
      return resp

if __name__ == '__main__':
   app.run()


