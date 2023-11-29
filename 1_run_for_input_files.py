# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 22:21:38 2023

@author: lafas
"""
from pedalboard import Pedalboard, Compressor, Gain, Chorus, Phaser, Reverb, Limiter, Distortion
from pedalboard.io import AudioFile
import random
import os
files= os.listdir('unprocessed_audio_data/')

# Read in a whole file, resampling to our desired sample rate:
samplerate = 44100.0
for file in files:
    with AudioFile('unprocessed_audio_data/'+ file).resampled_to(samplerate) as f:
        audio = f.read(f.frames)
    
    # Define the number of unique results you want
    num_results = 100
    
    # Create a list to store the results
    results = []
    
    # Loop to generate unique results
    for _ in range(num_results):
        # Create a new pedalboard with random effect parameter settings
        board = Pedalboard()  # Create an empty pedalboard
        
        # Add Compressor with random parameters
        board.append(Compressor(threshold_db=random.uniform(-50, 0), ratio=random.uniform(1, 20)))
        
        # Add Gain with random parameters
        board.append(Gain(gain_db=random.uniform(0, 40)))
        
        # Add Chorus with random parameters
        board.append(Chorus(rate_hz=random.uniform(0.1, 5), depth=random.uniform(0.1, 1)))
        
        # Add Phaser with random parameters
        board.append(Phaser(rate_hz=random.uniform(0.1, 5), depth=random.uniform(0.1, 1)))
        
        # Add Reverb with random parameters
        board.append(Reverb(room_size=random.uniform(0.1, 0.5)))
        
        # Add Limiter with random parameters
        board.append(Limiter(threshold_db=random.uniform(-10, 0)))
    
        
        # Add Distortion with random parameters
        board.append(Distortion(drive_db=random.uniform(0, 25)))
        
        # Process the audio through the pedalboard
        effected = board.process(audio, samplerate)
        
        # Append the result to the list
        results.append(effected)
    
    # Save the results to separate audio files
    for i, result in enumerate(results):
        with AudioFile(f'processed_audio_data/{file}_{i}.wav', 'w', samplerate, result.shape[0]) as f:
            f.write(result)

