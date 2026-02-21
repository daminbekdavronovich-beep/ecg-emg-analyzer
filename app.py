import streamlit as st
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

st.set_page_config(page_title="ECG Age Analysis", layout="wide")

st.title("🫀 ECG Age-Based Heart Analysis")

st.markdown("ECG signal yuklang va yoshga mos yurak tahlilini oling.")

# ==== AGE NORMAL RANGES ====
def age_normal_range(age):
    if age <= 1:
        return (100, 160)
    elif age <= 10:
        return (70, 120)
    elif age <= 18:
        return (60, 100)
    elif age <= 60:
        return (60, 100)
    else:
        return (60, 90)

# ==== FILE UPLOAD ====
uploaded_file = st.file_uploader("ECG TXT yoki CSV yuklang", type=["txt", "csv"])

if uploaded_file is not None:
    try:
        age = st.number_input("Yoshingizni kiriting", min_value=1, max_value=120, value=25)

        data = np.loadtxt(uploaded_file)
        df = pd.DataFrame(data)

        column_index = st.number_input(
            "Qaysi ustunni olish kerak?",
            min_value=0,
            max_value=df.shape[1] - 1,
            value=0,
            step=1
        )

        signal = df.iloc[:, column_index].values
        signal = signal - np.mean(signal)

        # ==== R-PEAK DETECTION ====
        peaks, _ = find_peaks(signal, distance=50, height=np.std(signal))

        duration_seconds = len(signal) / 1000  # sampling rate 1000 Hz deb olamiz
        bpm = (len(peaks) / duration_seconds) * 60

        st.subheader("📈 ECG Signal")
        st.line_chart(signal)

        st.subheader("❤️ Yurak urish tezligi (BPM)")
        st.metric("BPM", round(bpm, 1))

        normal_min, normal_max = age_normal_range(age)

        st.subheader("📊 Yoshga mos norma")

        st.write(f"Norma: {normal_min} - {normal_max} BPM")

        if bpm < normal_min:
            st.error("⚠️ Yurak urishi past (Bradycardia ehtimoli)")
        elif bpm > normal_max:
            st.error("⚠️ Yurak urishi yuqori (Tachycardia ehtimoli)")
        else:
            st.success("✅ Yurak urishi yoshga mos normal diapazonda")

    except Exception as e:
        st.error(f"Xato yuz berdi: {e}")
