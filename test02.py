##  書籍 : PythonとStramlitでデータ分析をWebアプリ化
##         データサイエンティストのためのWebアプリ入門

#streanlit   Anaconda =streamlit=  
#.     streamlit terminal 起動し. % streamlit run test02.py  を実行

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#st.write('Streamlit 面白い')

st.title('test02.py  by Streamlit')


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



df = pd.DataFrame()
#各列に x と y の値を格納していく
df['x'] = np.arange(0,10)
df['y'] = np.power( np.arange(0,10),2 )

st.write('DataFrame')
st.dataframe(df)

#dataを可視化
#st.line_chart(data=df)

#sizeを指定して可視化
st.write('line_chart')
st.line_chart(data=df , width=150 , height=350 )


#折線を塗りで可視化
st.write('area_chart')
st.area_chart(data=df , width=150 , height=350 )


#棒グラフで可視化
st.write('bar_chart')
st.bar_chart(data=df , width=150 , height=350 )




##------------------------------
### matplotlib.pyplot  散布図
##------------------------------

# グラフのオブジェクト作成

fig,ax = plt.subplots(figsize=(5,3))

#散布図を作成
ax.scatter(x=df['x'],y=df['y'])

plt.xlabel('x')
plt.ylabel('y')

st.pyplot(fig)