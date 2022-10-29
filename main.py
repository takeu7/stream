# いまにゅ   Udemy streamlit超入門
#    2022.10.10

import streamlit as st
import numpy as np
import pandas as pd



st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [ 1, 2, 3, 4],
    '2列目': [ 10, 20, 30, 40]
    
})

#st.write(df)

# st.datafreme  は width,heightを支持できる
st.dataframe(df ,width=400,height=200)

st.write('highlight')
st.dataframe(df.style.highlight_max(axis=0))

st.write('st.table')
st.table(df.style.highlight_max(axis=0))


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```

"""



'''
# 章2
## 節2
### 項2

```python

import numpy as np
import pandas as pd

```

'''