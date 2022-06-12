FROM python:3

# RUN mkdir -p /home/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "connect_oraculo.py"]
