FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV MONGO_AUTH_URI=mongodb+srv://yogesh-kumar:yogesh2829@oda.9uyfb.mongodb.net/AUTHDB
ENV BOOKING_SERVICE_URL=http://booking:5000/api

EXPOSE 5001

CMD [ "python", "run.py" ]