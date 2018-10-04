import numpy as np
import cv2
from contextlib import closing
from videosequence import VideoSequence
from video_expression import face_detector, model_emoji, graph
from awesome_video_expression.settings import NB_STEP_FRAME

emotion_list=["Anger","Disgust","Fear","Happy","Sad","Surprise","Neutral"]
emotion_mapping = {
    "Anger" : "Neutral",
    "Disgust" : "Neutral",
    "Fear" : "Neutral",
    "Neutral" : "Neutral",
    "Happy" : "Happy",
    "Surprise" : "Happy",
    "Sad" : "Sad"
}

def get_box(image):
    """
        Generate the box of face in image
        Input:
            image: the numpy array format of image
        Output: the box (x, y, w, h) of all face in image
    """

    dets = face_detector(image, 1)
    faces = [[d.left(), d.top(), d.right(), d.bottom()] for d in dets]
    return faces

def find_first_face(faces, scale):
    """
        Find the first face of faces array
        Input:
            faces: the array of faces
        Output: the box (x, y, w, h) of first face in image
    """
    if len(faces):
        return np.divide(faces[0], scale).astype(int)
    return [0, 0, 0, 0]


def get_max_box(frames, nb_frames=10, scale=0.5):
    """
        Generate the max box of face in video
        Input:
            frames: the frames array of the videosequence
            nb_frames : number of random frame detection
            scale: the scale ratio for reduce caculation time
        Output: max box (x, y, w, h) of face in video
    """
    # Add padding for expand box
    img = np.array(frames[0])
    padding = int(img.shape[1] * 0.03)
    random_indexes = np.random.choice(range(len(frames)), size=nb_frames)
    # Init zeros box
    x = y = w = h = 0
    # Detection box of random
    for index in random_indexes:
        frame = np.array(frames[index])
        # Resize image for
        small = cv2.resize(frame, (0, 0), fx=scale, fy=scale)
        faces = get_box(small)
        # Find first face
        first_face = find_first_face(faces, scale)
        (x, y, w, h) = (max(x, first_face[0]), max(y, first_face[1]), max(w, first_face[2]), max(h, first_face[3]))
    # Add padding
    (x, y, w, h) = (
    max(0, x - padding), max(0, y - padding), min(w + padding, img.shape[1]), min(h + padding, img.shape[0]))

    return (x, y, w, h)

def crop_faces(img, box, crop_size=(48, 48)):
    """
        Crop the face in image with box
        Input:
            img: the numpy array of image as gray scale
            box: the box with (x, y, w, h) format
            crop_size : the size of image cropped
        Output:
            cropped_image with crop_size expand dim -1
    """
    (x, y, w, h) = box
    detected_face = img[int(y):int(h), int(x):int(w)]
    detected_face = cv2.resize(detected_face, crop_size)
    return np.expand_dims(detected_face, -1)


def generate_faces(video_path):
    """
        Generate the input data from video for machine learning emotion predict
        Input:
            video_path: the path of video
        Output:
            times : the mapping time of data
            face : the list of faces over frames
    """

    try:
        with closing(VideoSequence(video_path)) as frames:
            times = []
            faces = []
            # Caculate max box in video
            box = get_max_box(frames=frames, nb_frames=10)

            for i in np.arange(0, len(frames), step=NB_STEP_FRAME):
                gray = cv2.cvtColor(np.array(frames[i]), cv2.COLOR_RGB2GRAY)
                cropped_face = crop_faces(gray, box=box)
                times.append(i)
                faces.append(cropped_face)
            return times, faces, len(frames)
    except:
        print('Error')
        return [], [], 0

def predict(video_path):
    """
        Predict face expression in video_path
        Input:
            video_path: the path of video
        Output:
            result : the list of dict result with format {"keyframe" : keyframe, "emotion" : emotion}
            nb_frames : the number of frame
    """
    with graph.as_default():
        times, faces, nb_frames = generate_faces(video_path)
        if nb_frames:
            results = model_emoji.predict(np.array(faces))
            # Convert to emotion text
            emotions = [emotion_list[np.argmax(r)] for r in results]
            return [{'keyframe': int(times[i]), 'emotion': emotion_mapping[emotions[i]]} for i in range(len(emotions))], nb_frames
        return [], 0

