import numpy as np
phrase = (input("phrase"))
liste=np.array([])
while phrase=='int' :
    phrase = str(input("phrase"))
for lettre in phrase:
    liste=np.append(liste,lettre)
print(liste)
