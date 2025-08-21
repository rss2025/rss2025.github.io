---
layout: default
title: Paper Sessions
description: Paper Sessions
priority: 11
invisible: true
published: true
---

<div class="page" id="inner-content">
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
  padding: 12px;
}

#myTable tr {
  border-bottom: 1px solid #ddd;
}

#myTable tr.header, #myTable tr:hover {
  background-color: #f1f1f1;
}
</style>

<div class="mini-paper-navbar" id="mini-session-navbar">
  <!-- we use JavaScript will populate this, see script #2 below -->
  <span style="visibility: hidden;"><i class="fa fa-chevron-left"></i>☰<i class="fa fa-chevron-right"></i></span>
</div>

<!-- <h1 class="page-title">{{ page.title }}</h1> -->
<h1 class="page-title" style="visibility: hidden;">{{ page.title }}</h1>
<br/>

<div style="width: 100%; text-align: center;">
<div style="width: 100%; text-align: center; margin-top: -20px;  margin-bottom: 15px;">
  <i id="chairedby"></i>
</div>
<div class="paper-authors">
<div class="paper-author-box">
    <div id="c1" class="paper-author-name"></div>
    <div id="c1a" class="paper-author-uni"></div>
</div>
<div class="paper-author-box">
    <div id="c2" class="paper-author-name"></div>
    <div id="c2a" class="paper-author-uni"></div>
</div>
</div>

<br>
<div id="session-datetime" style="margin-top: -6px; font-size: 0.95em; color: #555; text-align: center;"></div>
<hr>

<table id="myTable">
  <tr class="toprowHeader">
    <th>Order In Session</th>
    <th>Title</th>
    <th>Authors</th>
  </tr>
 {% for paper in site.data.rss2025CameraReadyInfo %}
 <tr session="{{ paper.SessionName }}">
    <td width="5%" height="100px">{{paper.OrderinSession }}</td>
    <!-- comment this for now to disable paper links -->
    <!-- <td width="45%" height="100px" ><a href="{{ site.baseurl }}/program/papers/{{ paper.PaperIDZeroes
}}/"><b>{{paper.PaperTitle}}</b></a></td> -->
    <!-- <td width="45%" height="100px"><b>{{ paper.PaperTitle }}</b></td> -->
    <td width="45%" height="100px">
      <a href="{{ site.baseurl }}/program/papers/{{ paper.PaperID }}/">
        <b>{{ paper.PaperTitle }}</b>
      </a>
    </td>
    <td width="40%" height="100px">{{ paper.AuthorNames | replace: ';', ',' | truncatewords: 40, "&nbsp;<button type='button' class='collapsible' style='border:none;background:none;font-size:smaller;color:#222299;'>...more&gt;</button>"}}
      <div class="content" style="display:none; padding-top:20px;">
        {{ paper.AuthorNames | replace: ';', ','}}
      </div>
    </td>
  </tr>
{% endfor %}
</table>

<br>
<!-- <div id="nav-button-container" style="display: flex; justify-content: space-between; margin-bottom: 10px;"></div> -->
<div class="paper-menu">
  <div class="paper-menu-inner" id="session-menu-inner">
    <!-- we use JavaScript will populate this, see script #2 below -->
  </div>
</div>
<br>

<script>
(function($) {
  $.QueryString = (function(a) {
    if (a == "") return {};
    var b = {};
    for (var i = 0; i < a.length; ++i) {
      var p = a[i].split('=');
      if (p.length != 2) continue;
      b[p[0]] = decodeURIComponent(p[1].replace(/\+/g, " "));
    }
    return b;
  })(window.location.search.substr(1).split('&'));
})(jQuery);

var $rows = $('#myTable tr');
$(document).ready(function() {
  //get the session name from the query string
  var sessionName = jQuery.QueryString["session"] || "";

  //use the session name to show/hide relevant rows
  $rows.hide().filter("tr[session='" + sessionName + "'],.toprowHeader").show();
  $(".page-title").text("Session " + sessionName).css("visibility", "visible");

  //look up session info from the YAML data
  var sessions = {{ site.data.rss2025PaperSessions | jsonify }};
  var sessionInfo = sessions.find(s => s.SessionName === sessionName);

  //set date, time, location
  if (sessionInfo) {
    var locationStr = '<a href="https://maps.app.goo.gl/gmsxcUqwNSfjsuHL8" target="_blank">Bovard Auditorium</a>';
    var dateTimeStr = "<strong>Date:</strong> " + sessionInfo.Day + ", " + sessionInfo.DateVerbose + ", 2025" +
                      " &nbsp; | &nbsp; <strong>Time:</strong> " + sessionInfo.Time +
                      " &nbsp; | &nbsp; <strong>Location:</strong> " + locationStr;
    $("#session-datetime").html(dateTimeStr);

    //populate chairs
    if (sessionInfo.C1 || sessionInfo.C2) {
      $("#chairedby").text("Chaired By");
      $("#c1").text(sessionInfo.C1 || "");
      $("#c1a").text(sessionInfo.C1A || "");
      $("#c2").text(sessionInfo.C2 || "");
      $("#c2a").text(sessionInfo.C2A || "");
    }
  }
});
</script>


<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    this.style.display = "none";
    var content = this.nextElementSibling;
    var c = this.parentElement;
    c.innerHTML = content.innerHTML;
    });
}
</script>

<!-- Script #1 to populate back/session/next buttons at top -->
<script>
document.addEventListener("DOMContentLoaded", function () {
  const sessions = {{ site.data.rss2025PaperSessions | jsonify }};
  const params = new URLSearchParams(window.location.search);
  const currentSessionName = decodeURIComponent(params.get("session"));
  const navTop = document.getElementById("mini-session-navbar");

  const currentIndex = sessions.findIndex(s => s.SessionName === currentSessionName);
  if (currentIndex === -1 || !navTop) return;

  function buildUrl(session) {
    const urlParams = new URLSearchParams({ session: session.SessionName });
    if (session.C1) urlParams.set("c1", session.C1);
    if (session.C1A) urlParams.set("c1a", session.C1A);
    if (session.C2) urlParams.set("c2", session.C2);
    if (session.C2A) urlParams.set("c2a", session.C2A);
    // return "/program/papersession?" + urlParams.toString();
    return "{{ site.baseurl }}/program/papersession?" + urlParams.toString();
  }

  const hasPrev = currentIndex > 0;
  const hasNext = currentIndex + 1 < sessions.length;

  const prev = document.createElement("a");
  prev.href = hasPrev ? buildUrl(sessions[currentIndex - 1]) : "#";
  prev.title = "Previous Session";
  prev.innerHTML = '<i class="fa fa-chevron-left"></i>';
  if (!hasPrev) {
    prev.style.visibility = "hidden";
  }
  navTop.appendChild(prev);

  const center = document.createElement("a");
  center.href = "{{ site.baseurl }}/program/allsessions";
  center.innerHTML = "☰";
  navTop.appendChild(center);

  const next = document.createElement("a");
  next.href = hasNext ? buildUrl(sessions[currentIndex + 1]) : "#";
  next.title = "Next Session";
  next.innerHTML = '<i class="fa fa-chevron-right"></i>';
  if (!hasNext) {
    next.style.visibility = "hidden";
  }
  navTop.appendChild(next);
});
</script>


<!-- Script #2 to populate back/session/next buttons at bottom -->
<script>
document.addEventListener("DOMContentLoaded", function () {
  const sessions = {{ site.data.rss2025PaperSessions | jsonify }};
  const params = new URLSearchParams(window.location.search);
  const currentSessionName = decodeURIComponent(params.get("session"));
  const container = document.getElementById("session-menu-inner");

  const currentIndex = sessions.findIndex(s => s.SessionName === currentSessionName);
  if (currentIndex === -1 || !container) return;

  function buildUrl(session) {
    const urlParams = new URLSearchParams({ session: session.SessionName });
    if (session.C1) urlParams.set("c1", session.C1);
    if (session.C1A) urlParams.set("c1a", session.C1A);
    if (session.C2) urlParams.set("c2", session.C2);
    if (session.C2A) urlParams.set("c2a", session.C2A);
    // return "/program/papersession?" + urlParams.toString();
    return "{{ site.baseurl }}/program/papersession?" + urlParams.toString();
  }

  function createSlotLink({ href = "#", iconClass = "", label = "", visible = true }) {
    const link = document.createElement("a");
    link.href = href;
    link.className = "paper-menu-icon";
    link.innerHTML = `<i class="fa ${iconClass}"></i><br><span class="paper-menu-label">${label}</span>`;
    if (!visible) {
      link.style.visibility = "hidden";
    }
    return link;
  }

  //back button (left)
  const hasPrev = currentIndex > 0;
  const prevLink = createSlotLink({
    href: hasPrev ? buildUrl(sessions[currentIndex - 1]) : "#",
    iconClass: "fa-arrow-left",
    label: "Back",
    visible: hasPrev
  });
  container.appendChild(prevLink);

  //sessions button (middle)
  const centerLink = createSlotLink({
    href: "{{ site.baseurl }}/program/allsessions",
    iconClass: "fa-list",
    label: "Sessions"
  });
  container.appendChild(centerLink);

  //next button (right)
  const hasNext = currentIndex + 1 < sessions.length;
  const nextLink = createSlotLink({
    href: hasNext ? buildUrl(sessions[currentIndex + 1]) : "#",
    iconClass: "fa-arrow-right",
    label: "Next",
    visible: hasNext
  });
  container.appendChild(nextLink);
});
</script>




<br/>
<br/>
<br/>
<br/>
<br/>
<center><footer style="color: lightslategray;">
  <small style="line-height: 95%;"><p style="padding-bottom: 2px; margin-bottom: 2px;">This page needs javascript to function.</p></small>
</footer>
</center>
</div>