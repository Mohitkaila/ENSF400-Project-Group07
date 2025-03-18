FROM python:3.9-slim
WORKDIR /app
COPY src/ .  
RUN pip install -r requirements.txt


# Exposing port and setting env. variables
EXPOSE 5000
ENV FLASK_ENV=production
ENV FLASK_APP=app.py

CMD ["sh", "-c", "python test.py & python app.py"]

