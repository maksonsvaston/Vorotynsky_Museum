# Vorotynsky Museum (Flask)

Небольшой сайт на Flask (шаблоны Jinja2 + статика).

## Запуск локально

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Откройте http://127.0.0.1:5000

## Деплой на Render

Создайте **Web Service** (Python):

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn app:app`

Если Render ругается на порты ("No open ports detected"), используйте:

`gunicorn app:app --bind 0.0.0.0:$PORT`
