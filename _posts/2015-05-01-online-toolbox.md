---
layout: post
title: "Online Toolbox"
date: 2015-05-01 03:24:00
categories: programming
---
# Movement I - The Backstory:

Over the past semester I have designed and developed a new tool for the Band and Orchestra department at Purdue University. My product is really the final iteration in a process that has spanned the last five or so years. Recruitment is a difficult process and the original goal was to have some sort of online system that allowed tracking of incoming students and provided a better level of accountability. The aim was to eliminate as much uncertainty as possible regarding the expected numbers of students at band camp. Planning for the season and shows starts well before band camp, so the more accurate the information is, the more planning can be done in advance.

A good friend of mine and fellow trumpet player, Doug Booth, built the original iteration of the Online Toolbox. His tool filled the need. He created a system using php and sql that would allow for importing students, tracking their status (committed to band camp, not committed, undecided) as well as provide some information full section breakdowns. During the marching band season it allowed the Chief of Staff to assign gigs (strikes) to students and also provided an avenue to track attendance.

After he graduated, he handed me the codebase and I became the new webmaster of the online toolbox. As is expected, due to changing situations and staff within Purdue Bands, there were requests for new features and improvements. The first was to add some additional fields to the student information form. These fields were all related to parent information: Names, Address, Email, etc. While this sounds like a simple task, the first iteration of the toolbox was not object oriented. To add the new fields I had to initially add the new columns to the database, then I had to go ahead and update the form in three of four separate files. This was a simple task, but I realized that without my programming skills it would have been a far from easy. Additionally, every year in preparation for the new season, every table in the database had to be carefully emptied to clean out old data and scores to make room for the next year. There were no perpetual tables.

Doug's system was effective and met the need that existed, but required both a fair amount of time and a fair amount of skill to maintain. I had my work cut out for me though, Doug had figured out what the need was and already determined how the userbase inside Purdue Bands functioned. The Minimum Viable Product existed, and the next logical step was version 2.0. With all of his "market research" in hand, I made it my goal to eliminate my job.

# Movement II - Making Contact:

When I set out to add the new parental contact information I discovered a fundamental flaw in the original design.  There was no way for the people responsible for managing recruitment to adjust a contact form on their own.  To do so, they would have to contact the current webmaster and wait for that individual to take care of it.  In most cases it could be done fairly quickly, but as this is a student run endeavor, what if someone has a bad week? Or a bad month?  In that case, it could be a few weeks or longer before the form is updated, and for what? To collect a few more pieces of information.  The first phase of this project revolved around creating a system that allowed for instantaneous modification of the contact form.  I wanted a form built in such a way that you could add and remove new fields at will and do so without having to change the database structure at all.

After I had played with a few different concepts, I finally settled on a schema that would meet my needs.  The Student table that had contained roughly 25+ columns in the original iteration of the toolbox was reduced to 8 columns.  First name, last name, email, recruit, archive, a primary key, and both an updated and created at timestamp.  In addition to the student table, a fields table was created that would ultimately contain all of the information necessary to built a contact form.  The concept of a field is simple: a textbox, combo box, or an address. Adding and removing entries from the field table would trigger updates to the rest of the system when student information was loaded.

To comply with this flexible style of creating forms, a non-traditional database structure was also needed.  Instead of storing data in a table corresponding to what type of object the data is, I instead store the data based on what the raw datatype is.  There is a table for text fields, a table for option fields, and a table for addresses.  Each entry in those three tables has a unique id and foreign keys corresponding to the field type, and to the student that it is related to.  When data is saved from a field in the form, the field type is used to cross reference against the table that the data should actually be put in.

And with that, the most important piece of the new tool was built.  The ability to store student data quickly and adapt quickly without the need of a developer had been met.

# Movement III - Season by Season:

With the concept of a student firmly ironed out, I needed to focus on actually making this tool useful for tracking student performance during a season.  The original version of the tool supported gigs and other notes during a season, but at the end of the year everything had to be manually emptied out and cleaned up.  After doing that once, I certainly did not wish to do it again.  The concept of a season is simple, it has a start date and an end date.  A season also has sections within it.  Each student then is part of the section.  A season's students are the sum of all of the student's within the associated sections.  That concept was built out and then expanded.  I built a way to track gigs, to add ranks (small groups) with a section, a way to track notes to directors, and a way for the leadership team to record reviews of student performance over time.  Everything at its lowest form links back to a season though, and that simple fact keeps the tool clean.

# Movement IV - Turning it On:

After the first two months or so of development most of the base features had been built.  I had a functioning model and I had developed a way to expand the tool quickly.  Because I spent so much time focusing on the database structure I avoided a lot of pitfalls that could have caught me up later on.  No matter how clean the tool was though, if it only ran on localhost on my laptop; that wouldn't really accomplish anything.

This tool was designed for use at Purdue by Purdue students, so it makes sense to host it at Purdue, right? Well that was what I tried first.  The old tool is hosted on iTap webhosting (which brings its own slew of problems) and I contacted them first.  It turns out that no one else has asked iTap for Rails hosting, or if they wanted Rails hosting they simply set up a box and did it themselves.  I was told quite simply that they did not have the tools to host the new version of the site, but if Purdue Bands and Orchestras paid for the development, their staff could look into the feasibility of hosting a site for us.

After hearing such an absurd invitation, I turned to ECN.  ECN advertises Rails hosting, and they seemed to have all of the things we would need.  And it would allow all of the data to be kept in house! A perfect situation.  Unfortunately ECN and iTap are not friendly organizations.  After being given the opportunity to pay for the development of iTap services, I was told that ECN could not do anything for us because iTap owns the site.  I was now in a situation where really nothing could be done.  One organization didn't have the ability, and for bureaucratic reasons the one that did could not work with us.  The only other option was external hosting.  Personally, I was in favor of this option because it allows me to maintain access after I graduate and keep working on my tool, but that's beside the point.

My first real test was with a hosting company called Ninefold.  It was excellent.  Great service, awesome performance, practically free hosting.  Ninefold met every need that existed, and for a price that the band department would accept without question.  (Free)  I had to be able to argue that my new tool would be a large enough improvement to justify an expense that hadn't existed with the original version.  After launching the site, and demoing it to some of the band staff and student department heads, I decided to ask a Ninefold staff member a performance question.  Instead of answering the question I was told that they were closing all US operations and had the chat window closed on me.  An email later in the week confirmed it, and I was back at ground zero.

I have used Heroku for a number of personal projects, but the quantity of data that the band website would require would quickly surpass the limits of the free rails hosting.  The next iterations was a full setup between a Heroku front-end and an AWS backend.  I was horribly mistaken in my expectation of how both services would play together.  The performance was terrible.  Basic parts of the site timed out, and it was immediately clear that AWS was not a viable long term solution with the setup I was using.  I don't really understand why this is, especially with Heroku living within AWS, but trouble-shooting it extensively is beyond me.

The final iteration was going back to Heroku and just paying for more space.  10 million rows is only $9 a month.  I'm not a fan of a limited number of rows, but at the current size and rate of usage it's 100s of years before that limit would be reached.  I had wanted to make it free if possible, but in the end it was clear that some services just need to be paid for.  Shortly after making that decision I had the website online and functioning.

# Movement V - Cleaning it Up:

Regardless of how many features a site has if it works slowly no one will want to use it.  The ultra clean code (minimalistic, not efficient) that I wrote generated a disgusting number of queries.  After getting everything online I had a small subset of the band leadership team lined up to do beta testing for me.  The only found one real bug, but noticed poor performance all across the site.  I had been testing with small sets of data, and had completely forgotten about scalability testing.

In the end, I was able to speed most of the slow pages up by over 300% and get the site into a much safer state.  Some of the pages are still slow, but parts of that are a limitation of the hosting services.  To save money, the band is only paying for one dyno, which means that I cannot add background workers to make the front-end more responsive.  Regardless though, the tool was quickly changed from a functioning system to one that functioned well.

Over the weeks since then I have continually iterated over my original model.  Buttons have been moved, features have been added, and small changes in the overall form and function have been done all across the website.  Without the testing that the leadership team has done, and without the original design Doug laid out, my current iteration of the tool would not exist.

# Movement IV - The End:

It has been a long road.  The first commit was made on Dec 23rd, 2014.  I took it easy over Christmas Break, but throughout this semester I have averaged 15+ hours a week of development.  I have poured all of my energy into this tool and am extremely proud of the final product.  I'm sure there is room for improvement, and I am sure that I missed some things, but without a doubt I have created something that has the potential to improve life within Purdue Bands.  I've had an incredible time at Purdue, and am hoping that this tool can live as my legacy, at least for a few years.  This was my opportunity to give back.

Ever grateful, ever true.  All Hail to our old Gold and Black!

--Nathan

<hr>

Check out the Code: [Online Toolbox \| GitHub](https://github.com/Tornquist/onlinetoolbox)

# Some Photos:

{% include photos.html
  height="25" id="online-toolbox-1"
  img1="/assets/2015/05/OnlineToolbox_2.png"
  img2="/assets/2015/05/OnlineToolbox_3.png"
%}
{% include photos.html
  height="13" id="online-toolbox-2"
  img1="/assets/2015/05/OnlineToolbox_5.png"
  img2="/assets/2015/05/OnlineToolbox_6.png"
  img3="/assets/2015/05/OnlineToolbox_7.png"
  img4="/assets/2015/05/OnlineToolbox_8.png"
%}
{% include photos.html
  height="13" id="online-toolbox-3"
  img1="/assets/2015/05/OnlineToolbox_9.png"
  img2="/assets/2015/05/OnlineToolbox_10.png"
  img3="/assets/2015/05/OnlineToolbox_11.png"
  img4="/assets/2015/05/OnlineToolbox_12.png"
%}

# (Semi-Complete) Feature List:

- Student Data
  - (Improved) Claimed Students
  - (Improved) Unclaimed Students
  - (Improved) Student Import
  - (New) Flexible Filters
  - (New) Rank/Section/Season Breakdowns
  - (New) Custom Search
  - (New) Flexible Forms
  - (New) CSV/PDF/Clipboard Export
- Gigs
  - (Improved) Transparency/Assignment
  - (New) Scheduling/Timeline
  - (New) Accountability
- GDS
  - (Improved) Assign GDS
  - (Improved) GDS Duty Assignment
  - (New) Custom Gameday Schedules
  - (New) Automatic GDS Alerts
  - (New) Email List Generation
- Seasons
  - (New) Perpetual Data
  - (New) Transfer Students
  - (New) Section Configuration
  - (New) Live Statistics
  - (New) Game Customization
- Sections
  - (Improved) Section Recruitment Notes
  - (New) Full Rank Configuration
- (New) Favorites
- (New) Help Documentation System
- (New) Announcement System
- (New) Internal User Management
  - Privilege Levels (Extended)
  - Full Administrative Panel
- (New) Extensive Online Administrative Portal
  - Recruit Status
  - Contact Type
  - Fields
  - Instrument Configuration
  - Ensemble Configuration
- (New) Accountability
  - Tracks Notes
  - Tracks Scoring of Students
  - Tracks Comments
  - Tracks Claimed/Unclaimed Students
  - Tracks Sign in Date/Time
  - Displays Above Information to All Users
    - No excuses for failure to recruit
- (New) Full Flexible CSV Import
  - Intermediate Data Validation
  - Auto-Import into Queue
- (New) 100% Live and Transparent
- (New) Full Mobile Support
