from keras.models import model_from_json, load_model
from awesome_video_expression.settings import (
    MODEL_EMOJI_JSON, MODEL_EMOJI_WEIGHTS, MODEL_FER2013_WEIGHT
)
import dlib
import tensorflow as tf

face_detector = dlib.get_frontal_face_detector()

graph = tf.get_default_graph()

model_emoji = model_from_json(open(MODEL_EMOJI_JSON, "r").read())
model_emoji.load_weights(MODEL_EMOJI_WEIGHTS)

emotion_classifier = load_model(
    MODEL_FER2013_WEIGHT,
    compile=False
)
