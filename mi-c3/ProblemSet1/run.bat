docker build -t time-difference-api .


docker run -d -p 8000:5000 --name api-instance1 time-difference-api 

docker run -d -p 8001:5000 --name api-instance2 time-difference-api