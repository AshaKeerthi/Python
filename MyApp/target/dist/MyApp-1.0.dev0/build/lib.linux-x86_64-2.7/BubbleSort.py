import string

class BubbleSort(object):
    number_of_element = 0
    
    def get_number_of_input(self):
        
        try :
            self.number_of_element = int(raw_input("Insert the number of Element"))
        except ValueError:
            print "Please Enter Int Value"
        self.get_number_to_sort(self.number_of_element)

    def get_number_to_sort(self, number_of_element):
        self.to_sort_element = []
        self.to_remove_element = []
        for number in range(int(self.number_of_element)):
            element = raw_input("Insert %d Element" % int(number+1))
            while len(str(element)) == 0 :                                # pragma: no cover
                element = raw_input("Insert %d Element" % int(number+1))
            try :
                element = float(element)
                self.to_sort_element.append(float(element))
            except ValueError:
                self.to_remove_element.append(element)  
        self.to_proceed_sorting(self.to_remove_element, self.to_sort_element)
    
    def to_proceed_sorting(self, to_remove_element, to_sort_element):
        if len(self.to_remove_element) > 0 and len(self.to_sort_element) > 0:
            proceed = raw_input("For proceed press y")
            if proceed.lower() == 'y':
                self.bubble_sort(self.to_sort_element)
                print "Removed Elements :" + str(self.to_remove_element)
            else:
                print "Try Again, You Cancel the sorting"
        elif len(self.to_sort_element) > 0:
            self.bubble_sort(self.to_sort_element)
        else:
            print "No Elements To Sort"

    def bubble_sort(self,to_sort_element):
        for i in range(len(self.to_sort_element)):
            for j in range(len(self.to_sort_element)):
                if self.to_sort_element[i] < self.to_sort_element[j]:
                    temp = self.to_sort_element[i]
                    self.to_sort_element[i] = self.to_sort_element[j]
                    self.to_sort_element[j] = temp
                    print self.to_sort_element
        print "Fully Sorted :" + str(self.to_sort_element)   
           
if __name__ == "__main__":        # pragma: no cover
    to_sort = BubbleSort()        # pragma: no cover
    to_sort.get_number_of_input() # pragma: no cover
