import os
import secrets
from PIL import Image
from flask import current_app


def save_picture(form_picture):
    """ save picture in picture_path """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f"{random_hex}{f_ext}"
    picture_path = os.path.join(
        current_app.root_path, 'static/media', picture_fn)

    img = Image.open(form_picture)
    img.save(picture_path)
    return picture_fn