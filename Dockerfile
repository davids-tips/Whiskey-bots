FROM python:3.7-alpine
WORKDIR /code
ENV FLASK_APP=alpha/wb.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASH_APP=Slash/wb.py
ENV FLASK_RUN_HOST=0.0.0.1
ENV FLASK_APP=beta/wb.py
ENV FLASK_RUN_HOST=0.0.0.2
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]