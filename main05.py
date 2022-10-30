# いまにゅ   Udemy streamlit超入門
#    2022.10.30   14:56 

from turtle import right
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
### column
left_column , right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')

if button :
    right_column.write('ここは右カラム')
    

expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')

#text = st.text_input('あなたの趣味を教えて下さい')
#condition = st.slider('あなたの今の気分は?',0,10,5)
### --------------------------------/////
'''
'あなたの趣味は',text,'です'
'コンディション:',condition
'''
#---------------------------------- with sidebar

