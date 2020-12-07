# Function to fill a truck with boxes and determine the maximum number 
# of units of any mix of products that can be shipped
# INPUT:
# Five arguments: num, integer representing number of products
# boxes, list of integers representing the number of available boxes
# unitSize, an integer representing size of unitsPerBox
# unitsPerBox, a list of integers representing the number of units packed in each box
# truckSize, an integer representing the number of boxes the truck can carry 
#
# OUTPUT:
# Return an integer representing the maximum units that can be carried by the truck 


class Solution:
    def fillTruck(self, num, boxes, unitSize, unitsPerBox, truckSize) -> int:
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