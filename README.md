## Інструкція по запуску

```shell
#Python вже має бути встановлений

#Далі просто вставляй ці команди в консоль по порядку
1) https://github.com/MikhailLyvak/ChildrenHelp.git
2) python -m venv venv
3) venv\Scripts\activate (on Windows) | source venv/bin/activate (on macOS)
4) pip install -r requirements.txt
5) python manage.py migrate    <- migrations я вже зробив за тебе -_0.
6) python manage.py runserver
```

# Посилання
```shell
# Реєстрація/Логін/Аккаунт
http://127.0.0.1:8000/user/register/
http://127.0.0.1:8000/user/login/
http://127.0.0.1:8000/user/profile_view/

# Посилання на сайті
http://127.0.0.1:8000/home/  <- Домашня сторінка (трошки цікавої інфи допишете в HTML)
http://127.0.0.1:8000/help_list/ <- Список запитів на волонтерську допомогу
http://127.0.0.1:8000/myhelp_list/ <- Список ваших запитів на допомогу
```

# Додаткова інфа
```shell
# Інши ендпоінти є на кнопочках і трохи про них

На детальній сторінці к-ть і набір кнопок ситуативні
  - Якщо ти власник запиту на допомогу в тебе є кнопка позначення запиту як завершений
  - Якщо ти не власник в тебе буде кнопка зареєструвати себе як бажаючого допомогти

Також, якщо ви власник запиту на допомогу ви будете бачити і моб. телефони бажачих допомогти, що можна було з ними зв'язитись і тоді логічно позначити свій запит як виконаний
```
