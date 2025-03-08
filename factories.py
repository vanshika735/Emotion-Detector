from faker import Faker

fake = Faker()

def fake_product():
    return {
        "name": fake.word(),
        "category": fake.word(),
        "price": round(fake.random_number(digits=3), 2),
        "description": fake.sentence(),
    }

# Print output to see it in the terminal
print(fake_product())
