import pandas as pd
import matplotlib.pyplot as plt

class dataC:
    def __init__(self, path, sheet) -> None:
        self.file = pd.read_excel(path, sheet_name=sheet, usecols="B,C")
        self.datas = pd.DataFrame(self.file, columns=['Periodo', 'Vendas']);
        self.readed = True
    
    def printout(self):
        if self.readed:
            print(self.file)
        else:
            print("Não há dados")
    def plot(self):
        if self.readed:
            self.datas.plot(x ='Periodo', y='Vendas', kind = 'line')	
            plt.show()
        else:
            print("Não há Dataframe disponível, use DataC() para isntancia um novo conjunto de dados")

class Calc:
    def __init__(self) -> None:
        pass
    def linearRegression(self):
        averangeX= self.datas['Periodo'].mean()
        averangeY= self.datas['Vendas'].mean()
        for Venda in self.datas['Vendas']:
            A2 += Venda - averangeY
        for Periodo in self.datas['Periodo']:
            A1 += Periodo - averangeX
        for Periodo in self.datas['Periodo']:
            A3 += (Periodo - averangeX)^(2)

print("Prompt Version")
dataObj = dataC('/home/caio/Área de Trabalho/Piloto.xlsm','Planilha1')
dataObj.printout()
dataObj.plot()