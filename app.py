import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout="wide")

st.title("⚡ Fast ECG & EMG Analyzer")

MAX_POINTS = 2000  # maksimal ko‘rsatiladigan nuqta

def downsample(signal, max_points=MAX_POINTS):
    if len(signal) > max_points:
        step = len(signal) // max_points
        return signal[::step]
    return signal

col1, col2 = st.columns(2)

# ===== ECG =====
with col1:
    st.subheader("🫀 ECG")

    ecg_file = st.file_uploader("ECG fayl", type=["txt"], key="ecg")

    if ecg_file is not None:
        ecg_data = np.loadtxt(ecg_file)

        if len(ecg_data.shape) > 1:
            ecg_signal = ecg_data[:, 5]
        else:
            ecg_signal = ecg_data

        ecg_signal = ecg_signal - np.mean(ecg_signal)
        ecg_signal = downsample(ecg_signal)

        st.line_chart(ecg_signal, use_container_width=True)


# ===== EMG =====
with col2:
    st.subheader("💪 EMG")

    emg_file = st.file_uploader("EMG fayl", type=["txt"], key="emg")

    if emg_file is not None:
        emg_data = np.loadtxt(emg_file)

        if len(emg_data.shape) > 1:
            emg_signal = emg_data[:, 5]
        else:
            emg_signal = emg_data

        emg_signal = emg_signal - np.mean(emg_signal)
        emg_signal = downsample(emg_signal)

        st.line_chart(emg_signal, use_container_width=True)        st.line_chart(emg_df, use_container_width=True)
