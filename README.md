# Frequency_Count_of_wave_from_generator

<img width="711" alt="Pasted Graphic 1" src="https://github.com/user-attachments/assets/760096ad-51e3-4bcc-a881-cd644b0e52d5">

<pre>
  Parts:
  NPN transistor 2N3904 x 1
  Schmitt trigger inverter SN74HC04N x 1
  resister 470K Ohm x 1
  resister 3.3K Ohm x 1
  capacitor 0.1 micro F x 2
</pre>

## usage

Read serial

<pre>
  python3 read_s.py /dev/tty.usbmodem1201 57600
</pre>

plot serial

<pre>
  python3 waveplot.py /dev/ttyACM0 57600
</pre>

## ref

ものづくりやろう!／第二十一回 Arduino Unoでつくる簡易周波数カウンタ｜2023年2月号 - 月刊FBニュース　アマチュア無線の情報を満載

https://www.fbnews.jp/202302/manufacturing/

PaulStoffregen/FreqCount: Measures the frequency of a signal by counting the number of pulses during a fixed time.

https://github.com/PaulStoffregen/FreqCount
