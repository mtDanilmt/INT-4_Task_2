FROM python:3.10
WORKDIR /app
COPY main.py /app
EXPOSE 8080
CMD ["python", "main.py"]