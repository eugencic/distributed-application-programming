FROM python:3.10.7

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 7071

# ENV NAME traffic-analytics-service-1

CMD ["python", "-u", "main.py", "--port", "7071"]
