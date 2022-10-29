# いまにゅ   Udemy streamlit超入門
#    2022.10.15   14:13

import streamlit as st
import numpy  as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門 dispimage.py')

"""
# Udemy Streamlit

## img = Image.open('img/obaba.jpg')
## st.image(img)


```python
import streamlit as st
import numpy  as np
import pandas as pd
from PIL import Image
```
"""

st.write('Display Image')

img = Image.open('img/obaba.jpg')

st.image(img , caption='オババ',use_column_width=True)


# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns= ['lat','lon']
# )

# st.map(df)

