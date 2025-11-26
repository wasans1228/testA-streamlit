# simple_stats_app.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 간단 통계 계산기")
st.markdown("CSV 파일을 업로드하면 각 열의 **평균, 분산, 표준편차**를 계산해 보여줍니다.")

# CSV 파일 업로드
uploaded_file = st.file_uploader("CSV 파일 업로드", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### 업로드한 데이터", df)

    # 숫자형 컬럼만 선택
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    if numeric_cols:
        st.write("### 통계 요약")
        stats_df = pd.DataFrame(index=numeric_cols)
        stats_df["평균"] = df[numeric_cols].mean()
        stats_df["분산"] = df[numeric_cols].var()
        stats_df["표준편차"] = df[numeric_cols].std()
        st.table(stats_df)
    else:
        st.warning("숫자형 컬럼이 없습니다.")
else:
    st.info("CSV 파일을 업로드해주세요.")
