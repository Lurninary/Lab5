from faker import Faker
import random
import json


fake = Faker()


def generate_profession():
    professions = ["Инженер-механик", "Биолог", "Пилот", "Врач", "Астроном", "Гид по Марсу", "Строитель", "Эколог",
                   "Финансист", "Юрист"]
    return random.choice(professions)


crew_members = []

for _ in range(10):
    crew_member = {
        "name": fake.first_name(),
        "last_name": fake.last_name(),
        "photo": f"{_}.jpg",
        "professions": [generate_profession(), generate_profession()]
    }
    crew_members.append(crew_member)

for member in crew_members:
    print(member)

json_string = json.dumps(crew_members, ensure_ascii=False)

with open('crew_members.json', 'w', encoding='utf-8') as file:
    file.write(json_string)