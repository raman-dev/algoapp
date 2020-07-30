import math
from functools import reduce


class Element:
    #class variables
    LEFT = -1
    RIGHT = 1

    def __init__(self,value):
        self.value = value
        #default direction of all elements is left
        self.direction = self.LEFT


def findLargestMobileElement(elements: [],length):
    largestMobile = None
    largestMobileIndex = -1
    i = 0
    while i < length:
        element = elements[i]#current element
        #largest mobile element is defined as the largest element
        #that points to another element that is less than this one
        direction = element.direction
        if direction == Element.LEFT and i > 0:
            #if the direction is left and we arent the first element in the list
            if elements[i - 1].value < element.value:
                if largestMobile == None or largestMobile.value < element.value:
                    largestMobile = element
                    largestMobileIndex = i
        elif direction == Element.RIGHT and i < length - 1:
            #print("length =>"+str(length))
            #print("i => "+str(i))
            if elements[i + 1].value < element.value:
                if largestMobile == None or largestMobile.value < element.value:
                    largestMobile = element
                    largestMobileIndex = i
        i+=1

    return largestMobileIndex

def elementToString(elements,input_string):
    result = ""
    for element in elements:
        result+=input_string[element.value]
    return result

#takes a string input returns a list of permutations
#convert to index comparison
def gen_permutations(input_string: str) -> []:
    result = []
    elements = [Element(val) for val in list(range(0,len(input_string)))]
    length = len(elements)
    hasMobileElements = True
    #convert this list of elements to json
    #so an array of objects that have a character and direction
    result.append(elementToString(elements,input_string))
    largestMobileIndex = findLargestMobileElement(elements,length)
    while largestMobileIndex != -1:
        #check if there is atleast one mobile element in the list elements
        #swap current element with the element it points to
        largestMobile =  elements[largestMobileIndex]
        #if direction is right then largestMobileIndex + 1 if direction is left the largestMobileIndex  - 1
        swapIndex = largestMobileIndex + largestMobile.direction
        swapElement = elements[swapIndex]
        elements[largestMobileIndex] = swapElement
        elements[swapIndex] = largestMobile
        #reverse direction of all elements larger than largestMobile
        for element in elements:
            if element.value > largestMobile.value:
                element.direction = element.direction * -1
        
        result.append(elementToString(elements,input_string))
        #check if there are mobile elements
        largestMobileIndex = findLargestMobileElement(elements,length)
        
    return result

#can i come up with an algorithm to get an n-combination
"""test_string = "aamnr"
print("result_expected_size => "+str(math.factorial(len(test_string))))
result = gen_permutations(test_string)
print("result_size => "+str(len(result)))
print(result)"""