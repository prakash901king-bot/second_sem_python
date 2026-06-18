scores={"Alice":85,"Bob":62,"Charlie":90,"Diana":55}
uppercase_name={(key.upper()): value for (key,value) in scores.items()}
print(uppercase_name)