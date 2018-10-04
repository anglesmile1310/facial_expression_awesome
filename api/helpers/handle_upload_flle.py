import os
from time import time
from awesome_video_expression.settings import VIDEO_UPLOAD_MODEL

def handle_uploaded_file(f):
    temp_path = os.path.join(VIDEO_UPLOAD_MODEL, '{}_{}')
    temp_path = temp_path.format(time(), f.name)
    temp_path = os.path.splitext(temp_path)[0] + '.mp4'

    with open(temp_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return temp_path

def remove_upload_file(path):
    try:
        os.unlink(path)
    except:
        pass