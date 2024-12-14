def calculate_bmi(height, weight):
  try:
    bmi = weight/(height**2)
  except:
    bmi = 0
  return round(bmi,2)


def calculate_bmr(height, weight, age, gender):
  bmr = 0
  if (gender == 'F'):
    bmr = 447.593 + 9.247 * weight + 3.098 * height + 4.330 * age
  elif (gender == 'M'):
    bmr = 88.362 + 13.397 * weight + 4.799 * height + 5.677 * age
  return round(bmr,2)

calculate_bmr(175, 70, 30, 'M')
calculate_bmr(175, 70, 30, 'F')