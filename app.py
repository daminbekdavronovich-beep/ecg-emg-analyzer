import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="ECG & EMG Analyzer", layout="wide")

st.title("🫀 ECG & 💪 EMG Signal Analyzer")

st.markdown("TXT yoki CSV fayl yuklang va signalni analiz qiling.")

# ==== FILE UPLOAD ====
uploaded_file = st.file_uploader("Fayl yuklang", type=["txt", "csv"])

if uploaded_file is not None:
    try:
        data = np.loadtxt(uploaded_file)
        df = pd.DataFrame(data)

        st.success("Fayl muvaffaqiyatli yuklandi ✅")

        col1, col2 = st.columns(2)

        with col1:
            signal_type = st.selectbox("Signal turini tanlang", ["ECG", "EMG"])

        with col2:
            column_index = st.number_input(
                "Qaysi ustunni olish kerak?",
                min_value=0,
                max_value=df.shape[1] - 1,
                value=0,
                step=1
            )

        signal = df.iloc[:, column_index]
        signal = signal - np.mean(signal)

        # Tezlashtirish
        if len(signal) > 5000:
            step = len(signal) // 5000
            signal = signal[::step]

        st.subheader(f"{signal_type} Signal Grafigi")

        st.line_chart(signal, use_container_width=True)

        st.subheader("📊 Statistika")

        col3, col4, col5 = st.columns(3)

        col3.metric("O'rtacha", round(float(np.mean(signal)), 2))
        col4.metric("Maks", round(float(np.max(signal)), 2))
        col5.metric("Min", round(float(np.min(signal)), 2))

    except Exception as e:
        st.error(f"Xato yuz berdi: {e}")
