import os

from flask import Flask
from flask import render_template
from werkzeug.utils import secure_filename

from ImageForm import ImageForm
from functions import change_contrast, processing_of_img, to_create_plot

app = Flask(__name__)

# Используем CSRF-токен.
SECRET_KEY = 'secret'
app.config['SECRET_KEY'] = SECRET_KEY


# Декоратор для вывода страницы по умолчанию (главной страницы).
@app.route("/")
def index():
    # Передаем данные в шаблон и вызываем его.
    return render_template('index.html')


# Декоратор для вывода страницы загрузки изображения.
@app.route('/run_app', methods=['GET', 'POST'])
def run_app():
    # Форма.
    form = ImageForm()
    if form.validate_on_submit():
        # Получаем имя файла-изображения.
        filename_img = os.path.join(r'./static/images',
                                    secure_filename(form.img.data.filename))

        # Сохраняем первый файл-изображение на сервере.
        form.img.data.save(filename_img)

        # Производим обработку изображения по дополнительному заданию.
        filename_img_contrast = change_contrast(filename_img, form.contrast_coeff.data)

        # Производим обработку изображения по заданию.
        filename_img_arr = processing_of_img(filename_img, form.scale.data)

        # Создаём график распределения цветов для исходного изображения.
        filename_img_new_plot = to_create_plot(filename_img)
        # Создаём график распределения цветов для полученного изображения.
        filename_img_contrast_new_plot = to_create_plot(filename_img_contrast)

        # Передаём переменные в шаблон.
        return render_template('result.html',
                               img=filename_img,
                               img_new_contrast=filename_img_contrast,
                               img_new=filename_img_arr[0],
                               img_resized_new=filename_img_arr[1],
                               img_new_plot=filename_img_new_plot,
                               img_contrast_new_plot=filename_img_contrast_new_plot,
                               )
    else:
        return render_template('form.html', form=form, result=u'Загрузите файл-изображение!')


# Запуск.
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=False)
