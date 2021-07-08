import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
config = {
    "font.family":'Arial',
    "font.size": 16,
    "mathtext.fontset":'stix',
    "font.serif": ['SimSun'],
}
rcParams.update(config)
def restruc(kk):
    Ag =[]
    Bg =[]
    Au =[]
    Bu =[]
    for i in range(len(kk[0])):
        if kk[1][i] == 1:
            Ag.append(kk[0][i])
        elif kk[1][i] == 2:
            Bg.append(kk[0][i])
        elif kk[1][i] == 3:
            Au.append(kk[0][i])
        elif kk[1][i] == 4:
            Bu.append(kk[0][i])
    kkmodes = [Ag, Bg, Au, Bu]
    return kkmodes

data = np.loadtxt("modes.txt")


fe = data.T[0:2]
femodes = restruc(fe)
cr = data.T[2:4]
crmodes = restruc(cr)
#print(fe)
colors1 = ['C{}'.format(i) for i in range(4)]
#print(colors1)

lineoffsets1 = [3, 1, -1, -3]
linelengths1 = [1, 1, 1, 1]
labels = ['Ag', 'Bg', 'Au', 'Bu']
plt.eventplot(femodes, colors=colors1, lineoffsets=lineoffsets1,
                    linelengths=linelengths1, linewidths=2, label=colors1)

plt.ylim([-4.3, 4.3])
plt.yticks([])
plt.xlim([-0.1, 28])
plt.ylabel('vibration Modes',)
plt.xlabel("Frequence(THz)")

for i in range(4):
    plt.annotate(labels[i],   xy=(25, lineoffsets1[i]-0.2), fontsize=16 , color=colors1[i])

plt.show()