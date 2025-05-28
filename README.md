## Приложение для прогноза погоды

Были использованы следующие технологии:
1. Django
2. Redis
3. HTML/CSS/Bootstrap


Из необязательных параметров было сделано:
- Написаны тесты
- Использован docker и docker-compose

<br>
Для получения данных о погоде было использовано API https://www.weatherapi.com/
<br><br>
!!! Для того чтобы воспользоваться приложением, необходимо получить API токен. Для этого нужно зарегистрироваться на https://www.weatherapi.com/ (с подтверждением почты)
<br>

### Инструкция по запуску приложения <br>
#### Без использования docker (У вас должен быть установленный redis):
1. В любой удобной вам директории скопируйте это приложение
```angular17html
git clone https://github.com/JaxckR/testTask_3.git
```
2. Создайте и активируйте переменное окружение<br>
Windows:
```angular17html
python -m venv venv
```
```angular17html
venv\Scripts\activate
```
Linux: 
```angular17html
python3 -m venv venv
```
```angular17html
source venv/bin/activate
```
3. Перейдите в директорию weather/src/ и примените миграции
```angular17html
cd weather/src
```
```angular17html
python manage.py migrate
```
4. Запустите приложение
```angular17html
python manage.py runserver
```
<br>

#### С использованием docker
1. В любой удобной вам директории скопируйте это приложение
```angular17html
git clone https://github.com/JaxckR/testTask_3.git
```
2. Перейдите в директорию weather/ и запустите docker-compose
```angular17html
cd weather
```
```angular17html
docker-compose up
```