import matplotlib.pyplot as plt
import numpy as np

def processdata(newdata):
    data=[]
    for i in range(len(newdata)):
        if i%2==0:
            a = newdata[i][::-1]
        else:
            a = newdata[i]
        data.append(a)
    return np.array(data)

######PBE
file = np.loadtxt("PBAND_PBAND_SUM_SOC_MZ.dat")
#PBE_NBAND=88
kpath = file.T[0]
Energy = file.T[1]
size = file.T[-1]
hkpts= np.array([0.000, 0.509, 1.019, 1.739])
########

######HSE
data = np.loadtxt("PBAND_PBAND_SUM_SOC_MZ.dat")
#HSE_NBANDS=84
tmpdata1 = data[6:].T[1:]#.flatten()
newdata = processdata(tmpdata1).flatten()
#newdata = [i for i in tmpdata if ]
#print(newdata[0])
kpath2 = np.array([kpath[0:180] for i in range(0, 84)])#.flatten()
kpath3 = processdata(kpath2).flatten()
#print(kpath2[3])
######

#'''

plt.figure(figsize=(3.0, 4.0), dpi=360)
#plt.scatter(kpath, Energy, s=O *100, c="white", alpha=1, edgecolor="cornsilk")
#PBE
#plt.scatter(kpath, Energy, c='blue', s=size, label="PBE")

plt.plot(kpath, Energy, c='peru',alpha=1, lw=1, label="PBE")
#plt.scatter(kpath, size, c= 'r')
#HSE
#plt.plot(kpath3, newdata, c='red',alpha=0.8, lw=1, label="HSE")

plt.legend(loc='upper right')
plt.ylabel('Energy [eV]',)  # fontsize='small',labelpad=5)

for i in hkpts:
    plt.axvline(x=i, ls=':', color='k', lw=0.5, alpha=0.5)
plt.axhline(y=0, ls=':', color='k', lw=0.5, alpha=0.5)
plt.ylim(-3, 5)
plt.xlim(hkpts.min(), hkpts.max())
plt.xticks(hkpts, ('G', 'X', 'M', 'G'))
#plt.show()
plt.savefig("test2.png", bbox_inches = 'tight')

#'''