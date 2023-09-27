def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices


products = ["soap", "sampoo", "powder", "soap powder", "soap"]
target = "soap"
target2 = 'mango'
result = linearSearchProduct(products, target)
print(result)