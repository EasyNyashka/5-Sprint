from faker import Faker

faker = Faker()


def generate_registration_data(self):
    name = faker.name()
    email = faker.email()
    password = faker.password(length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password