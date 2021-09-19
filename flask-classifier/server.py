import io
from PIL import Image
import numpy as np
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils
from flask import Flask, request


app = Flask(__name__)
model = None
app.config['SERVER_NAME'] = 'flask-classifier:5000'


def load_model():
    global model
    model = ResNet50(weights="imagenet")


def prepare_image(image, target):

    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    return image


@app.route("/predict", methods=["POST"])
def predict():

    if request.method == "POST":

        img = request.files.get('image')

        if not img:
            return 404
        
        img = img.read()
        img = Image.open(io.BytesIO(img))
        img = prepare_image(img, target=(224, 224))

        preds = model.predict(img)
        results = imagenet_utils.decode_predictions(preds)

        data = {} 
        data["predictions"] = []

        for (_, label, prob) in results[0]:
            r = {"label": label, "probability": float(prob)}
            data["predictions"].append(r)

        print(data)

    return data


if __name__ == "__main__":
    load_model()
    app.run(debug=True, port=5000)