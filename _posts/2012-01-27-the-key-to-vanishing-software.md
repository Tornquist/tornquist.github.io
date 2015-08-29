---
layout: post
title: "The Key to Vanishing Software"
date: 2012-01-27 10:03:00
categories: code
---
As I've been fiddling with Android programming, I keep seeing software vanish from my "My Apps Folder." Specifically my new projects. I became convinced that certain development settings didn't actually install my application on the phone. Today I learned that I was very wrong. I kept overwriting my applications with new, completely different programs. I misunderstood the purpose of namespace, and was using com.tornquist.nathan for every single application. With the standard environment I've set up, the filenames between projects were identical and old projects were overwritten every time I pushed a new project with the same files. So remember kids, use different namespaces for every program. They actually matter.

More can be read here: [your.package.namespace - what should it be changed to?](http://stackoverflow.com/questions/8991658/your-package-namespace-what-should-it-be-changed-to)

-Nathan
