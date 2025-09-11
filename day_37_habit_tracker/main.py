import os
import dotenv
import requests
from datetime import datetime


dotenv.load_dotenv()

TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
# The USERNAME variable is not suitable for use with environment variables because such a variable already exists in
# the Windows system (the login of the current user in the system), and load_dotenv() does not overwrite existing variables by default.
# Therefore, os.getenv("USERNAME") takes the system variable USERNAME from Windows, and not from the .env project.
#
# SOLUTION: you can allow load_dotenv() to overwrite load_dotenv(override=True),
# but it is better to use unique variable names (add a prefix of the application or project name)

GRAPH_ID = "lessons"

pixela_endpoint = "https://pixe.la/v1/users"


# POST: CREATE A USER
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)


# POST: CREATE A GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id": GRAPH_ID,
    "name": "Passed the Lessons",
    "unit": "quantity",
    "type": "int",
    "color": "shibafu",
}
# Colors: shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black)

headers = {
    "X-USER-TOKEN": TOKEN.encode("utf-8"),
}

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)


# POST: A PIXEL
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()  # or datetime(year=2000, month=2, day=20)
# print(today.strftime("%Y%m%d"))

post_pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many lessons did you learn today? \n- ")
}

response = requests.post(url=pixel_creation_endpoint, json=post_pixel_parameters, headers=headers)
print(response.text)


# PUT: UPDATE A PIXEL
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

update_parameters = {
    "quantity": "1"
}

# response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
# print(response.text)


# DELETE: A PIXEL
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

