# import required libraries
import pandas as pd
import matplotlib.pylab as plt

#import dataset
crash_df = pd.read_csv('C:\\Users\\adamg\\Documents\\MSDS_670_Viz\\Week_5\\Airplane_Crashes.csv', sep=',')

#group by operator, count, sort
operatorgraph = crash_df.groupby('Operator').count()
operatorgraph.sort_values(by='Date',inplace=True,ascending=False)

#reset index to extract operator names to column
operatorgraph.reset_index(inplace=True)

#Take only top 5 values from each, seperate into x and y axis variables
operator=operatorgraph['Operator'][:5]
operatorcrash=operatorgraph['Date'][:5]

#Generate operator barchart chart

#create figure, adjust size to golden dimensions
fig2, ax2 = plt.subplots(figsize=(10,5))

#Change dimensions of graph to fit title
for a in fig2.axes:
    box = a.get_position()
    a.set_position([box.x0, box.y0, box.width * 1, box.height * 1])

#set figure title
fig2.text(s='Airplane Operator Crashes', x=0.11, y=0.96, fontsize=24, ha='left', va='center')
fig2.text(s='Which operator has had the most airplane', x=0.11, y=0.9, fontsize=18, ha='left', va='center')
fig2.text(s='crashes', x=0.645, y=0.90, fontsize=18, ha='left', va='center', color='firebrick',fontweight='bold')
fig2.text(s='?', x=0.755, y=0.90, fontsize=18, ha='left', va='center')

#create bar graph
ax2.barh(operator,operatorcrash,color=['firebrick', 'indianred', 'dimgrey', 'darkgrey', 'lightgrey'])

#remove spines
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['left'].set_visible(False)

#remove x, y labels
ax2.axes.get_xaxis().set_ticks([])
ax2.axes.get_yaxis().set_ticks([])


#orient least to greatest
ax2.invert_yaxis()

#label bars with value
ax2.annotate('255',xy=(235,0.05),color='white',fontweight='bold',fontsize='14')
ax2.annotate('140',xy=(120,1.05),color='white',fontweight='bold',fontsize='14')
ax2.annotate('72',xy=(60,2.06),color='white',fontweight='bold',fontsize='14')
ax2.annotate('63',xy=(50,3.05),color='white',fontweight='bold',fontsize='14')
ax2.annotate('44',xy=(30,4.05),color='white',fontweight='bold',fontsize='14')

#label bars with Operator
ax2.annotate('Aeroflot',xy=(257,0.05),color='firebrick',fontweight='bold',fontsize='14')
ax2.annotate('U.S. Air Force',xy=(143,1.05),color='indianred',fontweight='bold',fontsize='14')
ax2.annotate('Air France',xy=(75,2.06),color='dimgrey',fontweight='bold',fontsize='14')
ax2.annotate('Lufthansa',xy=(65,3.05),color='darkgrey',fontweight='bold',fontsize='14')
ax2.annotate('United Air Lines',xy=(45,4.05),color='darkgrey',fontweight='bold',fontsize='14')

#exposition #1
ax2.annotate('Aeroflot, a Russian carrier, has had',xy=(200,1.50))
ax2.annotate('more crashes than any other',xy=(200,1.75))
ax2.annotate('operator.',xy=(200,2))

#exposition #2
ax2.annotate('Total crashes is loosely correlated',xy=(200,3))
ax2.annotate('to the age of the airline. Aeroflot,',xy=(200,3.25))
ax2.annotate('Air France, and United were all',xy=(200,3.5))
ax2.annotate("founded in the 1920's and 30s.",xy=(200,3.75))

#export figure to .jpg
fig2.savefig('operator_barcharts.jpg',dpi = 300) 