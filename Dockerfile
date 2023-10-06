# Использую Python 3.11
FROM python:3.11

# Устанавливаю рабочую директорию и сразу устанавливаем увикорн
WORKDIR /app
RUN pip install uvicorn 

# Копирую файлы рекуармнн в контейнер и устанавливаем их
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирую остальные файлы проекта в контейнер так было написано в форуме 
COPY . .

# Экспортирую порт 8000 будем юзать фаст апи
EXPOSE 8000

# Запускаю FastAPI 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
