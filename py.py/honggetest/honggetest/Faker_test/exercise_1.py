from faker import Faker#导入faker库

faker = Faker('zh_CN')#定义变量
for _ in range(3):
    print('name:', faker.name())
    print('address:', faker.address())
    print('text:', faker.text())
