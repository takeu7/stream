# いまにゅ   Udemy streamlit超入門
#    2022.10.15   14:13

import streamlit as st
import numpy  as np
import pandas as pd
from   PIL import Image

st.title('Streamlit 超入門 ')

"""
# Udemy Streamlit

## 
## st.image(img)

```python
import streamlit as st
import numpy  as np
import pandas as pd
from   PIL import Image
```
"""

st.write('Interactive Widgets')

if st.checkbox('Show Image'):
    img = Image.open('img/obaba.jpg')
    st.image(img , caption='オババ',use_column_width=True)


option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1,11))
)
'あなたの好きな数字は',option,'です'


### --------------------------------
### sidebar
text = st.sidebar.text_input('あなたの趣味を教えて下さい')
condition = st.sidebar.slider('あなたの今の気分は?',0,10,5)
### --------------------------------/////

'あなたの趣味は',text,'です'
'コンディション:',condition
#---------------------------------- with sidebar


