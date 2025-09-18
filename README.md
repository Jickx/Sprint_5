# Stellar Burgers - Автоматизация тестирования

Проект автоматизации тестирования веб-приложения **Stellar Burgers** с использованием **Selenium** и **pytest**.

[Перейти на сайт Stellar Burgers](https://stellarburgers.nomoreparties.site/)

---

## 📂 Структура проекта

```

├── README.md                      # Описание проекта и инструкции 
├── config.py                      # Конфигурационные параметры тестов 
├── conftest.py                    # Фикстуры и настройки pytest 
├── generators.py                  # Генераторы тестовых данных 
├── locators.py                    # Локаторы элементов для Selenium 
├── requirements.txt               # Список зависимостей проекта 
└── tests                           
    ├── test_ingredient_tabs.py    # Тесты вкладок ингредиентов 
    ├── test_login.py              # Тесты авторизации 
    ├── test_logout.py             # Тесты выхода из аккаунта 
    ├── test_personal_account.py   # Тесты личного кабинета 
    └── test_registration.py       # Тесты регистрации 
```

---

## ⚙️ Установка

1. Клонируйте репозиторий:
```bash
git clone <ссылка-на-репозиторий>
cd <папка-проекта>
````

2. Создайте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

---

## 🧪 Запуск тестов

Запуск всех тестов:

```bash
pytest -v
```

Запуск конкретного теста:

```bash
pytest tests/test_login.py -v
```

---

## 📌 Описание тестов

* **test\_registration.py** – проверка регистрации нового пользователя.
* **test\_login.py** – проверка входа в аккаунт различными способами.
* **test\_logout.py** – проверка выхода из личного кабинета.
* **test\_personal\_account.py** – проверка корректного отображения данных пользователя в личном кабинете.
* **test\_ingredient\_tabs.py** – проверка переключения вкладок ингредиентов на главной странице.

---

## 🔗 Сайт для тестирования

[Stellar Burgers](https://stellarburgers.nomoreparties.site/)

```

Если хочешь, могу сделать **ещё более наглядную версию со стрелочками и точной вложенностью всех папок**, чтобы было как дерево файлов в терминале.  

Хочешь, чтобы я так сделал?
```
