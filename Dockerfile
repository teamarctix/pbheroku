FROM python:3
WORKDIR /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py .
CMD [ "python", "main.py" ]
