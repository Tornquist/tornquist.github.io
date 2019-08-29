---
layout: post
title: "HP ENVY Thoughts and Experiences"
date: 2011-06-11 23:09:00
categories: thought
---
For college I upgraded to an HP ENVY, HP's MacBook lookalike. The PC is as I
just said, a PC, but has all of the sleek benefits and little gimmicks that Macs
have, like a multitouch trackpad, backlit keyboard, seamless case, slot load disk
drive, etc. Anyway, in the transition, I have learned some important things that
I would like to share, in case someone like myself happens to come across this.

Firstly, HP changed the way that they format their hard drives. I had been
planning to immediately set up a dual boot system with OSX86 on a partition,
and then a FAT32 partition to share files. My Pavilion had a single restore
partition, so in my mind, this would all be possible. The new HP PC's have a boot
partition with Windows 7, a recovery partition, and then two other partitions with
recovery files. This means that the maximum number of partitions are met for
simple hard drive formatting, and dynamic disks (5+ partitions) do not allow more
than one partition to boot. That essentially makes a dual boot system impossible
unless you delete the recovery partitions, which I was not about to do. This
discovery was a bit disheartening, but in the end, made the setup quite a bit
simpler. I'll just have to use my existing Apple hardware to program instead of
carrying around one unit that does everything. (If I really needed dual boot, I
would just have deleted the partitions and used my recovery disk if I needed it.
Recovery disks are no longer sent with the hardware, but are made by the user
with a tool included in Windows.)

On my Apple setup I have the main sync profile for my iPod and use that OS for
my Objective-C programming. When I got the ENVY, I wanted to have my entire
iTunes library present, and be able to sync normally without loosing the ability
to program. To accomplish this, I copied the entire iTunes folder from OSX to
7 after installing the same version of iTunes. From there I just had to delete
the content of the iTunes library on 7.

* Do not edit the XML iTunes library
* Do delete everything in the iTunes library formatted file.

Once the corrupt file is detected, the library will be rebuilt from the XML file.
Assuming that your music is well organized, everything should work. The XML file
only stores local file locations, not the full path, so that did not create a
problem. From there I synced with the new pc and then disabled autosync on the
Mac. From here I will just sync with 7 and then program with OSX. Life is good.
Problems will only arise if I sync within OSX. While this method worked with OSX
to 7, it should work the same for anyone wanting to upgrade their computer. The
best part is that it did not erase my iPod, because I copied the sync identity.
That means that everything was faster and I didn't have to rejailbreak anything.

Other things I did... I had to upgrade the trackpad driver to get multitouch
gesture support, and I upgraded the bluetooth driver. Everything else auto updated.

I think that's about it. It is awesome to have a computer that can play modern
games and turn on without having to be plugged in. I'll probably blog about my
experiences with L4D2 and splitscreen support + bluetooth PS3 controllers at a
later date.

**EDIT:** The computer is quite good. I am very pleased with it, and will save
comments of that sort for a post at a later date.

Nathan
