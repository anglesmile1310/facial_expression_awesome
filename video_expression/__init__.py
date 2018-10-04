from keras.models import model_from_json
from awesome_video_expression.settings import MODEL_EMOJI_JSON, MODEL_EMOJI_WEIGHTS
import dlib
import tensorflow as tf

face_detector = dlib.get_frontal_face_detector()
# load model

graph = tf.get_default_graph()

model_emoji = model_from_json(open(MODEL_EMOJI_JSON, "r").read())

model_emoji.load_weights(MODEL_EMOJI_WEIGHTS) #load weights