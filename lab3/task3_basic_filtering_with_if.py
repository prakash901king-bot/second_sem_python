scores={"Alice":85,"Bob":62,"Charlie":90,"Diana":55}
scores_up={key: value for (key,value) in scores.items() if value>70}
print(scores_up)