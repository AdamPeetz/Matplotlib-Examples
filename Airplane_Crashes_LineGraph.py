# import required libraries
import pandas as pd
import matplotlib.pylab as plt

#import dataset
crash_df = pd.read_csv('C:\\Users\\adamg\\Documents\\MSDS_670_Viz\\Week_5\\Airplane_Crashes.csv', sep=',')

# split date value to allow for charting by year
crash_df[['Month', 'Day', 'Year']] = crash_df['Date'].str.split('/', expand=True)

#group by year and count
countgraph = crash_df.groupby('Year').count()

#orient data for charting
countgraph2 = countgraph['Date']

#Generate crashes line chart

#create figure, adjust size to golden dimensions
fig1, ax1 = plt.subplots(figsize=(10,5))

#Change dimensions of graph to fit title
for a in fig1.axes:
    box = a.get_position()
    a.set_position([box.x0, box.y0, box.width * 1, box.height * 0.9])

#set figure title
fig1.text(s='Airplane Crashes', x=0.11, y=0.96, fontsize=24, ha='left', va='center')
fig1.text(s='How have airplane', x=0.11, y=0.90, fontsize=18, ha='left', va='center')
fig1.text(s='crashes', x=0.35, y=0.90, fontsize=18, ha='left', va='center', color='firebrick',fontweight='bold')
fig1.text(s='trended over time?', x=0.465, y=0.90, fontsize=18, ha='left', va='center')


#create line graph
ax1.plot(countgraph2, color='firebrick')

#annotate line at termination
ax1.annotate('Crashes',xy=(105,5),color='firebrick', fontweight='bold', annotation_clip=False)

#remove spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.spines['left'].set_visible(False)

#edit tick marks, and axis
ax1.set_xticks(ax1.get_xticks()[::18])
ax1.set_yticks(ax1.get_yticks()[1:6:4])
ax1.tick_params(axis='both', which='both', length=0)

#story #1, Expansion of industry
ax1.annotate('Crashes steadliy increased',xy=(0,60))
ax1.annotate('with the expansion of',xy=(0,55))
ax1.annotate('the airline industry.',xy=(0,50))

#story #2, Max Crashes
ax1.annotate('A record 88 crashes occured in 1946.',xy=(35,90),ha='center')

#story #3, modern downward trend
ax1.annotate('Airplane safety is improving,',xy=(65,25))
ax1.annotate('crashes have trended down',xy=(65,20))
ax1.annotate('since the 90s.',xy=(65,15))

#export figure to .jpg
fig1.savefig('trends_linegraph.jpg', dpi=300) 