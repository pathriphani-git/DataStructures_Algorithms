def bubble_sort(elements,key):

    size = len(elements)
    swapped = False
    for i in range(size-1):
        for j in range(size-1-i):
            if elements[j][key] > elements[j+1][key]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break



if __name__ == '__main__':
    elements = [
        {'name':'mona', 'transaction_amount':1000,'device':'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'pixel'},
        {'name': 'amir', 'transaction_amount': 800, 'device': 'samsung'}
    ]
#    numberList = [5,9,2,1,67,34,88,34]

    bubble_sort(elements,key='name')
    print(elements)