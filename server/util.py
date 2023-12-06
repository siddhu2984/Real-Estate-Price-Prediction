import json
import pickle
import numpy as np

__data_columns = None
__locations = None
__model = None


def get_estimated_price(location,sqft,bhk,bath):
   try:
      loc_index = __data_columns.index(location.lower())
   except:
      loc_index = -1

   y = np.zeros(len(__data_columns))
   y[0] = sqft
   y[1] = bath
   y[2] = bhk

   if loc_index >= 0:
      y[loc_index] = 1
   return round(__model.predict([y])[0],2)

def get_location_name():
   return __locations

def load_saved_artifacts():
   print("Loading saved artifacts")
   global __data_columns
   global __locations
   global __model

   with open("artifacts/columns.json",'r') as f:
      __data_columns = json.load(f)["data_columns"]
      __locations = __data_columns[3:]

   with open("artifacts\Bangalore_home_price_prediction.pickle",'rb') as f:
      __model = pickle.load(f)
   print("loading artifacts done")

if __name__ == "__main__":
   load_saved_artifacts()
   print(get_location_name())
   print(get_estimated_price('1st Phase JP Nagar', 1000,2 ,2))
   print(get_estimated_price('Indira Nagar', 1000,3 ,3))
   print(get_estimated_price('Iira Nagar', 1000,3 ,3))


