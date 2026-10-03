import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA Explorer | Muhammad Kamil Shah", page_icon="🔎", layout="wide")
st.title("Exploratory Data Analysis Explorer")
st.caption("Upload a CSV and inspect data quality, distributions, outliers and correlations.")

uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded is None:
    st.info("Upload a CSV to begin. The file is processed in the app session.")
    st.stop()

df = pd.read_csv(uploaded)
c1,c2,c3,c4 = st.columns(4)
c1.metric("Rows", f"{len(df):,}")
c2.metric("Columns", len(df.columns))
c3.metric("Missing cells", f"{int(df.isna().sum().sum()):,}")
c4.metric("Duplicate rows", f"{int(df.duplicated().sum()):,}")

tabs = st.tabs(["Preview", "Data quality", "Distribution", "Outliers", "Correlation"])
with tabs[0]:
    st.dataframe(df.head(100), use_container_width=True)
    st.dataframe(df.describe(include="all").T, use_container_width=True)
with tabs[1]:
    q = pd.DataFrame({"dtype":df.dtypes.astype(str),"missing":df.isna().sum(),"missing_%":(df.isna().mean()*100).round(2),"unique":df.nunique(dropna=True)})
    st.dataframe(q, use_container_width=True)
with tabs[2]:
    nums = df.select_dtypes(include=np.number).columns.tolist()
    if nums:
        col = st.selectbox("Numeric column", nums, key="dist")
        fig, ax = plt.subplots()
        ax.hist(df[col].dropna(), bins=30)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig); plt.close(fig)
        st.write({"mean":float(df[col].mean()),"median":float(df[col].median()),"std":float(df[col].std()),"skew":float(df[col].skew()),"kurtosis":float(df[col].kurt())})
    else: st.warning("No numeric columns found.")
with tabs[3]:
    nums = df.select_dtypes(include=np.number).columns.tolist()
    if nums:
        col = st.selectbox("Numeric column", nums, key="out")
        s=df[col].dropna(); q1,q3=s.quantile([.25,.75]); iqr=q3-q1
        lo,hi=q1-1.5*iqr,q3+1.5*iqr; out=s[(s<lo)|(s>hi)]
        st.metric("IQR-rule outliers", len(out))
        fig,ax=plt.subplots(); ax.boxplot(s, vert=False); ax.set_title(f"Box plot: {col}"); st.pyplot(fig); plt.close(fig)
        st.caption(f"IQR bounds: {lo:.3f} to {hi:.3f}. Domain-specific rules may be more appropriate.")
with tabs[4]:
    nums=df.select_dtypes(include=np.number)
    if nums.shape[1]>=2:
        corr=nums.corr()
        fig,ax=plt.subplots(figsize=(8,6)); im=ax.imshow(corr, vmin=-1, vmax=1); ax.set_xticks(range(len(corr.columns)),corr.columns,rotation=45,ha="right"); ax.set_yticks(range(len(corr.columns)),corr.columns); fig.colorbar(im,ax=ax); st.pyplot(fig); plt.close(fig)
        st.dataframe(corr.round(3), use_container_width=True)
    else: st.warning("At least two numeric columns are required.")

st.caption("Muhammad Kamil Shah · Python · pandas · data quality · statistical EDA · visualization")
