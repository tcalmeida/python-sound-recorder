import sounddevice
from scipy.io.wavfile import write


def main():
    
    # sample rate - frames/sec
    fs = 44100

    duration = int(input('How many seconds to you want to record?: '))
    print('Recording...\n')
    voice_record = sounddevice.rec(int(duration * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    write('MyRecording.wav', fs, voice_record)
    print('Record finished')


if __name__ == '__main__':
    main()
