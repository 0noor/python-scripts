class SuperList(list):
    def __len__(self):
        return 1000


suplist = SuperList()
print(suplist.__len__())
suplist.append(5)
print(suplist)
