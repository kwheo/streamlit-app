def main():
    print("Hello from streamlit-app!")
    import streamlit as st
    import pandas as pd
    import numpy as np

    st.title('내 첫 번째 Streamlit 앱')

    st.write('안녕하세요! 이것은 간단한 Streamlit 앱입니다.')

    # 간단한 차트 만들기
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

    # 사이드바에 슬라이더 추가
    x = st.sidebar.slider('x 값 선택', 0, 100, 50)
    st.write(f'x = {x}')

if __name__ == "__main__":
    main()
