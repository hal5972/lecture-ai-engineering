import streamlit as st
import pandas as pd
import numpy as np
import time
from PIL import Image

# ============================================
# ページ設定
# ============================================
# st.set_page_config(
#     page_title="Streamlit デモ",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ============================================
# タイトルと説明
# ============================================
st.title("Today's 新宿 Topic")

# テキスト入力
st.subheader("今日のおすすめランチ")
image = Image.open("carry.jpg")
st.image(image, caption="カレー屋フィッシュの3種コンボ", use_container_width=True)


# カラム
st.subheader("今日の新宿の天気")
col1, col2 = st.columns(2)
with col1:
    st.metric("気温", "24℃", "1%")
with col2:
    st.metric("湿度", "0%", "-10%")

