FROM python:alpine
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY del_2_marius.py ./del_2_marius.py
COPY secret/secret.txt ./secret/secret.txt
# COPY . .
RUN pip install -r requirements.txt
EXPOSE 3379
CMD ["uvicorn", "del_2_marius:app", "--reload", "--host", "0.0.0.0", "--port", "3379"]