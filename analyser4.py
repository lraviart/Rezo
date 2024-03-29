import pandas as pd
import matplotlib.pyplot as plt
file = '/home/ulysse/Documents/Reseau/P1/all_web.csv'

df = pd.read_csv(file)

protocol_counts = df['Protocol'].value_counts().sort_values(ascending=False)
protocol_counts = protocol_counts[protocol_counts.index.isin(["DNS","TCP","UDP"])]
print(protocol_counts)

protocol_counts.plot(kind='bar')
plt.xlabel('Protocols')
plt.ylabel('Count (# of packets)')
plt.title('Transport Protocol Histogram')
plt.savefig('/home/ulysse/Documents/Reseau/P1/histo2.png')
plt.show()
