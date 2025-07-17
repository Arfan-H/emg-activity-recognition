import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, find_peaks

# Fungsi untuk membaca data dari file
def read_emg_data(file_path):
    data = pd.read_csv(file_path, sep="\t", header=None)
    return data

# Fungsi untuk menerapkan filter Butterworth
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Load dataset
jumping_data = read_emg_data("Jumping.txt")
walking_data = read_emg_data("Walking.txt")
bowing_data = read_emg_data("Bowing.txt")

# Asumsikan kolom 0 adalah sinyal target (disesuaikan dengan dataset Anda)
emg_signal = walking_data[0]

# Parameter filter
sampling_rate = 1000  # Frekuensi sampling (asumsi, sesuaikan dengan data Anda)
cutoff_freq = 10  # Frekuensi cutoff untuk lowpass filter
filtered_signal = butter_lowpass_filter(emg_signal, cutoff_freq, sampling_rate)

# Deteksi puncak untuk mendeteksi jumping
peaks, _ = find_peaks(filtered_signal, height=500)  # Adjust height as needed
peak_count = len(peaks)

# Visualisasi sinyal
plt.figure(figsize=(10, 6))
plt.plot(emg_signal, label='Original Signal')
plt.plot(filtered_signal, label='Filtered Signal', alpha=0.7)
plt.scatter(peaks, filtered_signal[peaks], color='red', label='Detected Peaks')
plt.title('EMG Signal Analysis')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

print(f"Jumlah jumping terdeteksi: {peak_count}")
