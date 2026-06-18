inventory={"screws":150,"bolts":8,"washers":0,"nuts":45}
re_inventory={key: ("reorder" if value < 10 else "in stock")  for (key,value) in inventory.items()}
print(re_inventory)