# Speech Information Systems – Lab 4

# Sampling, quantization, speech coding

Name: Athoy Debnath
Neptune code: Klevis Imeri
Lab date: 27-03-2025

Audio materials: **p300_005.wav** (you can find it in Teams channel/files/labs)
This report, together with the attachment, must be sent to [aliraheem.mandeel@edu.bme.hu](mailto:%20aliraheem.mandeel@edu.bme.hu).
Please answer the only question in red text

1. Anti-Aliasing
- Using **Audacity**, generate a 2-second long **6 kHz sine wave** with **0.5 amplitude** (_Generate -> Tone…_), then examine its **Spectrum** (_Analyze -> Plot_ _Spectrum…_).
Insert a screenshot of the audio spectrum here!

- To degrade the recording, use <sup><sup>[\[1\]](#footnote-1)</sup></sup>**Audacity's Nyquist prompt** (Tools -> Nyquist Prompt).

Enter the following code:

;version 4

(force-srate 5500 \*track\*)

In this code:

- force-srate forces the program to use the desired sampling frequency.
- 5500 should be replaced with the required sampling rate.
- \*track\* ensures that the original track is overwritten.

In the above code, we specify a frequency at which aliasing occurs, so it is true that fs < 2\*fB<sub>.</sub> Then the signal will merge in time, since we will have fewer samples, but the system still wants to play it at the original sampling frequency. To correct this, adjust the playback speed to the correct sampling rate.


Examine the spectrum of the modified sound and describe your observations.

Insert a screenshot of the spectrum and a brief explanation of the phenomenon!

- Now, create another track and generate another **6 kHz sine wave** using the same method. Then, apply **resampling** using Tracks -> Resample…. **What do you observe this time?**

**Insert a screenshot of the spectrum and provide a brief explanation of the phenomenon!**

1. Aliasing in speech

Using the **p300_005.wav** file, perform the following steps:

1. Use the **Nyquist prompt** to set the sampling rate to **5500 Hz** and also adjust the **track speed** accordingly.
2. Write a few sentences describing what you observe.
3. Identify parameters that allow reducing the sampling rate without significant distortion.
4. Quantization

Download the <sup><sup>[\[2\]](#footnote-2)</sup></sup>file piano**\_96kHz_24bit_stereo.wav** and listen to its quality.

In **Audacity**, go to File -> Export Audio… and save the file with different **bit depths lower than 24-bit**. Observe how the **quantization bit depth** affects the audio quality.

**At what bit depth does quantization noise become audible?** Provide a **brief answer**.

1. **Playing with speech**

These tasks will be performed using **Praat**.

**Load** the **p300_005.wav** file in **Praat** (_Open -> Read from file…_) and **listen** (_Play_).

**Create a manipulation object** (_Manipulate -> To manipulation…_) using the default settings.

In the **Manipulation** object, open _View & Edit_.

Under the **Synth** menu, select **LPC** to synthesize the modified speech.

**Whispered Speech**

Select a part of the file.

Remove the **voiced** components by using _Pulse -> Remove pulses_.

This results in a **completely voiceless segment**, resembling whispered speech.

**Changing Pitch**

Modify **pitch curve points manually** or use:

- _Pitch -> Shift_
- _Pitch -> Multiply_

These allow **uniform pitch changes** across selected parts.

**Creating Monotone Speech**

In **Praat’s main window**, extract the **Pitch Tier** from the Manipulation object (_Extract pitch tier…_).

Modify it using _Modify -> Formula_ and set a **constant pitch (e.g., 150 Hz)**.

Replace the original **Pitch Tier** in the Manipulation object and **resynthesize** the speech.

Please send with this report: whispered speech, Monotone speech, and Speech with increased or decreased fundamental frequency (F0)!

1. <https://manual.audacityteam.org/man/nyquist_prompt.html>

    [https://en.wikipedia.org/wiki/Nyquist_(programming_language)](https://en.wikipedia.org/wiki/Nyquist_%28programming_language%29) [↑](#footnote-ref-1)

2. <https://www.lessloss.com/steinway-sons-grand-piano-recording-p-202.html> [↑](#footnote-ref-2)
