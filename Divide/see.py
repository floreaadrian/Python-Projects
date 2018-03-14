from fis import clasaparental

class fisier(clasaparental):
    def __init__(self,fileName="hei.txt"):
        clasaparental.__init__(self)
        self._fileName = fileName
        self._loadFile()

    def add(self,obj):
        clasaparental.add(self,obj)
        self._storeFile()

    def _storeFile(self):
        f = open(self._fileName,"w")
        obj = clasaparental.getAll(self)
        for k in obj:
            f.write(k+"\n")
        f.close()

    def _loadFile(self):
        try:
            f = open(self._fileName,"r")
            line = f.readline().strip()
            while line!="":
                atrs = line.split("\n")
                clasaparental.add(self,atrs[0])
                line = f.readline()
        except IOError:
            print("Can't open")
        finally:
            f.close()

a = fisier()
a.add("Hei")
print(a.getAll())
