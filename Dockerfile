FROM python:3.5.2
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt 
COPY . .
RUN . scripts/key.sh
ENV 'DB_URI'=${DB_URI}
ENV 'SECRET_KEY'=${SECRET_KEY}
RUN python create.py
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
