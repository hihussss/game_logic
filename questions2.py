class Fifo:
    def __init__(self):
        self.data = []
    
    def add_elem(self,value):
        self.data.append(value)
    
    def get_elem(self):
        if self.data:
            rezult = self.data.pop(0)
        else:
            rezult = None
        return rezult    
    def show_data(self):
         print(self.data)
         
         
class Fifo2:
    def __init__(self):
        self.data = []
    def add_elem(self,value):
        self.data.append(value)
    def pop_elem(self):
        return self.data.pop(0)
    def get_elem(self):
        return self.data[0]
    def size_data(self):
        return len(self.data) 
    def isEmpty_data(self):
        if self.data == []:
            msg = "Список пустой"
        else:
            msg = "Имеются данные "
        return msg    