import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import time


st.title('Streamlit 入門')

st.header('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

# st.write(df)
# st.dataframe(df.style.highlight_max(axis=0))
st.table(df.style.highlight_max(axis=0))
# 動的な表データならst.dataframe、静的な表データならst.table


st.header('マジックコマンド')
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


st.header('ラテフ表記')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')


st.header('チャート表示')
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df2)
# st.area_chart(df2)
# st.bar_chart(df2)


st.header('マップをプロット')
# 新宿の座標が35.69,139.70なので、それに対して0~1の乱数を50で割った数値を足す
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df3)


st.header('画像を表示')

img = Image.open('yukari.jpg')
st.image(img, caption='Yukari Tsuba', use_column_width=True)


st.header('インタラクティブなウィジェット')
'Interactive：動的な'

st.subheader('チェックボックス')
if st.checkbox('Show Image'):
    st.image(img, caption='Yukari Tsuba', use_column_width=True)

st.subheader('セレクトボックス')
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

st.subheader('テキストボックス')
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は', text, 'です。'

st.subheader('スライダー')
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition


st.header('レイアウトを整える')

st.subheader('サイドバー')

text_2 = st.sidebar.text_input('あなたの趣味')
condition_2 = st.sidebar.slider('今日のコンディション', 0, 100, 50)

'あなたの趣味は', text_2, 'です。'
'コンディション：', condition_2

st.subheader('2カラムレイアウト')

left_column, right_colomn = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_colomn.write('ここは右カラム')

st.subheader('エキスパンダー')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせの回答')

expander2 = st.beta_expander('問い合わせ2')
expander2.write('テキストボックスの挿入も可能')
text = expander2.text_input('問い合わせ内容')


st.header('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'