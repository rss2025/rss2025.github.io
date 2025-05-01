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

<!-- <style>
  :root {
    --google-blue-medium: #d2e3fc;   /* Medium-light blue */
    --google-green-medium: #c8e6c9;  /* Medium-light green */
    --google-red-medium: #f4c7c3;    /* Medium-light red */
    --google-gray-300: #e0e0e0;      /* Slightly darker gray */
    --google-gray-100: #f1f3f4;      /* Light gray for date */
    --google-black: #000000;
  }

  .date-block {
    background-color: var(--google-gray-100);
    color: var(--google-black);
    font-weight: bold;
  }

  .session-block {
    background-color: var(--google-blue-medium);
    color: var(--google-black);
  }

  .keynote-block {
    background-color: var(--google-red-medium);
    color: var(--google-black);
  }

  .break-block {
    background-color: var(--google-green-medium);
    color: var(--google-black);
  }

  .workshop-block {
    background-color: var(--google-gray-300);
    color: var(--google-black);
  }

  .highlight-block {
    background-color: var(--google-blue-medium);
    color: var(--google-black);
  }
</style> -->

<style>
  :root {
    --modern-indigo: #e0e7ff;
    --modern-soft-gold: #fef9c3;
    --modern-deep-red: #dc2626;
    --modern-soft-red: #fcd5ce;
    --modern-vibrant-orange: #fdba74;
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

  .keynote-block {
    background-color: var(--modern-deep-red);
    color: white;
  }

  .speaker-block {
    background-color: var(--modern-vibrant-orange);
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
</style>


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
              <!-- <td rowspan="19" class="workshop-block">RSS Pioneers</td> -->
              <td rowspan="19" class="workshop-block">
              <a href="{{ site.baseurl }}/program/pioneers/">RSS Pioneers</a>
              </td>
              <!-- <td rowspan="7" class="workshop-block">Workshops + RSS Pathways</td> -->
              <td rowspan="7" class="workshop-block">
              <a href="{{ site.baseurl }}/program/workshops/">Workshops</a> + <a href="{{ site.baseurl }}/program/pathways/">RSS Pathways</a>
              </td>
              <td rowspan="3" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=4.+Perception">4. Perception</a>
              </td>
              <td rowspan="3" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=9.+HRI">9. HRI</a>
              </td>
              <td rowspan="1" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=14.+Robot+Design">14. Robot Design</a>
              </td>
              <!-- <td rowspan="19" class="workshop-block">Workshops + Tours</td> -->
              <td rowspan="19" class="workshop-block">
              <a href="{{ site.baseurl }}/program/workshops/">Workshops</a> + Tours
              </td>
              <td style="display:none;">&nbsp;</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">9:30AM</td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=15.+Navigation">15. Navigation</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">10:00AM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">10:30AM</td>
              <td rowspan="1" class="break-block">Break + Posters Setup</td>
              <td rowspan="1" class="break-block">Break + Posters Setup</td>
              <td rowspan="1" class="break-block">Break + Posters Setup</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">11:00AM</td>
              <td rowspan="1" class="keynote-block">Early Career Spotlight</td>
              <td rowspan="1" class="keynote-block">Early Career Spotlight</td>
              <td rowspan="1" class="keynote-block">Awards Ceremony</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">11:30AM</td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=5.+Planning">5. Planning</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=10.+Multi-Robot+Systems">10. Multi-Robot Systems</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=16.+Manipulation+III">16. Manipulation III</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">12:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">12:30PM</td>
              <td rowspan="2" class="break-block">Welcome Reception Lunch + Poster Setup</td>
              <td rowspan="3" class="break-block">Lunch + Posters</td>
              <td rowspan="3" class="break-block">Lunch + Posters</td>
              <td rowspan="3" class="break-block">Lunch + Posters</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">1:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">1:30PM</td>
              <td rowspan="1" class="break-block">Opening address</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">2:00PM</td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=1.+Perception+and+Navigation">1. Perception and Navigation</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=6.+Manipulation+I">6.<br>Manipulation I</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=11.+Manipulation+II">11.<br>Manipulation II</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=17.+Imitation+Learning+II">17. Imitation Learning II</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">2:30PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">3:00PM</td>
              <!-- <td rowspan="2" class="keynote-block">Keynote: Barbara Webb</td> -->
              <td rowspan="2" class="speaker-block">
              <a href="{{ site.baseurl }}/program/keynote/" style="color: black">Keynote: Barbara Webb</a>
              </td>
              <td rowspan="2" class="keynote-block">Past, Present, and Future Panel</td>
              <!-- <td rowspan="2" class="keynote-block">Keynote: Trevor Darrell</td> -->
              <td rowspan="2" class="speaker-block">
              <a href="{{ site.baseurl }}/program/keynote/" style="color: black;">Keynote: Trevor Darrell</a>
              </td>
              <td rowspan="2" class="keynote-block">Test of Time Award</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">3:30PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">4:00PM</td>
              <td rowspan="1" class="break-block">Break</td>
              <td rowspan="1" class="break-block">Break</td>
              <td rowspan="1" class="break-block">Break</td>
              <td rowspan="3" class="break-block">Break + Posters + Tours</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">4:30PM</td>
              <!-- <td rowspan="2" class="session-block">2. VLA Models</td>
              <td rowspan="2" class="session-block">7. Humanoids</td>
              <td rowspan="2" class="session-block">12. Control and Dynamics</td> -->
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=2.+VLA+Models">2. VLA Models</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=7.+Humanoids">7. Humanoids</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=12.+Control+and+Dynamics">12. Control and Dynamics</a>
              </td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">5:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">5:30PM</td>
              <!-- <td rowspan="2" class="session-block">3. Scaling Robot Learning</td>
              <td rowspan="2" class="session-block">8. Imitation Learning I</td>
              <td rowspan="2" class="session-block">13. Mobile Manipulation and Locomotion</td> -->
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=3.+Scaling+Robot+Learning">3. Scaling Robot Learning</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=8.+Imitation+Learning+I">8. Imitation Learning I</a>
              </td>
              <td rowspan="2" class="session-block">
              <a href="{{ site.baseurl }}/program/papersession/?session=13.+Mobile+Manipulation+and+Locomotion">13. Mobile Manipulation and Locomotion</a>
              </td>
              <td rowspan="2" class="break-block">Town Hall</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">6:00PM</td>
       </tr>
       <tr>
              <td style="background-color: #E2F0D950;">6:30PM</td>
              <td rowspan="3"  style="box-shadow: none;"></td>
              <td rowspan="3" class="break-block">RoboNight: Dinner + Posters</td>
              <td rowspan="3" class="break-block">RoboNight: Dinner + Posters</td>
              <td rowspan="3" class="break-block">RoboNight: Dinner + Posters</td>
              <td rowspan="3" class="break-block">Farewell Drinks</td>
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



