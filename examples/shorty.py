import pandas as pd
df = pd.read_csv("legislators-current.csv")
newDf = df[[ "state", "first_name", "last_name", "phone" ]]
newDf.to_csv("fancypants.csv")
