import pandas as pd

df_big = pd.DataFrame([])

df = ['a','b','c']

df = pd.DataFrame(df)

df_big.append(df)
# df_big = pd.concat([df_big,df])

print(df_big)
print("Shape of df_big: " + str(df_big.shape))