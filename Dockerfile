FROM python:3.11-slim
WORKDIR /app
COPY src/ .
RUN pip install flask

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run", "--port=5000"]
