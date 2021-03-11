# PyOpenFisheries
Access the http://www.openfisheries.org/ API from python. Work In Progress.


### example usage:
````
open_fish_conn = PyOpenFisheries()
skipjack_tuna = open_fish_conn.annual_landings(species="SKJ").filter_years(start_year=1970,end_year=1991)
print(skipjack_tuna.landings)
# [{'year': 1970, 'catch': 402166}...{'year': 1991, 'catch': 1575170}]
print(skipjack_tuna.summarize())
# Landings of SKJ globally from 1970 to 1991
````
