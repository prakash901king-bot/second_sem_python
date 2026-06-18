people = {'John': 25, 'Emma': 15, 'Lucas': 8, 'Sophia': 42} 
def classify_age(age):
    if age<13:
        return "child"
    elif 13>=age>=19:
        return "teen"
    else:
        return "adult"
    
age_add={key: str(classify_age(value)) for (key,value) in people.items()}
print(age_add)