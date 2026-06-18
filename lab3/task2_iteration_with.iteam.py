price={"apple":1.00,"banana":0.50,"orange":0.75}
price_updated={key: (value*2) for (key,value) in price.items()}
print(price_updated)