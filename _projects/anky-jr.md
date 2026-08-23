---
title: "Catbot: Capstone Prototype"
excerpt: "Prototype of my capstone senior project built in the first half of the course to outline Anky Senior's ROS2 and electrical architecture."
order: 2
img: anky-jr/catbot.jpg
img-position: 50% 50%  # e.g. "30% 70%" to nudge proportionally, or "left 20px top 10px" for an exact pixel offset
---
<div class="section-header" markdown="1">
**Personal Project — Completed March 2026**
</div>

A prototype of my capstone project, built to be a proof of concept for [Anky](/projects/bring-roar-to-life/) before committing 
to the full-scale robot. I built this entirely on my own, outside of the team's official senior design work, so that the controls 
and electrical architecture for the full robot would already be planned out and working plus it served as a fallback to guarantee 
the team would still have a functioning robot even if my reinforcement learning model didn't pan out in time.
<br>
**Project goals:**
- Establish the ROS2 node architecture and communication method that Anky would later inherit.
- Prototype the electrical wiring and power delivery scheme for the leg servos and sensors.

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/matlab_gait_example.mp4" type="video/mp4">
</video>
- MATLAB's Robot Toolbox was used to compute and visualize the inverse kinematics trajectory for each leg.
- This let me validate the gait pattern and end effector trajectories before deploying it to hardware.
- The order of leg motion, the size of each step, and the gait duty factor are all parameterized to quickly be able to change the gait type.
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/anky-jr/catbot_rqt.jpg" style="width: 500px;">
- The ROS2 architecture routes a spoken command through a `/speech_recognizer` node on the Raspberry Pi, to the MATLAB joint solver, and back to the Pi.
- `/serial_bridge` passed the resulting servo commands from ROS2 to an Arduino, which drove the leg servos directly
- This became the foundation of the pipeline that later became capstone project's voice-teleoperation structure.
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 400px;">
<source src="/assets/video/catbot_walking_simple.mp4" type="video/mp4">
</video>
- This is the first test of the IK-driven gait, the joint commands were computed in MATLAB, and passed to the joints over ROS2. 
- This test confirmed the leg trajectories translated correctly from the MATLAB simulation into real servo motion.
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/anky-jr/catbot_wiring.jpg" style="width: 500px;">
- The electrical architecture used an Arduino Uno to drive the leg servos, with a Raspberry Pi handling higher-level compute and a variable DC power supply providing servo power separately to the logic and servos.
- This wiring scheme became the baseline for my capstone project's electrical design.
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted controls playsinline preload="none" style="width: 500px;">
<source src="/assets/video/catbot_walking_full_demo.mp4" type="video/mp4">
</video>
- Full end-to-end demo: a spoken "Hey Anky" command triggers the ROS2 speech recognizer, which triggers MATLAB to compute an joint-space trajectory
  and sends the trajectory back to the Pi which sends it to the Arduino over serial.
- Saying "Hey Anky, Stop" interrupts the gait mid-stride, confirming the voice-controlled stop command worked in real time.
- The final version had control for speed, and gait type but did not incorporate an IMU for stabalization.
</div>
