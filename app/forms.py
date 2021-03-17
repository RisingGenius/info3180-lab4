from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class UploadForm(FlaskForm):
    pic = FileField('Upload Image', validators=[ FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!') ])
