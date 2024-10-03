---
layout: page
title: Detailed Program
description: Detailed schedule of the program.
priority: 10
invisible: true
published: false
---

* Our [**virtual conference site**](https://pheedloop.com/rss2020/virtual/)
hosts all live events, allows users to flexibly join workshops and
paper discussion sessions, interact with each other and sponsors, and
manages registration.
* All [**accepted papers with pre-recorded presentations**]({{site.baseurl}}/program/papers/) are now available.
* Our [**RSS youtube channel**](https://www.youtube.com/channel/UCeEbAUGjtBlzmqWO5u6VeGg) hosts all pre-recorded presentations, and will host recordings of the
live plenary sessions.
* Please find the [**workshop program**]({{site.baseurl}}/program/workshops/) separately.
* The schedule is also available as [**shared Google Calendar**](https://calendar.google.com/calendar?cid=dDBoN2ltZGx2YnNyYmRocnYxZjgwYTdhcThAZ3JvdXAuY2FsZW5kYXIuZ29vZ2xlLmNvbQ) and its [**ical link**](https://calendar.google.com/calendar/ical/t0h7imdlvbsrbdhrv1f80a7aq8%40group.calendar.google.com/public/basic.ics).

### Overview


<img src="{{ site.baseurl }}/images/schedule-crop.jpg"
       alt="Virtual Event Schedule" width = "700" /> 


<br/>

<center>
  <a class="btn btn-primary" href="#tue" role="button">Tuesday</a>
  <a class="btn btn-primary" href="#wed" role="button">Wednesday</a>
  <a class="btn btn-primary" href="#thu" role="button">Thursday</a>
</center>

<br/>

All times below are given in **Coordinated Universal Time (UTC)**.

### Additional live Q&A sessions in Eastern time zones on the following day

All **plenary sessions will be recorded** and made freely available on
youtube. For those that cannot join the talks live, they can watch them the
next day and join a live Q&A session with the speakers on the
following day. This concerns the Test of Time talk (ToT), the three
Early Career Award talks (EC1-3), and the Keynote talk.



<a name="tue">&nbsp;</a>

### Tuesday, July 14

<table class="table table-striped table-program">
  <tr>
    <td width="140px">14:30 - 15:00 UTC</td>
    <td>
      <b>Welcome & Paper Nominations</b> <a href="https://pheedloop.com/rss2020/virtual/#session_EykIMu" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>

      <br/>Marc Toussaint, Jens Kober, Tim Barfoot, Hadas Kress-Gazit
    </td>
  </tr>
  <tr>
    <td width="140px">15:00 - 17:00 UTC</td>
    <td>
      <b>Live Paper Discussions #1-34 (<a href="../papers/">SEARCH PAPERS BY AUTHOR/TITLE</a>)</b> 
	  <br/>
	  <div style="font-size:90%;">
	  {% for paper in site.data.CameraReadyIntegration %}
	  {% assign tmp = paper.PaperId | plus: 0 %}
      {% if tmp < 35 %}
	  #{{tmp}}
	  <a href="{{site.baseurl}}/program/papers/{{paper.PaperId}}/" title="paper details">{{paper.PaperTitle}}</a>
	  <!--
	  <a href="http://www.roboticsproceedings.org/rss16/p{{paper.PaperIdZeros}}.pdf" title="pdf" style="color:#4040a0;">[pdf]</a>
	  <a href="https://www.youtube.com/watch?v={{paper.YouTube}}" title="Pre-recorded Presentation on Youtube" style="color:#4040a0;">[talk]</a>
	  -->
	  <a href="{{paper.deeplink}}" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
	  <br/>
      {% endif %}
	  {% endfor %}
	  </div>
    </td>
  </tr>
  <tr>
    <td width="140px">17:00 - 17:45 UTC</td>
    <td>
      <b><a href="{{site.baseurl}}/program/testoftimeaward/">Test of Time Award Talk + Q&A</a></b> <a href="https://pheedloop.com/rss2020/virtual/#session_fAlqAe" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Speakers: Frank Dellaert, Michael Kaess
      <br/>Moderator: Marc Toussaint
	  <br/>Title: <i>From Square Root SAM to GTSAM: Factor Graphs in Robotics</i>
    </td>
  </tr>
  <tr>
    <td width="140px">17:45 - 18:15 UTC</td>
    <td>
      <b>Test of Time Panel Debate</b> <a href="https://pheedloop.com/rss2020/virtual/#session_yIjewU" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Panelists: Frank Dellaert, Michael Kaess, Danica Kragic, Gaurav Sukhatme
	  <br/>Moderator: Marc Toussaint
    </td>
  </tr>
  <tr>
    <td width="140px">18:30 - 19:15 UTC</td>
    <td>
      <b><a href="{{site.baseurl}}/program/careerawards/">Early Career Award Keynote + Q&A</a></b> <a href="https://pheedloop.com/rss2020/virtual/#session_uCoRvD" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Speaker: Byron Boots
      <br/>Moderator: Marco Pavone
      <br/>Title: <i>Perspectives on Machine Learning for Robotics </i>
    </td>
  </tr>
</table>

<a name="wed">&nbsp;</a>

### Wednesday, July 15

<table class="table table-striped table-program">
  <tr>
    <td width="140px">14:00 - 15:00 UTC</td>
    <td>
      <b><a href="https://sites.google.com/view/inclusion-2020/program">Inclusion@RSS hosts: Future of Robotics Panel</a></b> <a href="https://pheedloop.com/rss2020/virtual/#meetup_EXH4762FMEQSK7AXN" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Moderators: Matthew Johnson-Roberson
    </td>
  </tr>
  <tr>
    <td width="140px">15:00 - 17:00 UTC</td>
    <td>
      <b>Live Paper Discussions #35-69 (<a href="../papers/">SEARCH PAPERS BY AUTHOR/TITLE</a>)</b>
	  <br/>
	  <div style="font-size:90%;">
	  {% for paper in site.data.CameraReadyIntegration %}
	  {% assign tmp = paper.PaperId | plus: 0 %}
      {% if tmp >= 35 and tmp < 70 %}
	  #{{tmp}}
	  <a href="{{site.baseurl}}/program/papers/{{paper.PaperId}}/" title="paper details">{{paper.PaperTitle}}</a>
	  <!--
	  <a href="http://www.roboticsproceedings.org/rss16/p{{paper.PaperIdZeros}}.pdf" title="pdf" style="color:#4040a0;">[pdf]</a>
	  <a href="https://www.youtube.com/watch?v={{paper.YouTube}}" title="Pre-recorded Presentation on Youtube" style="color:#4040a0;">[talk]</a>
	  -->
	  <a href="{{paper.deeplink}}" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
	  <br/>
      {% endif %}
	  {% endfor %}
	  </div>
    </td>
  </tr>
  <tr>
    <td width="140px">17:00 - 18:00 UTC</td>
    <td>
      <b><a href="{{site.baseurl}}/program/keynote/">Keynote + Q&A</a></b> <a href="https://pheedloop.com/rss2020/virtual/#session_JKGGgV" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Speaker: Josh Tenenbaum
      <br/>Moderator: Marc Toussaint
      <br/>Title: <i>It's all in your head: Intuitive physics, planning, and problem-solving in brains, minds and machines</i>

    </td>
  </tr>
  <tr>
    <td width="140px">18:00 - 18:30 UTC</td>
    <td>
      <b>Virtual Meetups</b>
    </td>
  </tr>
  <tr>
    <td width="140px">18:30 - 19:15 UTC</td>
    <td>
      <b><a href="{{site.baseurl}}/program/careerawards/">Early Career Award Keynote + Q&A</a></b> <a href="https://pheedloop.com/rss2020/virtual/#session_EIhCLO" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Speaker: Luca Carlone
      <br/>Moderator: Angela Schoellig
      <br/>Title: <i>The Future of Robot Perception: Certifiable Algorithms and Real-time High-level Understanding</i>
    </td>
  </tr>
</table>

<a name="thu">&nbsp;</a>

### Thursday, July 16

<table class="table table-striped table-program">
  <tr>
    <td width="140px">14:15 - 15:00 UTC</td>
    <td>
      <b>Discussion & Town Hall Meeting</b> <a href="https://pheedloop.com/rss2020/virtual/#session_VbWoLC" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Hadas Kress-Gazit, Antonio Bicchi, Marc Toussaint
    </td>
  </tr>
  <tr>
    <td width="140px">15:00 - 17:00 UTC</td>
    <td>
      <b>Live Paper Discussions #70-103 (<a href="../papers/">SEARCH PAPERS BY AUTHOR/TITLE</a>)</b>
	  <br/>
	  <div style="font-size:90%;">
	  {% for paper in site.data.CameraReadyIntegration %}
	  {% assign tmp = paper.PaperId | plus: 0 %}
      {% if tmp >= 70 %}
	  #{{tmp}}
	  <a href="{{site.baseurl}}/program/papers/{{paper.PaperId}}/" title="paper details">{{paper.PaperTitle}}</a>
	  <!--
	  <a href="http://www.roboticsproceedings.org/rss16/p{{paper.PaperIdZeros}}.pdf" title="pdf" style="color:#4040a0;">[pdf]</a>
	  <a href="https://www.youtube.com/watch?v={{paper.YouTube}}" title="Pre-recorded Presentation on Youtube" style="color:#4040a0;">[talk]</a>
	  -->
	  <a href="{{paper.deeplink}}" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
	  <br/>
      {% endif %}
	  {% endfor %}
	  </div>
    </td>
  </tr>
  <tr>
    <td width="140px">17:00 - 17:45 UTC</td>
    <td>
      <b><a href="{{site.baseurl}}/program/careerawards/">Early Career Award Keynote + Q&A</a></b> <a href="https://pheedloop.com/rss2020/virtual/#session_NgJTmi" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Speaker: Jeannette Bohg
      <br/>Moderator: Stefanie Tellex
      <br/>Title: <i>A Tale of Success and Failure in Robotics Grasping and Manipulation</i>
    </td>
  </tr>
  <tr>
    <td width="140px">18:00 - 18:45 UTC</td>
    <td>
      <b>Paper Awards & Farewell</b> <a href="https://pheedloop.com/rss2020/virtual/#session_kaLhOW" title="Pheedloop Virtual Session" style="color:#4040a0;" target="_blank">[session]</a>
      <br/>Tim Barfoot, Marc Toussaint
    </td>
  </tr>
</table>
