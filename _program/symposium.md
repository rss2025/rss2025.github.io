---
layout: page
title: Area Chair Symposium
description: Area chair symposium time and details.
invisible: true
published: false
---

{% comment %}
The RSS Area Chair Symposium will be held in 3305 Newell-Simon Hall at Carnegie Mellon University in
Pittsburgh, Pennsylvania, USA on April 6, 2017.

<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3036.4386202453593!2d-79.9456134!3d40.443428!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8834f2216b3de60b%3A0x9dc3e7773e241828!2sNewell-Simon+Hall!5e0!3m2!1sen!2sus!4v1490145373776" width="600" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>

## Program Summary

<table class="table">
    <tbody class="text-left">
      <tr>
        <td style="width: 130px">9:00 - 9:20 AM</td>
        <td>
          <b>Welcome and Overview</b> <br/>
          Aaron Johnson, Henny Admoni, and Sidd Srinivasa
        </td>
      </tr>
      <tr>
        <td>9:20 - 10:40 AM</td>
        <td>
          <b>New Sensors and Actuators</b> <br/>
          Akihiko Yamaguchi, Carnegie Mellon University, <a href="javascript:void($('#yamaguchi').toggle());"><i>Whole-Body Vision</i></a>
          <div id="yamaguchi" style="display:none;">
            <br/>
            We propose using cameras (as well as acceleromters, gyros, ...) to provide tactile and proximity sensing in robot skin. Following the principle that "Sensing Solves Robotics", covering an entire robot with cameras greatly simplifies robot control.
          </div>
          <br/>
          Robert Howe, Harvard University, <a href="javascript:void($('#howe').toggle());"><i>Achieving selective kinematics and stiffness in flexible robotics</i></a>
          <div id="howe" style="display:none;">
            <br/>
            We are working to create a new technology that allows robot structures to transition between soft and hard, based on “laminar jamming.” In its simplest form, thin sheets of a flexible material (e.g. ordinary printer paper) are stacked inside a plastic envelope. When the bag is connected to a vacuum pump, the layers are pressed together by the pressure of the surrounding air, and friction locks them together into a single stiff structure. Because the bending stiffness of a beam is proportional to its thickness to the third power, even a few laminae can produce dramatic increases in stiffness. These “jamming elements” can be integrated into soft robot actuators and structures, allowing controlled transitions between stiff and compliant behavior. This enables a number of useful capabilities. One example is variable kinematics: if a row of jamming actuators is embedded along the length of a soft bending actuator, they can stiffen to form rigid “links” separated by compliant joints, so the robot can switch between a continuously-bending tentacle and a jointed arm. Another example is shape-locking, which would hold the current shape of the actuator after power is removed. These elements can be combined to create a wide range of new robotic capabilities.
          </div>
          <br/>
          Ralph Hollis, Carnegie Mellon University, <a href="javascript:void($('#hollis').toggle());"><i>An Omnidirectional Mobile Robot with Just Two Moving Parts</i></a>
          <div id="hollis" style="display:none;">
            <br/>
            We discuss the design and operation of SIMbot, a ballbot mobile robot powered by a direct drive closed-loop spherical induction motor. Performance results are given, including comparison with a ballbot which employs a more conventional mechanical drive.
          </div>
          <br/>
          Matei Ciocarlie, Columbia University, <a href="javascript:void($('#ciocarlie').toggle());"><i>Senses and sensing ability for dexterous hands</i></a>
          <div id="ciocarlie" style="display:none;">
            <br/>
            I will present new results on sensors and sensing modalities for dexterous hands (including tactile and proprioceptive sensing), and new analysis of grasp quality metrics that make use of such data.
          </div>
        </td>
      </tr>
      <tr>
        <td>10:40 - 11:00 AM</td>
        <td>
          <b>Coffee Break</b>
        </td>
      </tr>
      <tr>
        <td>11:00 - 12:20 PM</td>
        <td>
          <b>Tasks and Autonomy</b> <br/>
          Todd Murphey, Northwestern University, <a href="javascript:void($('#murphey').toggle());"><i>From Coverage to Robot Art: Specifying Statistically-Defined Tasks</i></a>
          <div id="murphey" style="display:none;">
            <br/>
            This talk will focus on ergodicity-based task specification for robotic systems and how merging data-driven analysis and trajectory analysis yields a rich and computable paradigm in which tasks are represented as distributions. Examples include active shape estimation, rehabilitation/assistive technologies, and robotic drawing.
          </div>
          <br/>
          Nathan Michael, Carnegie Mellon University, <a href="javascript:void($('#michael').toggle());"><i>Efficient and Robust Autonomous Inspection in Cluttered and Confined Industrial Environments</i></a>
          <div id="michael" style="display:none;">
            <br/>
            Autonomous inspection in confined and cluttered environments requires planning, perception, and control strategies that are amenable to challenging and diverse environment and operation conditions. In this talk, we will present recent theoretic and systems developments to enable robust and precise autonomous inspection.
          </div>
          <br/>
          Justus Piater, University of Innsbruck, <a href="javascript:void($('#piater').toggle());"><i>Visual Task Outcome Verification Using Deep Learning</i></a>
          <div id="piater" style="display:none;">
            <br/>
            We recently developed a method allowing a robot to assert visually whether a manipulation has achieved the desired effect or not. If the answer is negative, it generates a corrective motion, bringing the manipulation closer to success.  Both outcome assessment and motion generation are done by deep CNNs, using training data automatically generated from very few real-world examples.
          </div>
          <br/>
          Matt Walter, Toyota Technological Institute at Chicago, <a href="javascript:void($('#walter').toggle());"><i>Learning to Follow (and Give) Natural Language Instructions in Unknown Environments</i></a>
          <div id="walter" style="display:none;">
            <br/>
            Natural language promises an efficient and flexible means for humans to communicate with robots, whether they are assisting the physically impaired, or performing disaster mitigation tasks as our surrogates. In this talk, I will describe our recent work developing end-to-end methods that enable robots to interpret free-form instructions in a priori unknown environments, without the need for specialized linguistic resources. If time allows, I will also talk about efforts to essentially invert this model in order to allow robots to generate natural language instructions.
          </div>
        </td>
      </tr>
      <tr>
        <td>12:20 - 1:40 PM</td>
        <td>
          <b>Lunch</b>
        </td>
      </tr>
      <tr>
        <td>1:40 - 2:40 PM</td>
        <td>
          <b>Assisting Humans</b> <br/>
          Steve Collins, Carnegie Mellon University, <a href="javascript:void($('#collins').toggle());"><i>Human-in-the-loop optimization of exoskeleton control</i></a>
          <div id="collins" style="display:none;">
            <br/>
            I would describe our recent big result (now in review at Science) tha automatically customizing exoskeleton assistance during walking and running under various conditions leads to huge improvements in performance. I would also admonish the field to stop doing crappy prosthetics and exoskeleton research, for example in which no human participants are involved.
          </div>
          <br/>
          Guy Hoffman, Cornell University, <a href="javascript:void($('#hoffman').toggle());"><i>A Wearable Robotic Forearm</i></a>
          <div id="hoffman" style="display:none;">
            <br/>
            We present the design and implementation of a wearable robotic forearm for close-range human-robot collaboration. We discuss usage scenarios, kinematics, bio-mechanical load analysis, and insights from three studies of people interacting with the robot.
          </div>
          <br/>
          Henny Admoni, Carnegie Mellon University, <a href="javascript:void($('#admoni').toggle());"><i>Assistive Robotics Using Natural Human Behavior</i></a>
          <div id="admoni" style="display:none;">
            <br/>
            Assistive robots must recognize human mental states---such as what people intend to do or where they need help---in order to provide effective assistance. People naturally express their mental states through their behavior, like eye gaze. Robots that detect, interpret, and respond to human behavior can provide better assistance.
          </div>
        </td>
      </tr>
      <tr>
        <td>2:40 - 3:00 PM</td>
        <td>
          <b>Coffee Break</b>
        </td>
      </tr>
      <tr>
        <td>3:00 - 5:00 PM</td>
        <td>
          <b>Discussion / Meetings / Free time / Run with Sidd</b>
        </td>
      </tr>
    </tbody>
</table>

{% endcomment %}