""" You have a list of integers, and for each index you want to find the product
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a
list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution! """

# Start coding from here


from functools import reduce


def get_products_of_all_ints_except_at_index(alist):
    listOfProducts = list()
    for i in range(len(alist)):
        calc = 1
        for j in range(len(alist)):

            if i != j:
                calc = calc*alist[j]
        listOfProducts.append(calc)

    return listOfProducts


# print('by calcluating ..',
#       get_products_of_all_ints_except_at_index([1, 7, 3, 4]))


# The above solution is taking O(n²) TIME COMPLEXITY.
# A much better solution would be to calc the product of the whole array at once and divide with the element at that particular index
# soo..


def get_products_of_all_ints_except_at_index2(alist):
    listofproducts = [1]*len(alist)
    store = reduce((lambda x, y: x*y), alist)
    print(store)
    for i in range(len(alist)):
        listofproducts[i] = store//alist[i]
    return listofproducts


print(get_products_of_all_ints_except_at_index2([1, 7, 3, 4]))
