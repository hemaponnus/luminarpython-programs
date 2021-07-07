# 7/4/21--26

class Pycharm:
    def open(self):
        print("open method in pycharm")
    def run(self):
        print("run method in pycharm")
    def debug(self):
        print("debug method in pycharm")
class Vscode:
    def open(self):
        print("open method in Vscode ")
    def run(self):
        print("run method in  Vscode")
    def debug(self):
        print("debug method in  Vscode")


class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
py=Pycharm()
vs=Vscode()
prg=Programmer()
prg.coding(vs)
                                            # o/p
                                #open method in  Vscode
                                #run method in   Vscode
                                #debug method in Vscode