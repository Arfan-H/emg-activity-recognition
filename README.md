# emg-activity-recognition

# EMG Activity Recognition

This project analyzes EMG (Electromyography) signals to recognize human physical activities—both normal and aggressive—using signal processing techniques including low-pass filtering and peak detection.

## 📚 About the Dataset

The dataset used is from Kaggle:  
🔗 [Dataset for Drift Detection – Kaggle](https://www.kaggle.com/datasets/arashnic/dataset-for-drift-detection)

It consists of EMG signals collected from 8 muscle groups (biceps and triceps of both arms, hamstrings and thighs of both legs) using the Delsys EMG wireless apparatus. The data was recorded from 4 participants (3 males and 1 female, aged 25–30), each performing 10 normal and 10 aggressive physical activities.

### 📌 Dataset Highlights:
- **Total Subjects**: 4
- **Actions**: 10 normal + 10 aggressive
- **Channels**: 8 EMG channels (CH1–CH8)
- **Recording Device**: Delsys EMG wireless
- **Environment**: 4m × 5.5m robotic lab arena with punching/kicking dummy

## 🧪 Protocol & Ethics

Participants performed activities voluntarily with full consent. The study followed ethical codes from the British Psychological Society, with minimal risk of injury.

## 🧰 Features

- Load EMG data from multiple text files
- Apply Butterworth low-pass filter
- Detect motion events with peak detection
- Visualize original and filtered signals

## 📁 Data Format

Each `.txt` file contains tab-separated values from 8 EMG channels. One file corresponds to one trial or action type (e.g., Walking, Jumping, Bowing).

## 📦 Dependencies

Install required Python libraries:

```bash
pip install numpy pandas matplotlib scipy
