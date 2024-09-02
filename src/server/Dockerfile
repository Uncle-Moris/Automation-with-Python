# Wybierz obraz bazowy z Pythonem
FROM python:3.8-slim

# Ustaw katalog roboczy w kontenerze
WORKDIR /app

# Skopiuj pliki zależności i zainstaluj je
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę plików aplikacji
COPY . .

# Ustaw zmienną środowiskową wskazującą na port, na którym uruchomiona zostanie aplikacja
ENV FLASK_APP=app.py

# Otwórz port 5000
EXPOSE 5000

# Uruchom aplikację Flask za pomocą Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
