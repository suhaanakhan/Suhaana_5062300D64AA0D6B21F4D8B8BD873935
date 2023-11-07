#Function to perform Linear Search
def linear_search_product(product_list, target_product):
    indices = []
    for i in range(len(product_list)):
        if product_list[i] == target_product:
            indices.append(i)
    return indices

#List of products
products = products = ["Corn Flakes", "Cheetos", "Parle-G", "Bourbon", "Pringles", "Cheetos", "Bingo", "Parle-G"]

target1 = "Parle-G"
result1 = linear_search_product(products, target1)
print("The indexes of the occurrence of ", target1, ": ",result1)

target2 = "Lays"
result2 = linear_search_product(products, target2)
print("The indexes of the occurrence of ", target2, ": ",result2)

target3 = "Bourbon"
result3 = linear_search_product(products, target3)
print("The indexes of the occurrence of ", target3, ": ",result3)
