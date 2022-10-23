class PrepareExcelData:
    def __init__(self, data):
        self.data = data
    
    def __str__(self):
         return self.data

    def prepare(self):
        print("OILA")
        print(self.data)
        return self.data
