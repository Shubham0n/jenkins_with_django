import logging
import random
from faker import Faker
from employee.models import EmployProfile
from celery import shared_task

# logging
logger = logging.getLogger("django")

# Initialize Faker
fake = Faker()


def generate_random_employee():
    """
    Generate a random employee profile with fake data.
    """
    return {
        "role": random.choice(["developer", "manager", "designer"]),
        "name": fake.name(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "linkedin": fake.url(),
        "github": fake.url(),
        "objective": fake.sentence(),
        "address": fake.address(),
        "total_experience": round(random.uniform(1, 15), 1),
        "slug": fake.user_name(),
    }


@shared_task
def add_data_every_minute():
    """
    Generate and save a random employee profile.
    """
    data = generate_random_employee()

    # Create and save the employee profile
    employee = EmployProfile(**data)
    employee.save()

    logger.info(f"Employee profile created: {data}")
