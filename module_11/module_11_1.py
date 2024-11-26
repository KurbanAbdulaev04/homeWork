# начну пожалуй с библиотеки requests
# используется для HTTP запросов
import requests

# например можем запросить какую-нибудь картинку, методом get, и сохранить ее в виде файла
img_url = 'https://avatars.mds.yandex.net/i?id=7cb577fccf8b7354b5248cb8101dd09433fa521f-4253662-images-thumbs&n=13'
r = requests.get(img_url)

with open('cat.png', 'wb') as cat_file:
    # Используем метод content, т.к. ответом на запрос является файл
    cat_file.write(r.content)

# так же с помощью метода status_code, можно узнать, выполнился-ли наш запрос успешно(состояние запроса)
print(r.status_code)
# 200-запрос выполнен успешно

# так же есть все возможные методы, которые имеют схожий функционал работы,
# не смог придумать как мне ими воспользоваться пока


# =========================================================================================================


# далее можно эту картинку преобразовать с помощью библиотеки pillow(PIL)
from PIL import Image, ImageFilter, ImageEnhance

p1 = Image.open('cat.png')
# можно узнать какие-нибудь данные об изображении
print(p1.size)
print(p1.format) # не знаю почему формат показывает jpeg
print(p1.mode)
print(p1.info)

# изменяем размер фотографии, отзеркалим и сохраняем
cat_resize = p1.crop((100, 40, p1.height+80, p1.height-40)).transpose(Image.Transpose.FLIP_LEFT_RIGHT)
cat_resize.save('cat_resize.jpeg')

# попытаемся улучшить фото
cat_resize.filter(ImageFilter.DETAIL)
cat_ = ImageEnhance.Contrast(cat_resize)
cat_.enhance(1.3).show()
# не очень получилось, но пойдет

# с помощью этой библиотеки(pillow) можно одинаково(или не одинаково) обработать много фотографий довольно быстро

