from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    
    pitch = TextAreaField(' Blog', validators = [Required()])
    
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')  
class CommentForm(FlaskForm):
    comment = TextAreaField('Type in a comment',validators = [Required()])
    submit = SubmitField('Submit')          