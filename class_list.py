
#create a class called circle
class Circle():
    
    # define constructor that takes in list1 as the argument
    def __init__(self, list1):
        self.list1 = list1
        

    #define pi to return its value
    def __pi(self):
        return 3.141

    # calculate_area by iteriating each value in list 1 using the formula pi*r*r
    # create a new list and append the area values to the list
    def calculate_area(self, *list1):
        self.list_area = []        
        for radius in list1:
            area = self.__pi()* radius* radius
            self.list_area.append(area)
            return self.list_area
        
    # calculate perimeter by iteriating each value in list 1 using the formula 2*pi*r
    # create a new list and append the perimeter values to the list
    def calculate_perimeter(self, *list1):
        self.list_perimeter =[]
        for radius in list1:
            perimeter = 2 * self.__pi * radius
            self.list_perimeter.append(perimeter)
            return self.list_perimeter
   
    #define a display output fuction to print the lists
    def display_output(self):
        print(f"The area of the given list: {self.list_area}")
        print(f"The perimeter of thr given list : {self.list_perimeter}")

#create an obj for class and print the output
list1 = [10, 501, 22, 37, 100, 999, 87, 351]
cir = Circle(list1)
cir.display_output()