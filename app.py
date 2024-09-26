import streamlit as st
import numpy as np

st.title('Demo Page')
st.write('Streamlit 배포 테스트 파일입니다.')
st.write('Hello world!')

st.warning('warning test')
st.write(f'numpy test : {np.array(1) + np.array(2)}')