import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="ECG & EMG Analyzer",
    layout="wide",
    page_icon="📈"
)

# CSS dizayn
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
h1, h2, h3 {
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("📈 ECG & EMG Signal Analyzer")

st.markdown("Zamonaviy signal ko‘rish platformasi")

col1, col2 = st.columns(2)

# ===== ECG =====
with col1:
    st.subheader("🫀 ECG Signal")

    ecg_file = st.file_uploader("ECG fayl yuklang", type=["txt"], key="ecg")

    if ecg_file is not None:
        ecg_data = np.loadtxt(ecg_file)

        if len(ecg_data.shape) > 1:
            ecg_signal = ecg_data[:, 5]
        else:
            ecg_signal = ecg_data

        # 0 markazga tushirish
        ecg_signal = ecg_signal - np.mean(ecg_signal)

        ecg_df = pd.DataFrame({"ECG": ecg_signal})
        st.line_chart(ecg_df, use_container_width=True)


# ===== EMG =====
with col2:
    st.subheader("💪 EMG Signal")

    emg_file = st.file_uploader("EMG fayl yuklang", type=["txt"], key="emg")

    if emg_file is not None:
        emg_data = np.loadtxt(emg_file)

        if len(emg_data.shape) > 1:
            emg_signal = emg_data[:, 5]
        else:
            emg_signal = emg_data

        # 0 markazga tushirish
        emg_signal = emg_signal - np.mean(emg_signal)

        emg_df = pd.DataFrame({"EMG": emg_signal})
        st.line_chart(emg_df, use_container_width=True)