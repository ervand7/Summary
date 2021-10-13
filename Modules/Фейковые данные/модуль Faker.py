# прекрасная документация: https://faker.readthedocs.io/en/master/
# pip install Faker

from faker import Faker

fake = Faker('ru_RU')

print(fake.name())
print(fake.address())
print(fake.text())
for _ in range(10):
    print(fake.name())
