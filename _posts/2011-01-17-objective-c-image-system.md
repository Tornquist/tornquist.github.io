---
layout: post
title: "Objective-C: Image System"
date: 2011-01-17 11:28:00
categories: code
---
I have decided that I do not want to rely on a game library for my first major Obj-C game.  I may in the future, but I do not want to get into the situation where I know a single library, not a language.  There are a few ways that I could code my graphics system. The first is with UIImageViews and UIViews.  I could have  a separate view for each image and then manipulate the views. That would work, but I prefer to code with a canvas where each time the game loops every item is drawn the the screen with a back and front buffer system.  This morning I simulated that with Objective-C.

First I set up a sample class: Object.  This class has some simple initiation code that takes an x and y coordinate, and then the draw method:

{% highlight objective-c %}
- (void)draw:(CGContextRef)ctx
{
     CGContextSetRGBFillColor(ctx, 255, 0, 0, 1);
     CGContextFillEllipseInRect(ctx, CGRectMake(X, Y,20, 20));
}
{% endhighlight %}

In my UIView I overloaded the drawRect method like so:

{% highlight objective-c %}
- (void)drawRect:(CGRect)rect
{
     // Drawing code
     SharedVariables *manager = [SharedVariables sharedManager];
     CGContextRef context = UIGraphicsGetCurrentContext();
     CGContextClearRect(context, rect);
     for (int i = 0; i &lt; [manager.objectList count]; i++)
     {
          [[manager.objectList objectAtIndex:i] draw:context];
     }
}
{% endhighlight %}

All the objects are stored in objectList within my shared methods class. I just add objects when I wish to draw them to the screen. At this point in time no objects are cleared so everything stays, but doing so is just as simple as deleting everything in objectList.

This method is simple and yet because I have access to all of the CG methods, it is still powerful enough for me to make a viable game.  I shouldn't run into any problems other than the potential of having to write my own collision detection system as well.
