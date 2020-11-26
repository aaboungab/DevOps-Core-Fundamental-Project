FROM python:3.5.2
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt 
RUN chmod +x keys.sh
COPY . .
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]
