from datetime import datetime
from faker import Faker
import random

class ColonistGenerator:
    def __init__(self):
        self.fake = Faker()
        self.crew_members = []

    def generate_position(self):
        positions = ["Engineer", "Doctor", "Biologist", "Astronomer", "Pilot", "Middle Engineer", "Chief Engineer"]
        return random.choice(positions)

    def generate_profession(self, position):
        profession_variations = {
            "Engineer": ["Software Development Engineer", "Project Engineer", "Automotive Engineer"],
            "Doctor": ["Surgeon", "Traumatologist", "Ophthalmologist"],
            "Biologist": ["Geneticist", "Ecologist", "Microbiologist"],
            "Astronomer": ["Space Researcher", "Astrophysicist", "Astronaut"],
            "Pilot": ["Commercial Pilot", "Military Pilot", "Helicopter Pilot"],
            "Middle Engineer": ["Junior Software Developer", "Assistant Project Manager", "Mechanical Technician"],
            "Chief Engineer": ["Senior Software Architect", "Lead Project Manager", "Head of Mechanical Engineering"]
        }
        return random.choice(profession_variations[position])

    def add_colonist(self):
        surname = self.fake.last_name()
        name = self.fake.first_name()
        age = int(random.uniform(5, 60))
        position = self.generate_position()
        colonist = {
            "surname": surname,
            "name": name,
            "age": age,
            "position": position if age > 21 else 'child',
            "speciality": self.generate_profession(position) if age > 21 else None,
            "address": f"{random.choice(['module_1', 'module_2'])}",
            "email": f"{surname}_{name}@mars.org",
            "hashed_password": 'some_pass123',
            "created_date": datetime.now()
        }
        self.crew_members.append(colonist)

    def generate_all_colonists(self, count=5):
        for _ in range(count):
            self.add_colonist()
