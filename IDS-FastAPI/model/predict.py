import joblib
import pickle
import pandas as pd
# import 
with open('model/IDS_model.pkl', 'rb') as f:
    model = joblib.load(f)
#extract model version using mlflow , ye 1.0.0 bas aise he likha 
MODEL_VERSION = '1.0.0'

def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    return output