FROM python:3.11-slim
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt 
COPY . .

CMD [ "python","-u", "./main.py" ]
