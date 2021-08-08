from faker import Faker
import random

fake = Faker('ko_KR')
fake.seed_instance(4321)
print(fake.name())
fake2 = Faker('ko_KR')
print(fake2.name())