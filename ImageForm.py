from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField
from wtforms import FloatField
from wtforms.validators import DataRequired, NumberRange



# Форма для загрузки изображения и выбора параметров.
class ImageForm(FlaskForm):
    contrast_coeff = FloatField('Изменить контраст:',
                       validators=[DataRequired(message="Поле не должно быть пустым!"),
                                   NumberRange(min=0.01, message="Масштаб должен быть больше 0!")],
                       default=0.50)

    scale = FloatField('Изменить масштаб:',
                       validators=[DataRequired(message="Поле не должно быть пустым!"),
                                   NumberRange(min=0.01, message="Масштаб должен быть больше 0!")],
                       default=0.15)

    # Поле загрузки файла. Валидатор укажет ввести корректный файл.
    img = FileField('Выберите файл-изображение:',
                             validators=[FileRequired(),
                                         FileAllowed(['jpg', 'jpeg', 'png'],
                                                     'Только файлы изображений!')])
