# Шагайны дүрс таних

Гүн сургалтын (Deep Learning) арга ашиглан зурагнаас шагайн хэлбэрийг таних моделийг [Deep Learning UB 2018](https://www.facebook.com/events/1918739155078866/) зуны сургалтын хүрээнд сургаж туршсан. Танилтыг объект илрүүлэх хурдан бөгөөд нарийвчлал өндөртэй аргуудын нэг болох [RetinaNet](https://arxiv.org/abs/1708.02002)-ийг ашигласан.

![жишээ](test_44.png)

## Ашиглах

1. `pip install -r requirements.txt` шаардлагатай сунгуудыг суулгана. (GPU ашиглах бол `tensorflow`-г `tensorflow-gpu` болгон өөрчлөөрэй)
2. `$ jupyter notebook` jupyter дэвтрийн серверийг асаана.
3. `abr_test.ipynb` руу орж сургасан модель болгон шалгах зургуудын байршлыг тохируулан ажиллуулна.

## Сургах

1. `pip install -r requirements.txt` шаардлагатай сангуудыг суулгана.
2. Jupyter notebook ашиглах бол `$ jupyter notebook` jupyter дэвтрийн серверийг асаана.
3. Jupyter дэвтэр ашиглах бол `abr_train.ipynb` дэвтрийг ашиглан шинэ модель сургана. Хэрэв дэвтэр ашиглахгүй бол `train.py` файлыг ашиглана.
4. `abr_train.ipynb` эсвэл `train.py` доторх параметруудыг сургалтандаа тохируулан өөрчилж сургалтаа эхэлнэ.

## Татах файлууд

Dataset: [Google Drive (Зургууд)](https://goo.gl/Uq856R), label нь `ankle_bones_dataset` хавтсанд

Сургасан модель: [Google Drive](https://goo.gl/cYiXno)
