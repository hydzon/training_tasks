import os
import whisper
import pandas as pd
import json


class Whisper:
    with open('whisper_models.json', 'r') as json_file:
        models = json.load(json_file)

    def __init__(self, model='3'):
        self.model = whisper.load_model(Whisper.models[model]['Size'][:-6])

    def transcribe_audio(self, audio_file):
        return self.model.transcribe(audio_file)


def main():
    print('Wisper models:')
    print(pd.DataFrame(Whisper.models).transpose())
    model = input('Select number of model: ')
    if model in '12345':
        transcribe = Whisper(model=model)
        # file = input('Enter name audio file: ')
        file = 'C:/Users/Sergey/PycharmProjects/training_tasks/whisper_files/YUrijj_SHatunov_-_Sedaya_noch.mp3'
        if os.path.isfile(file):
            with open('whisper_files/transcribe.txt', 'w') as tr_file:
                tr_file.write(transcribe.transcribe_audio(file))
                print('Transcribe complete.')
        else:
            print(f'File not found: {file}')
    else:
        print(f'Model № {model} not find.')


if __name__ == '__main__':
    main()
