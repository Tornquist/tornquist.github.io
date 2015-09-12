---
layout: post
title: "Objective-C: Instance Variables and Where They Like to Play"
date: 2011-01-29 21:36:00
categories: code
---
As I have written about before, the most difficult part of Objective-C for me is getting the variable declarations to work correctly.  The lesson of today is where variables need to be declared and what each area does specifically. There are two types of variables, public and private.  In standard class declaration you have a header (.h) and an implementation file (.m). Getting global objects is completely different from creating global variables.  Ironically enough, I was able to get local objects and global variables working correctly, but the opposite proved difficult because of the differences in Objective-C. The following displays the differences in variable declaration.

Local Boolean Variable:

{% highlight objective-c %}
//Object.h
@interface Object : NSObject {
	BOOL Variable;
}
@end
{% endhighlight %}

{% highlight objective-c %}
//Object.m
#import "Object.h"
@implementation Object
@end
{% endhighlight %}

Global Boolean Variable:

{% highlight objective-c %}
//Object.h
@interface Object : NSObject {

}
@end
{% endhighlight %}

{% highlight objective-c %}
//Object.m
#import "Object.h"
@implementation Object
BOOL Variable;
@end
{% endhighlight %}

As you can see, this process is incredibly simple, but proves quite challenging when you are trying to write everything like it was C#. As far as global and local objects are concerned, global objects can be set up with a singleton class.  Once the class is set up, you just access the class manager to change any objects that you have created within it.  My singleton class looks lik

{% highlight objective-c %}
//
//  SharedVariables.h
//

#import

@interface SharedVariables : NSObject {
	//This is where all global objects are defined.
	NSMutableArray *objectList;

}
//Allocated memory is set normally.
@property (nonatomic, retain) NSMutableArray *objectList;

+ (id)sharedManager;

@end
{% endhighlight %}

{% highlight objective-c %}
//
//  SharedVariables.m
//  Log.Acc
//
//  Created by Nathan Tornquist on 11/25/10.
//  Copyright 2010 Student. All rights reserved.
//

#import "SharedVariables.h"

static SharedVariables *sharedMyManager = nil;

@implementation SharedVariables

//Synthesize All Objects
@synthesize objectList;

#pragma mark Singleton Methods
+ (id)sharedManager {
    @synchronized(self) {
        if(sharedMyManager == nil)
            sharedMyManager = [[super allocWithZone:NULL] init];
    }
    return sharedMyManager;
}
+ (id)allocWithZone:(NSZone *)zone {
    return [[self sharedManager] retain];
}
- (id)copyWithZone:(NSZone *)zone {
    return self;
}
- (id)retain {
    return self;
}
- (unsigned)retainCount {
    return UINT_MAX; //denotes an object that cannot be released
}
- (void)release {
    // never release
}
- (id)autorelease {
    return self;
}
- (id)init {
    if (self = [super init]) {
		//Initiate All Objects
		objectList = [[NSMutableArray alloc] init];
    }
    return self;
}
- (void)dealloc {
	// Should never be called, but just here for clarity really.
	[objectList release];
	[super dealloc];
}

@end
{% endhighlight %}

And finally you can access any of the objects in the singleton class like so:

{% highlight objective-c %}
//Include the header file in the class that you want to give access
//to the singleton to.
#import "SharedVariables.h"

//Access as so:
SharedVariables *manager = [SharedVariables sharedManager];
int count = [manager.objectList count];
//Simply use [manager.objectname function] like any other
//Objective-C object.
{% endhighlight %}

Hopefully this helps anyone starting with Objective-C.

-Nathan
