From python:alpine3.14
WORKDIR /app
RUN apk add curl net-tools
COPY requirements.txt .
COPY main.py .
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
