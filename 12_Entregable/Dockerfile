FROM apache/airflow:latest AS de_ch

WORKDIR /requirements

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

WORKDIR /src