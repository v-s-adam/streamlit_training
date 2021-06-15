import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

st.title('Streamlit 入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))
# 動的な表データならst.dataframe、静的な表データならst.table

st.write('マジックコマンド')
"""
# 章
## 節
### 項
テキストテキスト

pythonのコードを表示
```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

st.write('ラテフ表記')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


st.write('チャート表示')
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df2)
# st.area_chart(df2)
# st.bar_chart(df2)


st.write('マップをプロット')
# 新宿の座標が35.69,139.70なので、それに対して0~1の乱数を50で割った数値を足す
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df3)

st.write('画像を表示')

img = Image.open('yukari.jpg')
st.image(img, caption='Yukari Tsuba', use_column_width=True)
