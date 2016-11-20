#!/usr/bin/python

from __future__ import print_function

import sys
import tk_draw
from pydub import AudioSegment

USAGE = "python audio_playground.py mp3_file"


def main(mp3_file):
    sound = AudioSegment.from_mp3(mp3_file)
    loudness = sound.rms
    highest_amp = sound.max
    samples = sound.get_array_of_samples()
    raw = sound.raw_data
    dBFS = sound.dBFS
    max_dBFS = sound.max_dBFS
    print("frame rate: ", sound.frame_rate)
    print("frame count: ", sound.frame_count())
    print("number of channels: ", sound.channels)
    print("sample width: ", sound.sample_width)
    print("loudness: ", loudness)
    print("highest amplitude: ", highest_amp)
    print("dBFS: ", dBFS)
    print("max dBFS: ", max_dBFS)
    print("samples length: ", len(samples))
#    print("raw data: ", raw)
#    print("samples: ", samples)
    normalized = list(map(lambda x: x / highest_amp, samples))
#    print("normalized: ", normalized)
    instance = tk_draw.getInstance()
    window = tk_draw.getWindow(instance)
    print("normalized length: ", len(normalized))
    normalized = normalized[:100000]
    tk_draw.drawData(window, normalized)
#    tk_draw.drawBoard(window, board)
#    tk_draw.attachUpdater(instance, window, board)
    tk_draw.attachMainloop(instance)

if __name__ == '__main__':
    ''' Entry point '''
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print(USAGE)
