---
layout: page
title: Overview
description: Overview of the program
priority: 12
invisible: false
published: true
---

<style>
@media (max-width: 600px) {
  .schedule {
    display: table !important;
    width: 100% !important;
    overflow-x: auto;
  }
}
</style>

<style>
  :root {
    --modern-indigo: #e0e7ff;
    --modern-soft-gold: #fef9c3;
    --modern-deep-red: #dc2626;
    --modern-soft-red: #fcd5ce;
    --modern-faded-coral: #fcbaba;
    --modern-soft-orange: #fdeacc;
    --modern-date-light: #f1f5f9;
    --modern-warm-gray: #f5f5f4;
    --modern-sky-blue: #bae6fd;
    --modern-charcoal: #1f2937;
  }

  .date-block {
    background-color: var(--modern-date-light);
    color: var(--modern-charcoal);
    font-weight: bold;
  }

  .session-block {
    background-color: var(--modern-indigo);
    color: var(--modern-charcoal);
  }

  .event-block {
    background-color: var(--modern-faded-coral);
    color: var(--modern-charcoal);
  }

  .keynote-block {
    background-color: var(--modern-faded-coral);
    color: var(--modern-charcoal);
  }

  .break-block {
    background-color: var(--modern-soft-gold);
    color: var(--modern-charcoal);
  }

  .workshop-block {
    background-color: var(--modern-warm-gray);
    color: var(--modern-charcoal);
  }

  .highlight-block {
    background-color: var(--usc-gold);
    color: var(--modern-charcoal);
  }

  .block-link {
    display: flex;
    width: 100%;
    height: 100%;
    text-decoration: none;
    color: inherit;
    box-sizing: border-box;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
</style>

<!-- need for hover effect with blocks -->
<style>
  .schedule td {
    min-height: 40px !important;
    height: 40px !important;
    transition: background-color 0.2s ease, filter 0.2s ease;
  }

  .schedule td:hover {
    filter: brightness(1.2);
    cursor: pointer;
  }
</style>

<!-- needed for hover effect with multiple links in block -->
<style>
  /* Default: look like normal text */
  .schedule td a {
    color: inherit;
    text-decoration: none;
    transition: color 0.15s ease, text-decoration 0.15s ease;
  }

  /* When hovering over the cell, make links blue */
  .schedule td:hover a {
    color: #0000EE;
  }

  /* When hovering over the actual link text, add underline */
  .schedule td a:hover {
    text-decoration: underline;
  }
</style>

<div style="display: flex; flex-direction: column; gap: 1em; margin-bottom: 2em;">

  <div style="background-color: var(--modern-warm-gray); padding: 1em 1.2em; border-radius: 6px;">
    <strong>RSS Pioneers, Pathways@RSS, and Workshops:</strong>
    <ul style="margin: 0.5em 0 0 1em; padding: 0;">
      <li>Poster sessions of all workshops will take place at <a href="https://maps.app.goo.gl/YTtHP12vrTdBQpce9">Epstein Family Plaza</a>.</li>
      <li>For workshop locations, see the <a href="{{ site.baseurl }}/program/workshops/">Workshops</a> page.</li>
      <li><a href="{{ site.baseurl }}/program/pathways/">Pathways@RSS</a>  will take place in Room 115 at <a href="https://maps.app.goo.gl/ceZrio6J48qrKjR2A">Ronald Tutor Hall (RTH)</a>.</li>
      <li><a href="{{ site.baseurl }}/program/pioneers/">RSS Pioneers</a> will take place in Room 132 at <a href="https://maps.app.goo.gl/RNc715bRFr9B4Zn96">Olin Hall of Engineering (OHE)</a>.</li>
    </ul>
  </div>

  <div style="background-color: var(--modern-soft-gold); padding: 1em 1.2em; border-radius: 6px;">
    <strong>Posters and Demos:</strong>
    <ul style="margin: 0.5em 0 0 1em; padding: 0;">
      <li>Poster sessions of the main conference and the demos will take place at <a href="https://maps.app.goo.gl/Hno98qim4BKMVFc59">Associates Park</a>.</li>
      <li>Poster sessions of the workshops will take place at <a href="https://maps.app.goo.gl/YTtHP12vrTdBQpce9">Epstein Family Plaza</a>.</li>
    </ul>
  </div>

  <div style="background-color: #e8f5e9; padding: 1em 1.2em; border-radius: 6px;">
    <strong>Main Conference Events:</strong>
    <ul style="margin: 0.5em 0 0 1em; padding: 0;">
       <li>The <a href="{{ site.baseurl }}/attending/social/">social events</a> (RoboNight and Farewell Reception) and lunches will take place at <a href="https://maps.app.goo.gl/KBvJUBtyXxn319QG8">Founders Park</a>.</li>
	   <li>The short coffee breaks will take place at the entrance of <a href="https://maps.app.goo.gl/gmsxcUqwNSfjsuHL8">Bovard Auditorium</a>.</li>
      <li>All other events of the main conference (keynotes, panels, early career spotlights, and awards) will take place at <a href="https://maps.app.goo.gl/gmsxcUqwNSfjsuHL8">Bovard Auditorium</a>.</li>
    </ul>
  </div>

</div>

---

<table class="schedule" cellspacing="0" border="0">
       <tr>
              <td style="width: 5em; border: none; background-color: #E2F0D9;"></td>
              <td class="date-block" style="width: 16%;">June 20<br>Friday</td>
              <td class="date-block" style="width: 16%;">June 21<br>Saturday</td>
              <td class="date-block" style="width: 16%;">June 22<br>Sunday</td>
              <td class="date-block" style="width: 16%;">June 23<br>Monday</td>
              <td class="date-block" style="width: 16%;">June 24<br>Tuesday</td>
              <td class="date-block" style="width: 16%;">June 25<br>Wednesday</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">9:00AM</td>
              <td rowspan="19" class="workshop-block">
              <a class="block-link" href="{{ site.baseurl }}/program/pioneers/">RSS Pioneers</a>
              </td>
              <td rowspan="7" class="workshop-block">
              <a href="{{ site.baseurl }}/program/workshops/">Workshops</a> + <a href="{{ site.baseurl }}/program/pathways/">RSS Pathways</a>
              </td>
              <td rowspan="3" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=4.+Perception">4. Perception</a>
              </td>
              <!-- <td rowspan="3" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=9.+HRI">9. HRI</a>
              </td> -->
              <td rowspan="3" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=9.+HRI">9. HRI</a>
              </td>
              <td rowspan="1" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=14.+Robot+Design">14. Robot Design</a>
              </td>
              <!-- <td rowspan="19" class="workshop-block" style="text-align: center; vertical-align: middle;">
              <a href="{{ site.baseurl }}/program/workshops/">Workshops</a>
              </td> -->
              <td rowspan="19" class="workshop-block">
              <a class="block-link" href="{{ site.baseurl }}/program/workshops/">Workshops</a>
              </td>
              <td style="display:none;">&nbsp;</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">9:30AM</td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=15.+Navigation">15. Navigation</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">10:00AM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">10:30AM</td>
              <!--
              <td rowspan="1" class="break-block">Coffee Break  + Posters Setup</td>
              <td rowspan="1" class="break-block">Coffee Break  + Posters Setup</td>
              <td rowspan="1" class="break-block">Coffee Break  + Posters Setup</td>
              -->
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break  + Posters Setup</a>
              </td>
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break  + Posters Setup</a>
              </td>
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break  + Posters Setup</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">11:00AM</td>
              <td rowspan="1" class="event-block">
              <a class="block-link" href="{{ site.baseurl }}/program/earlycareer/">Early Career Spotlight:<br>Dorsa Sadigh</a>
              </td>
              <td rowspan="1" class="event-block">
              <a class="block-link" href="{{ site.baseurl }}/program/earlycareer/">Early Career Spotlight:<br>Zac Manchester</a>
              </td>
              <td rowspan="1" class="event-block">Awards Ceremony</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">11:30AM</td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=5.+Planning">5. Planning</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=10.+Multi-Robot+Systems">10. Multi-Robot Systems</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=16.+Manipulation+III">16. Manipulation III</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">12:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">12:30PM</td>
              <!-- <td rowspan="2" class="break-block">Welcome Reception Lunch + Poster Setup</td> -->
              <td rowspan="2" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Welcome Reception Lunch + Poster Setup</a>
              </td>
              <!-- 
              <td rowspan="3" class="break-block">Lunch + Posters</td>
              <td rowspan="3" class="break-block">Lunch + Posters</td>
              <td rowspan="3" class="break-block">Lunch + Posters</td> 
              -->
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Lunch + Posters</a>
              </td>
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Lunch + Posters</a>
              </td>
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Lunch + Posters</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">1:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">1:30PM</td>
              <!-- <td rowspan="1" class="break-block">Opening address</td> -->
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Opening Remarks</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">2:00PM</td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=1.+Perception+and+Navigation">1. Perception and Navigation</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=6.+Manipulation+I">6.<br>Manipulation I</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=11.+Manipulation+II">11.<br>Manipulation II</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=17.+Imitation+Learning+II">17. Imitation Learning II</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">2:30PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">3:00PM</td>
              <td rowspan="2" class="keynote-block">
              <a class="block-link" href="{{ site.baseurl }}/program/keynote/">Keynote:<br>Barbara Webb</a>
              </td>
              <td rowspan="2" class="event-block">Past, Present, and Future Panel</td>
              <td rowspan="2" class="keynote-block">
              <a class="block-link" href="{{ site.baseurl }}/program/keynote/">Keynote:<br>Trevor Darrell</a>
              </td>
              <td rowspan="2" class="event-block">
              <a class="block-link" href="{{ site.baseurl }}/program/testoftimeaward/">Test of Time Award</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">3:30PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">4:00PM</td>
              <!--
              <td rowspan="1" class="break-block">Coffee Break</td>
              <td rowspan="1" class="break-block">Coffee Break</td>
              <td rowspan="1" class="break-block">Coffee Break</td>
              -->
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break</a>
              </td>
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break</a>
              </td>
              <td rowspan="1" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break</a>
              </td>
              <td rowspan="3" class="break-block">
              <a href="{{ site.baseurl }}/attending/social/">Coffee Break</a> +
              <a href="{{ site.baseurl }}/program/posters/">Posters</a> +
              <a href="{{ site.baseurl }}/program/labtours/">Tours</a>
              </td>
              <!-- <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Coffee Break + Posters + Tours</a>
              </td> -->
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">4:30PM</td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=2.+VLA+Models">2. VLA Models</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=7.+Humanoids">7. Humanoids</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=12.+Control+and+Dynamics">12. Control and Dynamics</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">5:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">5:30PM</td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=3.+Scaling+Robot+Learning">3. Scaling Robot Learning</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=8.+Imitation+Learning+I">8. Imitation Learning I</a>
              </td>
              <td rowspan="2" class="session-block">
              <a class="block-link" href="{{ site.baseurl }}/program/papersession/?session=13.+Mobile+Manipulation+and+Locomotion">13. Mobile Manipulation and Locomotion</a>
              </td>
              <td rowspan="2" class="break-block">Town Hall</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">6:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">6:30PM</td>
              <td rowspan="3"  style="box-shadow: none;"></td>
              <!-- 
              <td rowspan="3" class="break-block">RoboNight: Dinner + Posters</td>
              <td rowspan="3" class="break-block">RoboNight: Dinner + Posters</td>
              <td rowspan="3" class="break-block">RoboNight: Dinner + Posters</td>
              <td rowspan="3" class="break-block">Farewell Reception</td> 
              -->
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">RoboNight: Dinner + Posters</a>
              </td>
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">RoboNight: Dinner + Posters</a>
              </td>
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">RoboNight: Dinner + Posters</a>
              </td>
              <td rowspan="3" class="break-block">
              <a class="block-link" href="{{ site.baseurl }}/attending/social/">Farewell Reception</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">7:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">7:30PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">8:00PM</td>
       </tr>
</table>

---

<div style="text-align: center; margin: 3em auto;">
  <img src="{{ site.baseurl }}/images/local2025/usc_map.png"
       alt="Map of key RSS 2025 locations on the USC campus"
       style="max-width: 90%; height: auto; border-radius: 6px;">
  <div style="margin-top: 0.5em; font-size: 0.9em; color: #666;">
    Map of key RSS 2025 locations on the USC campus
  </div>
</div>