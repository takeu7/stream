# いまにゅ   Udemy streamlit超入門
#    2022.10.15   14:13

import streamlit as st
import numpy  as np
import pandas as pd

st.title('Streamlit 超入門 map.py')

"""
# Udemy Streamlit
## 座標情報 st.map(df)


```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""



df0 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns= ['lat','lon']
)


df1 = pd.DataFrame(
    np.random.rand(400,2)/[25,25] + [35.69,139.70],
    columns= ['lat','lon']
)


df = df0

st.map(df)


st.write('DataFrame')
st.write(df)
