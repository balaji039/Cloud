class matrixcomputation:
    def matcom(self):
        arr = []
        inp = open ("dataset.txt","r")

        for line in inp.readlines():

            arr.append([])

            for i in line.split():
                arr[-1].append(int(i))
        return arr

    def cloud2(self):
        #arr = []
        arr2=[]
        inp1 = open ("dataset2.txt","r")

        for line in inp1.readlines():

            arr2.append([])

            for i in line.split():
                arr2[-1].append(int(i))
        return arr2

    def cloud3(self):
        #arr = []
        arr3=[]
        inp2 = open ("dataset3.txt","r")

        for line in inp2.readlines():

            arr3.append([])

            for i in line.split():
                arr3[-1].append(int(i))
        return arr3