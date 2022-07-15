import random
from statistics import mean

import pandas as pd
#list für periods
perioden = []
#data
data = []
alpha = 0.3
#defined random values to calculate values for the periods
list_values = [1.5, 7.4, 8.1, 20.3, 10.2, 10, 3.45, 70.65, 15, 2, 9.4]
value = 501.5
for x in range(1, 116):

    if x % 12 == 0:
        value = 501.5
    value = value + random.choice(list_values)
    data.append(value)
    # value = 0

#24 perios (1period = 1month)
for x in range(1, 116):
    perioden.append(x)
#initialize dataframe
df = pd.DataFrame(data=[data], columns=perioden)

#debug prints
print(perioden)
print(data)
print(df)

exp_smoothed_data = []
for x in range(1, 116):
    if x == 115:
        value_1 = df[x]
        #NOTE hier bin ich mir nicht sicher wie ich es am besten mache einen NullPointer zugriff zu vermeiden. Wie wird das letzte Ergebnis berechnet wenn
        #immer das aus der nächten Periode genommen wird um den aktuellen wert zu berechnen?
        # value_2 = df[x]
        # exp_smoothed = 0.3 * value_1 + (1 - 0.3) * value_2
        exp_smoothed_data.append(df[x])
    else:
        value_1 = df[x+1].values.item() #not sure if there is a better way?
        value_2 = df[x].values.item()
        exp_smoothed = alpha * value_1 + (1-alpha) * value_2
        exp_smoothed = round(exp_smoothed, 3)
        print(type(exp_smoothed))
        exp_smoothed_data.append(exp_smoothed)
print(exp_smoothed_data)

#add row with exponential smoothed values
df.loc[-1] = exp_smoothed_data
df.index = df.index+1
print(df.head)
print(df.info)
print(df[1])

#fehler berechnen

calculatet_error = []

for x in range(1, 116):
    cal_err = df[x][1] - df[x][0]
    cal_err = round(cal_err, 3)
    print(cal_err)
    cal_err = abs(cal_err)
    calculatet_error.append(float(cal_err))

df.loc[-1] = calculatet_error
df.index = df.index+1

print(df)
#average error is
print("average error: " + str(mean(calculatet_error)))


#ses
#https://koalatea.io/python-ses-timeseries/
# from statsmodels.tsa.api import SimpleExpSmoothing
#
# ses = SimpleExpSmoothing(data)
#
# alpha = 0.2
# model = ses.fit(smoothing_level = alpha, optimized = False)

#Holt Wintersverfahren mit Parameteroptimierung (z.B. Grid)
#st = exp_smoothed_data
# from statsmodels import  holtwinters

alpha = float
beta = float
gamma = float

st = alpha
bt = []
ct = []

# print("first value in list st: "+str(st[1]))

#https://support.minitab.com/de-de/minitab/20/help-and-how-to/statistical-modeling/time-series/how-to/winters-method/methods-and-formulas/methods-and-formulas/
#erweitertes Prognoseverfahren

#ARIMA/SaARIMA

#ML Random Forest)

#Darstellen des Prognosefehlers (MAD, RMSE, MAPE)
# Verschiedene Zeitreihen teesten