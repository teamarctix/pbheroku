FROM python:3.11
WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py .
CMD [ "python", "main.py" ]
