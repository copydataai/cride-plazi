

# Python
from csv import DictReader

# models
from cride.circles.models.circles import Circle

def insert_circles_to_csv(path: str):
    with open(path, 'r') as csv_file:
        circles = [Circle(**attrs) for attrs in DictReader(csv_file)]
        Circle.objects.bulk_create(circles)
        for circle in circles:
            print(f'Circle saved success: {circle}')


def run():
    default_path = './circles.csv'
    insert_circles_to_csv(default_path)
