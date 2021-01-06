FROM python:3.5.2
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt 
COPY . .
ENV 'DB_URI'=getenv('DB_URI')
ENV 'SECRET_KEY'=getenv('SECRET_KEY')
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
