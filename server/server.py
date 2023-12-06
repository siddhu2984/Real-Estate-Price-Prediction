from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_location_name')
def get_location_name():
   response = jsonify({
      'locations':util.get_location_name()
   })
   response.headers.add('access-control-allow-origin','*') 
   return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
   total_sqft = float(request.form['total_sqft'])
   location = request.form['location']
   bhk = int(request.form['bhk'])
   bath = int(request.form['bath'])

   response = jsonify({
      'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
   })
   response.headers.add('access-control-allow-origin','*') 
   return response

if __name__ == '__main__':
   print("Starting Flask")
   util.load_saved_artifacts()
   app.run()
