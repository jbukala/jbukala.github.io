import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq, irfft

INPUT_FILE_MALE = './potato-farm-male.wav'
INPUT_FILE_FEMALE = './potato-farm-female.wav'

# Read input files
def get_raw_signal_and_fourier(input_file: str):
    sample_rate, data = wavfile.read(input_file)
    data = data[40000:90000, :] # Cut off some silent parts of audio files
    num_audio_channels = data.shape[1]
    num_samples = data.shape[0]
    print(f"number of channels = {num_audio_channels}")

    # Get raw signal
    x = np.arange(0, num_samples/sample_rate - 1/sample_rate, 1/sample_rate)
    y = (data[:, 0] - np.mean(data[:, 0])) / np.std(data[:, 0])  # take first channel only for now and standardize it

    # Get Fourier-transformed signal (only need second half as its a real-valued input)
    xf = rfftfreq(num_samples, 1 / sample_rate)
    yf = rfft(y)

    return x, y, xf, yf, sample_rate

x_male, y_male, xf_male, yf_male, rate_male = get_raw_signal_and_fourier(INPUT_FILE_MALE)
x_female, y_female, xf_female, yf_female, rate_female = get_raw_signal_and_fourier(INPUT_FILE_FEMALE)

# Plot original and fourier transformed signals:
plotcolor = '0.8' # Light gray for all axes and labels
with plt.rc_context({'axes.edgecolor':plotcolor, 'xtick.color':plotcolor, 'ytick.color':plotcolor}):
    f, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1)
    ax1.plot(x_male, y_male, 'r')
    ax2.plot(xf_male, yf_male, 'b')
    ax3.plot(x_female, y_female, 'r')
    ax4.plot(xf_female, yf_female, 'b')

    ax1.set_title("Raw audio signal of spoken words", color=plotcolor)
    ax1.set_xlabel('Time (s)', color=plotcolor)

    ax2.set_title("Fourier-transformed signal", color=plotcolor)
    ax2.set_xlabel('Frequency (Hz)', color=plotcolor)

    ax3.set_title("Raw audio signal of the same words by another person", color=plotcolor)
    ax3.set_xlabel('Time (s)', color=plotcolor)

    ax4.set_title("Fourier-transformed signal", color=plotcolor)
    ax4.set_xlabel('Frequency (Hz)', color=plotcolor)
plt.tight_layout()
plt.savefig('./images/fourier-transform-audio.svg', transparent=True)

# Start filtering low-frequency noise:
xf_male_highpass  = xf_male
yf_male_highpass  = yf_male
yf_male_highpass[0:500] = 0

# Inverse Fourier transform the signal:
y_male_highpass = irfft(yf_male_highpass)
x_male_highpass = np.arange(0, len(y_male_highpass)/rate_male - 1/rate_male, 1/rate_male) # use sample rate to show time-axis for plot

with plt.rc_context({'axes.edgecolor':plotcolor, 'xtick.color':plotcolor, 'ytick.color':plotcolor}):
    f, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(x_male_highpass, y_male_highpass, 'r')
    ax2.plot(xf_male_highpass, yf_male_highpass, 'b')
    ax1.set_title("Filtered audio signal", color=plotcolor)
    ax1.set_xlabel('Time (s)', color=plotcolor)

    ax2.set_title("Fourier-transformed filtered signal", color=plotcolor)
    ax2.set_xlabel('Frequency (Hz)', color=plotcolor)
plt.tight_layout()
plt.savefig('./images/fourier-transform-audio-highpass-filtered.svg', transparent=True)

# Write single-channel filtered signal to wav file:
FILTERED_AUDIO_OUTPUT_FILE = 'potato-farm-highpass.wav'
wavfile.write(FILTERED_AUDIO_OUTPUT_FILE, rate_male, y_male_highpass)



##### Filter high frequencies in other file
xf_female_lowpass  = xf_female
yf_female_lowpass  = yf_female
yf_female_lowpass[2500:] = 0

# Inverse Fourier transform the signal:
y_female_lowpass = irfft(yf_female_lowpass)
x_female_lowpass = np.arange(0, len(y_female_lowpass)/rate_female - 1/rate_female, 1/rate_female) # use sample rate to show time-axis for plot

with plt.rc_context({'axes.edgecolor':plotcolor, 'xtick.color':plotcolor, 'ytick.color':plotcolor}):
    f, (ax1, ax2) = plt.subplots(2, 1)
    ax1.plot(x_female_lowpass, y_female_lowpass, 'r')
    ax2.plot(xf_female_lowpass, yf_female_lowpass, 'b')
    ax1.set_title("Filtered audio signal", color=plotcolor)
    ax1.set_xlabel('Time (s)', color=plotcolor)

    ax2.set_title("Fourier-transformed filtered signal", color=plotcolor)
    ax2.set_xlabel('Frequency (Hz)', color=plotcolor)
plt.tight_layout()
plt.savefig('./images/fourier-transform-audio-lowpass-filtered.svg', transparent=True)

# Write single-channel filtered signal to wav file:
FILTERED_AUDIO_OUTPUT_FILE = 'potato-farm-lowpass.wav'
wavfile.write(FILTERED_AUDIO_OUTPUT_FILE, rate_female, y_female_lowpass)