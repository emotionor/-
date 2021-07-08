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
file = np.loadtxt("BaBiO_nd2.freq.gp")
#PBE_NBAND=88
kpath = file.T[0]
Energy = file.T[1]
hkpts= np.array([0.000, 0.540000, 1.000000, 1.707107])
########


plt.figure(figsize=(6, 5), dpi=180)
#plt.figure(figsize=(3.0, 4.0), dpi=360)
#plt.scatter(kpath, Energy, s=O *100, c="white", alpha=1, edgecolor="cornsilk")
#PBE
for i in range(15):
    plt.plot(kpath, file.T[i+1], c='blue',alpha=0.5, lw=1, label="PBE")

#plt.legend(loc='upper right')
#plt.ylabel('Energy [eV]',)  # fontsize='small',labelpad=5)

for i in hkpts:
    plt.axvline(x=i, ls=':', color='k', lw=0.5, alpha=0.5)
plt.axhline(y=0, ls=':', color='k', lw=0.5, alpha=0.5)
#plt.ylim(-3, 5)
plt.xlim(hkpts.min(), hkpts.max())
plt.xticks(hkpts, ('$\Gamma$', 'X', 'M', "$\Gamma$"))

#plt.show()
plt.savefig("phonon_dis_cry.png", bbox_inches = 'tight')


#'''