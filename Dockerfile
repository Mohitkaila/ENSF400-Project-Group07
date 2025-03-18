FROM python:3.9-slim
WORKDIR /app
COPY . .  
RUN pip install -r src/requirements.txt
EXPOSE 5000
ENV FLASK_ENV=production
ENV FLASK_APP=src/app.py

# Run tests 
CMD ["sh", "-c", "python test.py & python src/app.py"]
