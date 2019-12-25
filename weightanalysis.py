import matplotlib.pyplot as plt

names = ['mon', 'tue', 'wed', 'thur', 'fri']
values = [152, 151, 154, 153, 151]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.ylabel('Weight in LBS')
plt.suptitle('My 5 Day Weight management test.')
plt.tick_params(axis='x', which='major', labelsize=7)
plt.show()
