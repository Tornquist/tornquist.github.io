---
layout: post
title: "Android Screen Scaling and Cross-Platform Support"
date: 2012-05-17 20:18:00
categories: code
custom_css:
- syntax
---

There are tons of resources online discussing the best ways to implement cross-platform support for android.  Most of those articles however are aimed at building xml interfaces that automatically scale. When I started Storm the Castle two months ago I really couldn't find a good explanation for getting Cross-Platform support on games.  Additionally I fell under the assumption that OpenGL was only fit for 3D games, and that anything in 2D should be directly written using Canvas.

With those thoughts in mind I began thinking of the best way to scale my game.  Sometime during early development I either misread an article or there was a misguided article that convinced me that there was no way that a Canvas would autoadjust or that there is any autoscaling built in.  That is partially correct. I took that to mean that there could be no scaling, not that you simply had to implement the scaling.

I then undertook the process of writing my game in a way that would allow it to scale to any device size.  I built an image class that automatically adjusted my sprites and I had every distance and position in the game multiplied times the appropriate scaleX or scaleY factor.

In all of my testing that worked perfectly of course.  I was testing on a device with the game's native resolution.  When I emailed my brother the \*.apk file yesterday I came under the horrible realization that I had been horribly misguided.  For awhile I was at the point that I thought the entire game needed to be rewritten before a wonderful user on StackOverflow suggested I use the matrix.preScale() method.  That method would allow me to render the entire game on a 960 x 540 canvas and then scale that canvas to fit any screen size.

There are some obvious pros and cons to this.  The biggest con is my continued use of the Canvas class, instead of rewriting the game in OpenGL.  Seeing as the game is not super graphically intensive and will require a fairly modern phone to run anyway, I was able to get by with the decreased speed associated with Canvas.  Another huge con is that the game is scaling itself every loop.  If I used OpenGL and just set the camera angle correctly, or if I had gotten the scaling implementation correct, then the game would simply draw what the user would see, and no other effects would be needed.

The huge pro is that it is easy to implement and doesn't require me to rewrite the graphics engine.  And for that pro, I am willing to sacrifice a bit in performance.  To actually implement the matrix scaling, I needed to do two things.  The first is determine the scale factors needed to adjust the canvas, so that the graphics would be scaled the right way, and the second is to use that same scalefactor to adjust the touch input.  If I am testing on a screen half the size of my native resolution, I need to scale the graphics down and the touch input up, so the user sees the correct display and the game receives the correct input. This is exactly what I did.

Within the initialization of my game panel I run the following method:

```java
public void setScale(int DeviceWidth, int DeviceHeight)
{
  this.deviceWidth = DeviceWidth;
  this.deviceHeight = DeviceHeight;
  float widthA = (float)deviceWidth;
  float widthB = (float)DEFAULT_WIDTH;
  float heightA = (float)deviceHeight;
  float heightB = (float)DEFAULT_HEIGHT;
  this.scaleX = widthA/widthB;
  this.scaleY = heightA/heightB;
}
```

One of the most important aspects of that is the fact that I convert all the integer values to floats.  Without that rounding could cause my scale factor to round down to zero, which would prevent anything from being drawn to the screen.  Once the scalefactor is set I run the following code from my main Thread:

```java
Matrix matrix = new Matrix();
matrix.preScale(gamePanel.getScaleX(), gamePanel.getScaleY());
```

The getScaleX() and getScaleY() methods simply return the scaleX and scaleY values found above.  This allows me to set the matrix in a way that will scale the game canvas correctly.  Once the matrix is set I use the following in the main loop.  My loop looks like this:

```java
canvas = this.surfaceHolder.lockCanvas();
canvas.setMatrix(matrix);
synchronized (surfaceHolder)
{
  // update game state
  startTime = System.currentTimeMillis();
  this.gamePanel.update(elapsedTime);

  // draws the canvas on the panel
  this.gamePanel.onDraw(canvas);

  elapsedTime = System.currentTimeMillis() - startTime;
}
```

There is of course a try catch loop around that to handle and exceptions and to make sure that the canvas gets unlocked, but that is the basic loop.

The final piece is getting the touch input to scale correctly.  The important thing here is that the scale factors are used in the opposite direction.  Because this time you are going from the device resolution to the native resolution instead of going the opposite way.

My onTouchEvent() method looks like this:

```java
@Override
public boolean onTouchEvent(MotionEvent event) {
  int action = event.getAction() & MotionEvent.ACTION_MASK;
  int pointerIndex = (event.getAction() & MotionEvent.ACTION_POINTER_ID_MASK) >> MotionEvent.ACTION_POINTER_ID_SHIFT;
  int pointerId = event.getPointerId(pointerIndex);
  switch (action) {
    case MotionEvent.ACTION_DOWN:
    case MotionEvent.ACTION_POINTER_DOWN:
      //Log.d("pointer id - down",Integer.toString(pointerId));
      fingerData[pointerId][0] = event.getX(pointerIndex)/scaleX;
      fingerData[pointerId][1] = event.getY(pointerIndex)/scaleY;
      fingerData[pointerId][2] = 1;
      break;

    case MotionEvent.ACTION_UP:
    case MotionEvent.ACTION_POINTER_UP:
    case MotionEvent.ACTION_CANCEL:
      //Log.d("pointer id - cancel",Integer.toString(pointerId));
      fingerData[pointerId][0] = event.getX(pointerIndex)/scaleX;
      fingerData[pointerId][1] = event.getY(pointerIndex)/scaleY;
      fingerData[pointerId][2] = 0;
      break;

    case MotionEvent.ACTION_MOVE:

      int pointerCount = event.getPointerCount();
      for(int i = 0; i < pointerCount; ++i) {
        pointerIndex = i;
        pointerId = event.getPointerId(pointerIndex);
        //Log.d("pointer id - move",Integer.toString(pointerId));
        fingerData[pointerId][0] = event.getX(pointerIndex)/scaleX;
        fingerData[pointerId][1] = event.getY(pointerIndex)/scaleY;
        fingerData[pointerId][2] = 1;
      }
      break;
  }
  return true;
}
```

That too works exactly as planned.  I tested this new code yesterday on a Samsung S Aviator and it not only scaled correctly, but I saw no decrease in performance. While this solution may not be as elegant as OpenGL it allows you to stick to the basic android libraries, and it ultimately scales just as well.

-Nathan
