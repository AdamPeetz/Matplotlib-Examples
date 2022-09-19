# import required libraries
import pandas as pd
import matplotlib.pylab as plt

#import dataset
crash_df = pd.read_csv('C:\\Users\\adamg\\Documents\\MSDS_670_Viz\\Week_5\\Airplane_Crashes.csv', sep=',')

#group by operator, count, sort
fatalitiesgraph = crash_df.groupby('Operator').sum()
operatorgraph2 = crash_df.groupby('Operator').count()

#reset index to extract operator names to column
fatalitiesgraph.reset_index(inplace=True)
operatorgraph2.reset_index(inplace=True)

#extract meaningful values
operator2=operatorgraph2['Operator']
operatorcrash2=operatorgraph2['Date']
fatalities=fatalitiesgraph['Fatalities']

# intialize lists of data
data = {'operator':operator2,
        'fatalities':fatalities,
        'count':operatorcrash2,
       }
 
# Create DataFrame
fatalities_df = pd.DataFrame(data)

#extract values for 5 airlines in previous graph
scatterplot_df = fatalities_df.loc[fatalities_df['operator'].isin(['Aeroflot','Military - U.S. Air Force',\
                                                        'Air France','Deutsche Lufthansa','United Air Lines'])]

#sort values
scatterplot_df.sort_values(by='count',inplace=True,ascending=False)

#Generate fatalities and crashes scatterplot

#create figure, adjust size to golden dimensions
fig3, ax3 = plt.subplots(figsize=(10,5))

#Change dimensions of graph to fit title
for a in fig3.axes:
    box = a.get_position()
    a.set_position([box.x0, box.y0, box.width * 1, box.height * 0.9])

#set figure title
fig3.text(s='Airplane Crashes vs Fatalities', x=0.05, y=.95, fontsize=24, ha='left', va='center')
fig3.text(s='How do fatalities compare to', x=0.05, y=0.885, fontsize=18, ha='left', va='center')
fig3.text(s='crashes', x=0.416, y=0.885, fontsize=18, ha='left', va='center', color='firebrick',fontweight='bold')
fig3.text(s='for the 5 worst operators?', x=0.53, y=0.885, fontsize=18, ha='left', va='center')

#Generate Scatterplot
ax3.scatter(scatterplot_df['count'],scatterplot_df['fatalities'], color=['firebrick', 'indianred', 'dimgrey',\
                                                                         'darkgrey', 'lightgrey'])
    
#remove spines,
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.spines['left'].set_visible(False)

#change ticks
ax3.set_yticks([387,1019,1757,3356,8858])
ax3.set_xticks([44,63,72,140,255])

#set axis label
ax3.set_xlabel('Total Crashes',fontsize='15',labelpad=10)
ax3.set_ylabel('Total Fatalities',fontsize='15',labelpad=10)

#airline labels
ax3.annotate('Aeroflot',xy=(228,8700),color='firebrick',fontweight='bold',fontsize='12')
ax3.annotate('U.S. Air Force',xy=(143,3205),color='indianred',fontweight='bold',fontsize='12')
ax3.annotate('Air France',xy=(75,1650),color='dimgrey',fontweight='bold',fontsize='12')
ax3.annotate('Lufthansa',xy=(65,225),color='darkgrey',fontweight='bold',fontsize='12')
ax3.annotate('United Air Lines',xy=(47,888),color='darkgrey',fontweight='bold',fontsize='12')

#exposition #1
ax3.annotate('An increase in crashes generally aligns with',xy=(50,7500))
ax3.annotate('an increase in fatalities. The exception is',xy=(50,7000))
ax3.annotate('Lufthansa, who had more crashes but fewer',xy=(50,6500))
ax3.annotate("fatalities than United Air Lines.",xy=(50,6000))

#export figure to .jpg, set DPI
fig3.savefig('crashes_vs_fatalities_scatter.jpg',dpi = 300) 

