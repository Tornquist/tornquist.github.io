---
layout: post
title: "MegaBrite Programmable RGB LED"
date: 2013-07-07 15:01:00
categories: code
custom_css:
- syntax
---
Over the past few weeks I've been working on a project that utilizes an msp430 micro-controller and a [MegaBrite LED](https://www.sparkfun.com/products/10236).  The LED has a 32-bit shift register and supports 1024 color intensities of red, green and blue.  Unfortunately I shorted the LED chip and burned out the logic device so I cannot provide a video of it working, but this is the Energia logic I've written to control it.  This code should work for an Arduino as well.

```c
void rgbConversion(int red, int green, int blue, int clockPin, int latchPin, int dataPin)
{
  //Set control values
  digitalWrite(dataPin, LOW);
  digitalWrite(clockPin, HIGH);
  digitalWrite(clockPin, LOW);

  int j = 0;
  int i = 9;
  float color = blue*1023.0/255.0;
  int colorInt = color;
  int temp[] = {0,0,0,0,0,0,0,0,0,0};
  for (j = 0; j < 16; j ++)
  {
    temp[i] = !!(colorInt & (1 << j));
    if (j < 10)
    {
      i = i - 1;
    }
  }
  for (i = 0; i < 10; i++)
  {
    digitalWrite(dataPin, temp[i]);
    digitalWrite(clockPin, HIGH);
    digitalWrite(clockPin, LOW);
  }
  i = 9;
  color = red*1023.0/255.0;
  colorInt = color;
  for (j = 0; j < 16; j ++)
  {
    temp[i] = !!(colorInt & (1 << j));
    if (j < 10)
    {
      i = i - 1;
    }
  }
  for (i = 0; i < 10; i++)
  {
    digitalWrite(dataPin, temp[i]);
    digitalWrite(clockPin, HIGH);
    digitalWrite(clockPin, LOW);
  }
  i = 9;
  color = green*1023.0/255.0;
  colorInt = color;
  for (j = 0; j < 16; j ++)
  {
    temp[i] = !!(colorInt & (1 << j));
    if (j < 10)
    {
      i = i - 1;
    }
  }
  for (i = 0; i < 10; i++)
  {
    digitalWrite(dataPin, temp[i]);
    digitalWrite(clockPin, HIGH);
    digitalWrite(clockPin, LOW);
  }
  digitalWrite(latchPin, HIGH);
  digitalWrite(latchPin, LOW);
}
```
