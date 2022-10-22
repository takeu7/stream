##  書籍 : PythonとStramlitでデータ分析をWebアプリ化
##         データサイエンティストのためのWebアプリ入門



import streamlit as st
import pandas as pd


st.title('これはテストです')
st.write('テスト')


df = pd.DataFrame(
    [[0,1,2],[3,4,5],[6,7,8]],
    columns=['1列目','2列目','3列目']
)


#st.table(df)
st.dataframe(df)


st.latex(
r'''
S =\sum^{N}_{i=0}a_{n}
'''
)