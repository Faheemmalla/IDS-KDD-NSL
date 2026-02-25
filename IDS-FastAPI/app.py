from fastapi import FastAPI
from fastapi.responses import JSONResponse
import joblib
#user input wali jo pydantic class banayi hai aussi ko yahan load kr rahe hai so that we can use it
from schema.user_input import UserInput
##
from model.predict import predict_output,model,MODEL_VERSION


app = FastAPI()

@app.post('/predict')
def predict(input_data: UserInput):

    #providing data to model in correct order for prediction
    user_input = {
            'src_bytes': input_data.src_bytes,
            'dst_bytes': input_data.dst_bytes,
            'count': input_data.count,
            'srv_count': input_data.srv_count,
            'num_failed_logins': input_data.num_failed_logins,
            'num_compromised': input_data.num_compromised,
            'serror_rate': input_data.serror_rate,
            'rerror_rate': input_data.rerror_rate,
            'num_file_creations': input_data.num_file_creations,
            'num_shells': input_data.num_shells
    }
    #making prediction
    #isse we will get a list , aus list ka 0th item chahiye hoga isseliye [0]
    try:
        prediction = predict_output(user_input)
        return JSONResponse(
            status_code=200, 
            content={'prediction': int(prediction),'result': 'anomaly' if prediction else 'normal'
            }
        )
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
#human readable
@app.get('/')
def home():
    return {'message':'Intrusion Detection System API'}

#health check endpoint (isse aws ko pata lagta hai ki api live hai ya nhi )
#machine readable
@app.get('/health')
def health_check():
    return {'status': 'OK',
            'version': MODEL_VERSION,
            'model Loaded':model is not None
            }
