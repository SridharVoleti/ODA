FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

ENV MONGO_DEV_URI=mongodb+srv://yogesh-kumar:yogesh2829@oda.9uyfb.mongodb.net/DEVDB
ENV MONGO_TEST_URI=mongodb+srv://yogesh-kumar:yogesh2829@oda.9uyfb.mongodb.net/TESTDB
ENV AUTH_URL=http://auth:5000

EXPOSE 5000

CMD [ "python", "run.py" ]