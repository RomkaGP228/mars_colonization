import requests

# получение всех работ
print(requests.get('http://127.0.0.1:8080/api/jobs').json())

# получение одной работы
print(requests.get('http://127.0.0.1:8080/api/jobs/1').json())

print(requests.get('http://localhost:8080/api/jobs/2').json())

print(requests.get('http://localhost:8080/api/jobs/abc').json())
