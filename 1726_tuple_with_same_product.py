
nums = [2,3,4,6,8,12]

def tupleSameProduct(nums):
    # Create an empty dic to store the products of 2 num
    products = {}
    # Start a counter
    x=0
    counter=0

    # Iterate across the list
    for n1 in nums:
        x+=1
        for n2 in nums[x:]:
            product = n1 * n2
            if not products.get(product):
                products.update({product: 1})
            else:
                products[product]+=1

    # Count combinations
    for value in products.values():
        if value >= 2:
            counter += value * (value - 1) / 2   # Based on combinatory of 2 in x = x!/2!(x-2)! 
    return(counter * 8)

print(tupleSameProduct(nums))