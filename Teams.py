
import pandas as pd

teams = pd.read_csv('teams.csv',sep=',')


teams.head(16)


#1  Who was a winner?

teams.Team.loc[(teams.Goals == teams.Goals.max())]


#2 How many red cards there were and which team got it?


teams['Red Cards'].sum()


teams[teams['Red Cards'] == 1].Team


#3 Which teams have shooting accurancy more than 50 % and saves-to-shots ratio are more than 80%?

teams[(teams['Shooting Accuracy'] > '50%') & (teams['Saves-to-shots ratio'] > '80%')]


