from faker import providers
from faker import Faker
for _ in range(5):
    print('姓名：', Faker.name())