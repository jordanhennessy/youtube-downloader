FROM python:3.11
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8502
COPY src /app
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port", "8502"]