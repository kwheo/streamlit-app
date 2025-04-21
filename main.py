def main():
    import streamlit as st
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    st.title('데이터 시각화 앱')

    # 샘플 데이터 생성
    def generate_data():
        dates = pd.date_range('20230101', periods=100)
        df = pd.DataFrame(np.random.randn(100, 4), 
                        index=dates, 
                        columns=['A', 'B', 'C', 'D'])
        df = df.cumsum()
        return df

    data = generate_data()

    # 사이드바에 옵션 추가
    st.sidebar.header('옵션 설정')
    selected_columns = st.sidebar.multiselect(
        '표시할 열 선택',
        options=data.columns.tolist(),
        default=data.columns.tolist()[:2]
    )

    chart_type = st.sidebar.selectbox(
        '차트 유형 선택',
        ['선 그래프', '영역 그래프', '막대 그래프']
    )

    # 데이터 표시
    st.subheader('원본 데이터')
    st.dataframe(data[selected_columns])

    # 차트 표시
    st.subheader('데이터 시각화')
    if chart_type == '선 그래프':
        st.line_chart(data[selected_columns])
    elif chart_type == '영역 그래프':
        st.area_chart(data[selected_columns])
    elif chart_type == '막대 그래프':
        st.bar_chart(data[selected_columns])

    # Matplotlib 사용 예
    st.subheader('Matplotlib을 사용한 커스텀 시각화')
    fig, ax = plt.subplots(figsize=(10, 4))
    for column in selected_columns:
        ax.plot(data.index, data[column], label=column)
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    main()
