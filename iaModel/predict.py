from fastapi import File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import json
import io
import os

router = APIRouter()

# Cargar modelo y clases
#print(os.path.exists("modelo_comidas_mobilenetv2_tf.keras"))

model = load_model("modelo_comidas_mobilenetv2_dataset.keras")

with open("clases.json", "r") as f:
    clases_dict = json.load(f)

# Invertir dict: índice → clase
clases = {v: k for k, v in clases_dict.items()}

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    img = Image.open(io.BytesIO(contents)).convert("RGB").resize((225, 225))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    pred = model.predict(img_array)[0]
    idx = int(np.argmax(pred))
    confidence = round(float(pred[idx]) * 100, 2)

    return JSONResponse(content={
        "prediction": clases[idx],
        "confidence": f"{confidence}"
    })
