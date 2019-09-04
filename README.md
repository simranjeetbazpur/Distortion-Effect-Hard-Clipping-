# Distortion-Effect-Hard-Clipping

Hard clipping is a type of distortion effect where the amplitude of a signal is limited to a maximum amplitude. This effect can be created in the analog or hardware world when a transistor is pushed to a maximum amplitude.

<img src="https://i.pinimg.com/originals/44/34/67/443467544bd909d97bb4b2bf8cefc82e.jpg"/>

## Langugae Used 
Python 3.6

## Steps To Run the Program 
1. simranjeet.wav file[INPUT FILE] is converted to simranjeet.dat using SoX command i.e sox simranjeet.wav simranjeet.dat[You can skip this step as I have uploaded the simranjeet.dat file as well].
2. Remove first two header lines in the file simranjeet.dat and then use it in python.[I have already edited the simranjeet.dat file so this step can also be skipped]
3. temp.py is the python script you need to run.[I have run it using Spyder in Anaconda]
4. The python script takes the input simranjeet.dat and convert it into out.dat[Also waveforms will be displayed on the spyder console]
5. out.dat can be converted to out.wav using command sox out.dat out.wav

## NOTE: 
<ul>
  <li>simranjeet.wav is input and out.wav is the output produced after distortion.</li>
  <li>#waveforms can be seen in the console itself.</li>
  <li>For listening to sound import .wav files(simranjeet.wav and out.wav) in audacity and play the sound.You can see the difference between two sounds.</li>
  </ul>
  
