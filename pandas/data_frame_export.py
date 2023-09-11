import pandas as pd
from pandas import DataFrame

ser = pd.Series(["how are you?", "It is great!"])
df = DataFrame(data=ser, columns=["text"])
print(df)
# feather need pyarrow
df.to_feather('./text.feather')

