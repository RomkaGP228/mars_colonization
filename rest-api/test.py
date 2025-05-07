import requests

# # получение всех работ
# print(requests.get('http://127.0.0.1:8080/api/jobs').json())
#
# # получение одной работы
# print(requests.get('http://127.0.0.1:8080/api/jobs/1').json())
#
# print(requests.get('http://localhost:8080/api/jobs/2').json())
#
# print(requests.get('http://localhost:8080/api/jobs/abc').json())

# проверка post без ошибки
print(requests.post('http://localhost:8080/api/jobs',
                    json={'team_leader_id': 1, 'job': 'add new job', 'work_size': 15, 'is_finished': False,
                          'collaborators': '2, 3'}).json())

# ошибка в том, что запрос пустой
print(requests.post('http://localhost:8080/api/jobs', json={}).json())

# ошибка в том, что нет поля team leader
print(requests.post('http://localhost:8080/api/jobs',
                    json={'job': 'new job', 'work_size': 15, 'is_finished': False,
                          'collaborators': '2, 3'}).json())

# ошибка в том, что нет поля job
print(requests.post('http://localhost:8080/api/jobs',
                    json={'team_leader_id': 1, 'work_size': 15, 'is_finished': False,
                          'collaborators': '2, 3'}).json())
