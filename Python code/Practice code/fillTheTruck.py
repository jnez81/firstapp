# Function that outputs an integer representing the maximum units that can be 
# carried by the delivery truck. 
#
# INPUT:
# The input to the function method consists of five arguments:
# num, an integer representing number of products;
# boxes, a list of integers representing the number of available boxes for products;
# unitSize, an integer representing size of unitsPerBox;
# unitsPerBox, a list of integers representing the number of units packed in each box;
# truckSize, an integer representing the number of boxes the truck can carry.
# OUTPUT: 
# Return an integer representing the maximum units that can be carried by the truck.

def fill_the_truck(num, boxes, unitSize, unitsPerBox, truckSize):
    num = 3
    boxes = [1, 2, 3]
    unitSize = 3 
    unitsPerBox = [3, 2, 1]
    truckSize = 3 

    if num < 1 or len(boxes) < 1 or unitSize < 1 or len(unitsPerBox) < 1 or truckSize < 1:
            return 0

    heap = []
    for i in range(num):
        box = boxes[i]
        while box > 0:
            heap.heappush(heap, -1 * unitsPerBox[i])
            box -= 1
    res = 0
    while truckSize > 0:
        if len(heap) > 0:
            res += -1 * heap.heappop(heap)
        truckSize -= 1
    return res

fill_the_truck(3, [1,2,3], 3, [3,2,1], 3)