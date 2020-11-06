import matplotlib
from matplotlib import pyplot as plt

print(matplotlib.get_cachedir())

matplotlib.font_manager._rebuild()


for i in matplotlib.font_manager.fontManager.ttflist:
  if 'Nanum' in i.name:
    print(i.name, i.fname)

        
plt.rcParams['font.family']="NanumGothic"

plt.plot(["애폴","삼송","엘쥐"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.show()

