import os
import cv2
import matplotlib.pyplot as plt
import numpy as np


# Функция изменения контраста изображения.
def change_contrast(filename, contrast_coeff):
    # Проверка значения.
    if contrast_coeff <= 0:
        contrast_coeff = 0.1

    # Чтение изображения.
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    # Разбиение имени файла.
    filename, file_extension = os.path.splitext(filename)
    filename_new_img = filename + '_contrast' + file_extension

    # Изменение контраста.
    new_img = cv2.convertScaleAbs(img, alpha=contrast_coeff, beta=0)

    # Сохранение результата.
    cv2.imwrite(filename_new_img, new_img)

    return filename_new_img


# Функция обработки изображения.
def processing_of_img(filename, scale):

    # Проверка значения.
    if scale <= 0:
        scale = 0.1

    # Чтение изображения.
    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    # Конвертация BGR -> RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Разбиение имени файла.
    filename, file_extension = os.path.splitext(filename)
    # Имя файла нового изображения после обработки.
    filename_new_img = filename + '_new' + file_extension
    filename_new_resized_img = filename + '_resized_new' + file_extension
    filename_img_arr = [filename_new_img, filename_new_resized_img]

    # Получаем размеры изображения.
    height, width = img.shape[:2]

    #Изменение размера
    new_size = (int(width * scale), int(height * scale))
    new_img = cv2.resize(img, new_size)

    # Конвертация уменьшенного изображения BGR -> RGB
    new_img_rgb = cv2.cvtColor(new_img, cv2.COLOR_BGR2RGB)

    #Добавляем графики
    fig = plt.figure(figsize=(15, 15))
    plot_countx = int(1 ** 0.5) + 1
    plot_county = int(1 ** 0.5) + 1
    viewer = fig.add_subplot(plot_countx, plot_county, 1)
    viewer.imshow(np.array(img_rgb))
    fig.savefig(filename_new_img, dpi=300, bbox_inches='tight')
    viewer.imshow(np.array(new_img_rgb))
    fig.savefig(filename_new_resized_img, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return filename_img_arr


# Функция для построения графика распределения цветов.
def to_create_plot(filename):
    # Чтение изображения.
    img = cv2.imread(filename, cv2.IMREAD_COLOR)

    # Разбиение имени файла.
    filename, file_extension = os.path.splitext(filename)
    filename_plot = filename + '_plot' + file_extension

    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    y, x, z = img_lab.shape
    flat_lab = np.reshape(img_lab, [y * x, z])

    colors = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    colors = np.reshape(colors, [y * x, z]) / 255.

    # Построение графика распределения цветов.
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(xs=flat_lab[:, 2], ys=flat_lab[:, 1], zs=flat_lab[:, 0], s=10, c=colors, lw=0)
    # Установка осей.
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # Сохранение графика в файл.
    fig.savefig(filename_plot)
    plt.close(fig)

    return filename_plot