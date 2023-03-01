from scipy.io import wavfile
from scipy.fftpack import fft
import numpy as os
import numpy as np, os



def main(path):
    good_answer = 0
    full_answer = 0

    good_man = 0
    good_woman = 0
    man = 0
    woman = 0

    for file in os.listdir(path):
     #   print(file[4])
        w, signal = wavfile.read(path + file)
        signal = signal[::10]
        w = round(w / 10)
        letter = function_signal(signal, w)

        if letter == file[4]:
            good_answer += 1
        full_answer += 1

        if file[4] == 'M':
            man +=1
        else:
            woman+=1

        if letter == 'M' and file[4] == 'M':
            good_man +=1

        if letter == 'K' and file[4] == 'K':
            good_woman +=1

    print("\nAll audio files: " + str(full_answer) + "\nAccepted files: " + str(good_answer) + "\nPercent good answer: " + str(good_answer/full_answer*100))
    print("--------------------------------------")
    print("Man: " + str(good_man))
    print("Woman: " + str(good_woman))
    print("--------------------------------------")
    print("Recognized woman: " + str(woman - good_woman))
    print("Recognized man: " + str(man - good_man))

def recognize_gender(index):
    if index <= 165:
        return 'M'
    return 'K'

def fundamental_frequency(signal, w):
    signal = np.array(signal)
    if signal.ndim > 1:
        signal = signal[:, 0]
    n = len(signal)
    x = np.linspace(0, w, n)

    signal_fft = fft(signal)
    signal_fft = np.abs(signal_fft)
    signal_fft = signal_fft / n * 2
    signal_fft[0] /= 2

    signal_filtered = np.ones(signal_fft.shape)
    signal_filtered[:int(70 * n / w)] = 0
    signal_filtered[int(n / 2) + 1:] = 0

    for i in range(1, 5):
        for j in range(int(len(signal_filtered) / i)):
            signal_filtered[j] *= signal_fft[j * i]

    return x[np.argmax(signal_filtered)]

def function_signal(signal, w):
    x = len(signal)
    coefficient = {'M': 0, 'K': 0}
    for j in range(3):
        for i in range(j + 2):
            gender = recognize_gender(fundamental_frequency(signal[int(i * x / (2 + j)):int((i + 1) * x / (2 + j))], w))
            coefficient[gender] += (1 / (j + 2))
    if coefficient['M'] > 1.65:
        vote = 'M'
    else:
        vote = 'K'
    return vote


if __name__ == '__main__':
    main('train/')

