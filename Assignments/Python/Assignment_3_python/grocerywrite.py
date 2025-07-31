records = [
{'name':"rice","price":120,"category":"grocery"},
{'name':"sugar","price":220,"category":"grocery"},
{'name':"wheat","price":320,"category":"grocery"},
{'name':"rcereal","price":420,"category":"grocery"},
]
with open("grocery.txt", "w") as f:
    f.write("ID\t\tNAME\t\tPrice\t\tCategory\n")
    for i in range(len(records)):
        data = records[i]
        f.write(f"{i+1}\t\t{data['name']}\t\t{data['price']}\t\t{data['category']}\n")
