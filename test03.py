##  書籍 : PythonとStramlitでデータ分析をWebアプリ化
##         データサイエンティストのためのWebアプリ入門


#streanlit   Anaconda =streamlit=  
#.     streamlit terminal 起動し. % streamlit run test02.py  を実行

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.write('Streamlit 面白い')


if st.checkbox('チェックを入れて下さい'):
    st.write('チェックが入りました')



# ----------------------------------    
#選択肢
st.write('')
st.write('1個を選択')
select_list = [ 'Apple', 'Orange', 'Grape' ]
ret = st.selectbox( ' 果物を選んでください' , select_list )

#選択した結果
st.write(ret)

st.write( type(ret) )



# ----------------------------------    
#複数選択肢
st.write('')
st.write('複数を選択')
select_list = [ 'Apple', 'Orange', 'Grape', 'Peach' ]
ret = st.multiselect( ' 果物を選んでください' , select_list )

#選択した結果
st.write(ret)

st.write( type(ret) )






# ----------------------------------    P37   
"""


# 
## 書籍 P37 / 113  
### st.colums(2)
```python

    書籍では st.beta_columns(2)だが  2021-11-02から推奨から外れたっぽい
    left_column,right_column = st.beta_columns(2)

    Please replace st.beta_columns with st.columns.
    st.beta_columns will be removed after 2021-11-02.


```
"""

st.write('通常column-----------------------------------')
left_column,right_column = st.columns(2)

# -- left column
if left_column.checkbox('左列にチェックを入れて下さい'):
    left_column.write('  左列の画面にチェックが入りました')

# -- left column
if right_column.checkbox('右列にチェックを入れて下さい'):
    right_column.write('  右列の画面にチェックが入りました')


left_column.write('left column')

right_column.write('right column')


st.write('通常column-----------------------------------')

## 書籍P37  end /////////




# ----------------------------------    P38
#ラジオボタン
st.write('')
st.write('ラジオボタン')
select_list = [ 'Apple', 'Orange', 'Grape', 'Peach' ]
ret = st.radio( ' 果物を選んでください' , select_list )

#選択した結果
st.write('選択した果物は、',ret)

st.write( type(ret) )



# ----------------------------------    P38
#数値入力
st.write('')
st.write('数値入力')

ret = st.number_input(' ここに数字入力' , min_value=0,max_value=10,step=1 )

#選択した結果
st.write('入力した数字は',ret)

st.write( type(ret) )



# ----------------------------------    P38 from いまにゅ
#数値入力
st.write('')
st.write('数値入力')

option = st.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(0,100,5))
)
'あなたの好きな数字は',option,'です'


st.write( type(option) )




# ----------------------------------    P39 Sidebar
#数値入力
st.write('')
st.write('数値入力 [SideBar]')

ret = st.sidebar.number_input(
    'あなたが好きな数字を教えて下さい',
    min_value=0 ,
    max_value=10,
    step=1
)
'あなたの好きな数字は',ret,'です'


st.write( type(ret) )
