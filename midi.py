from mido import MidiFile, MetaMessage

mid = MidiFile('song.mid')

C2 = 65.4

def get_notes():
    notes = []

    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            data = str(msg).split()
            if type(msg) != MetaMessage:
                if data[0] == 'note_on':
                    notes.append(int(data[2].split('=')[-1]))


    notes = list(map(lambda n: C2 * 2 ** ((n - 60) / 12), notes))
    return notes
