# いまにゅ   Udemy streamlit超入門
#    2022.10.10    10.13

import streamlit as st
import numpy  as np
import pandas as pd

st.title('Streamlit 超入門')

"""
# Udemy Streamlit超入門


```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write('DataFrame')

dfa = pd.DataFrame({
    '1列目': [ 1,   2,  3,  4],
    '2列目': [ 10, 20, 30, 40]  
})

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a', 'b','c']
)


st.write(df)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#st.datafreme  は width,heightを支持できる
#st.dataframe(df ,width=400,height=200)

#st.write('highlight')
#st.dataframe(df.style.highlight_max(axis=0))

