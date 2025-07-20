''' '''
from abc import ABC,abstractmethod
class computer(ABC):
    @abstractmethod
    def process(self):
        pass
class laptop(computer):
    def process(self):
        print("its running")
class whiteboard(computer):
    def write(self):
        print("its writing")
class programmer:
    def work(self,com):
        print("solving bugs")
        com.process()
#com= computer()
#com.process()
com1=laptop()    
 
prog1=programmer()
w=whiteboard()
prog1.work(w)

 