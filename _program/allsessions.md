---
layout: page
title: Paper Sessions
description: List of Paper Sessions.
priority: 11
invisible: false
published: true
---
  
<style>
* {
  box-sizing: border-box;
}

#myTable {
  border-collapse: collapse;
  width: 100%;
  border: 1px solid #ddd;
  font-size: 100%;
}

#myTable th, #myTable td {
  text-align: left;
/*  padding: 12px;*/
  padding: 6px;
}

#myTable tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover {
  background-color: #f1f1f1;
}

</style>

Check the list of accepted papers <a href="{{ site.baseurl }}/program/papers/"><strong>[here]</strong></a>.

<!--
For information about the location of the sessions check out the [venue page]({{ site.baseurl }}/attending/atvenue/).
-->

<hr>

<table id="myTable">
  <tr class="toprowHeader">
    <th >Date</th>
    <th >Location</th>
    <th >Time</th>
    <th >Session Name and Chairs</th>
  </tr>
 {% for session in site.data.rss2025PaperSessions %}
  <tr session="{{ session.SessionName }}" style="border-bottom: none;">
    <td>{{ session.Date }}</td>
    <td>
      <a href="https://maps.app.goo.gl/gmsxcUqwNSfjsuHL8" target="_blank">Bovard Auditorium</a>
    </td>
    <td>{{ session.Time }}</td>
    <td>
      <a href="{{ site.baseurl }}/program/papersession?session={{ session.SessionName | url_encode }}">
      {{ session.SessionName }}
      </a>
    </td>
  </tr>
  <tr>
    <td style="padding-top: 0px;"></td>
    <td style="padding-top: 0px;"></td>
    <td style="padding-top: 0px;"></td>
    <td style="padding-top: 0px; font-size: smaller;">{{ session.C1 }}<br> <i>{{ session.C1A }}</i></td>
    <td style="padding-top: 0px; font-size: smaller;">{{ session.C2 }}<br> <i>{{ session.C2A }}</i></td>
  </tr>
  
{% endfor %}
</table>

