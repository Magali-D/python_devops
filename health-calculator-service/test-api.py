import requests

bmi_url = "http://localhost:5000/bmi"
bmr_url = "http://localhost:5000/bmr"

height_bmi=1.75
height_bmr=175
weight=70
age=30
gender="F"
data_bmi = {"height" : height_bmi,"weight" : weight}
data_bmr = {"height" : height_bmr,"weight" : weight, "age": age, "gender": gender}
response_bmi = requests.post(bmi_url, json = data_bmi)
response_bmr = requests.post(bmr_url, json = data_bmr)

print(f"response_bmi = {response_bmi.text}")
print(f"response_bmr = {response_bmr.text}")