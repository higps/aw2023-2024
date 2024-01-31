FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt ./requirements.txt
COPY predict_house_price.py ./predict_house_price.py
COPY predict_houses_function.py ./predict_houses_function.py
COPY kc_house_data.csv ./kc_house_data.csv
# COPY . .
RUN pip install -r requirements.txt
EXPOSE 1337
CMD ["uvicorn", "predict_house_price:app", "--reload", "--host", "0.0.0.0", "--port", "1337"]

