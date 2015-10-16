# SoftwareSystemsSynthesizer
For our project, we built an Aruduino Synthesizer based off of the instructions here:

http://www.instructables.com/id/Arduino-Audio-Output/

Using the existing structure, we built a synthesizer that created a single sine wave. We were able to adjust the frequency of the sine wave by changing the value of the interrupt timer. This required uploading the code afresh each time we desired a different frequency of sine wave.

We decided to create code in order to be able to play a song on our Arduino synthesizer. The code consists of a python script (makeOCR2ASeqfromNotes.py) that takes a sequence of notes and their durations and sets the OCR2A timer interrupt frequency accordingly. A song is input as a list of tuples, with one value for note name, and one value for note duration. The python script contains a dictionary that maps the name of a note to its frequency (e.g. B5 is mapped to 987 Hz). The code is written with the assumption of a 4/4 key signature, so a note with a duration of 1 represents a quarter note.

The python script outputs a lits of integer values, which you can then copy and paste into the synthesizer script (final_code.ino).
