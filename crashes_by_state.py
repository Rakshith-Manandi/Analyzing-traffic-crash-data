import pandas as pd
import numpy as np
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style = 'white', color_codes = True)

import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode()

def readFile(x):
	output = pd.read_csv(x)
	return output


def by_state(x):


	states = x.groupby('STATE')
	count_by_state = np.asarray(states.YEAR.count())
	fatals_by_state = np.asarray(states.FATALS.sum())

	stcodes = np.asarray(['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', \
	                     'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', \
	                     'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', \
	                     'VA', 'WA', 'WV', 'WI', 'WY'])

	stpopulation = np.asarray([4858979, 738432, 6828065, 2978204, 39144818, 5456574, 3590886, 945934, 646449, 20271272, 10214860, 1431603, 1654930, 12859995, 6619680, \
	                           3123899, 2911641, 4425092, 4670724, 1329328, 6006401, 6794422, 9922576, 5489594, 2992333, 6083672, 1032949, 1896190, 2890845, \
	                           1330608, 8958013, 2085109, 19795791, 10042802, 756927, 11613423, 3911338, 4028977, 12802503, 1056298, 4896146, 858469, 6600299, \
	                           27469114, 2995919, 626042, 8382993, 7170351, 1844128, 5771337, 586107])

	stpop_density = np.asarray([37, 0.5, 23.2, 22.1, 97, 20.3, 286.3, 187.4, 4088.4, 145.9, 68.6, 86.1, 7.7, 89.4, 71.4, \
	                          21.6, 13.7, 43.2, 41.7, 16.6, 238.9, 336.3, 67.8, 26.6, 24.6, 34.2, 2.7, 9.5, 10.2, \
	                          57.4, 467.2, 6.6, 162.2, 79.8, 4.2, 109.7, 22, 16.2, 110.5, 394.4, 62.9, 4.4, 61.8, \
	                          40.6, 14.1, 26.2, 82.0, 41.7, 29.6, 41.2, 2.3])

	stvehicles = np.asarray([1030, 960, 660, 700, 840, 340, 860, 950, 350, 710, 820, 760, 790, 750, 610, 1050, 830, 840, \
	                        910, 780, 790, 820, 870, 870, 680, 830, 1120, 1000, 500, 830, 690, 770, 570, 670, 1080, \
	                        910, 860, 770, 760, 730, 770, 950, 840, 720, 870, 910, 840, 870, 750, 860, 1140])

	sturban = np.asarray([59.0, 66.0, 89.8, 56.2, 95.2, 86.2, 88.0, 83.3, 100.0, 91.2, 75.1, 91.9, 70.6, 88.5, 72.4, 64.0, 74.2, \
	                      58.4, 73.2, 38.7, 87.2, 92.0, 74.6, 73.3, 49.3, 70.4, 55.9, 73.1, 94.2, 60.3, 94.7, 77.4, 87.9, 66.1, \
	                      59.9, 77.9, 66.2, 81.0, 78.7, 90.7, 66.3, 56.7, 66.4, 84.7, 90.6, 38.9, 75.5, 84.0, 48.7, 70.2, 64.8])

	# accidents per capita (10^5 )population
	acc_per_capita = count_by_state / stpopulation * 1e+5
	# accidents per population density
	acc_per_density = count_by_state / stpop_density
	# fatals per accidents
	fatals_per_acc = fatals_by_state / count_by_state

	return acc_per_capita, acc_per_density, fatals_per_acc