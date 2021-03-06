from requests import get, delete, post, put

# Ввывод всех пользователей
print(get('http://localhost:5000/api/v2/users').json())
# Вывод одного пользователя
print(get('http://localhost:5000/api/v2/users/1').json())
# Удаление пользователя
print(delete('http://localhost:5000/api/v2/users/4').json())
# Не правильный запрос
print(post('http://127.0.0.1:5000/api/v2/users',
           json={'id': 3, 'name': 'Almaz', 'surname': 'Almazov',
                 'email': 'almaz@mail.ru', 'password': 'test',
                 'address': 'Almet'}, ).json())
# Правильный запрос
print(post('http://127.0.0.1:5000/api/v2/users', json={
    'name': 'Almaz',
    'surname': 'Almazov',
    'email': 'almaz@mail.ru',
    'password': 'test',
    'address': 'Almet',
    'age': 18,
    'position': 'special',
    'speciality': 'special',
    'city_from': 'Альметьевск'
}).json())
# Вывод всех работ
print(get('http://localhost:5000/api/v2/jobs').json())
# Вывод одной работы
print(get('http://localhost:5000/api/v2/jobs/1').json())
# Удаление одной работы
print(delete(f'http://localhost:5000/api/v2/jobs/7').json())
print(put('http://127.0.0.1:5000/api/v2/jobs', json={
    'team_leader': 1,
    'job': 'Упасть в пропость',
    'work_size': 45,
    'collaborators': '3, 4',
    'end_date': '34',
    'is_finished': False,
    'creater_id': 1
}).json())
