---
title: "Capstone Senior Project: Bring ROAR to Life \"Hey, Anky!\""
excerpt: "Physical-AI controlled 14-DOF quadrupedal dinosaur robot with reinforcement learning training and voice teleoperation."
order: 1
img: bring-roar-to-life/anky_insim.jpg
img-position: 40% 50%
---
<div class="section-header" markdown="1">
**Senior Capstone Project — Completed July 2026**
</div>
<div class="img-text-row img-text-row--reverse" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/bring-roar-to-life/team_photo.jpg" alt="ROAR capstone team" style="width: 250px;">
<video autoplay loop muted playsinline style="width: 250px;">
  <source src="/assets/video/reboot_sequence.mp4" type="video/mp4">
</video>
</div>
Anky is a low-cost physical AI deployment platform built from 3d printed parts, and hobby level electronics. 
The control algorithm is a machine learning model developed in Isaac Lab and inferenced by a ROS2 node running on a Raspberry Pi.
Built by a team of 5 mechanical engineers, it is by far the most exciting project I've worked on.
</div>

<div class="section-header" markdown="1">
**Control Architecture Lead:** Developed a machine learning policy and ROS2 nodes to control the robot.
</div>
  The video below shows the second generation Anky learning to walk over 6 thousand iterations (top right corner). Each iteration had 1024 individual robot environments which brings total amount of training instances to over 6 million. On a RTX 2070 laptop this took about 6 hours to film. 
  <div class="img-text-row" markdown="1">
  <video autoplay loop muted playsinline style="width: 400px;">
    <source src="/assets/video/training.mp4" type="video/mp4">
  </video>

  - The team's CAD assembly was converted to URDF format and imported to NVIDIA's Isaac Lab 3.0. 
  - This software is where we can write custom reward and penalty functions that "motivate" toward a certain goal.
  - Expected conditions can also be simulated. For example and in Anky's case the robot had a high magnitude impulse randomly induced in a random direction to teach it how to react to being pushed in real life. 
  </div>

  <div class="img-text-row img-text-row--reverse" markdown="1">
  <img src="/assets/img/projects/bring-roar-to-life/rqt_graph_horizontal.jpg" style="width: 1000px;">

  - An inference method for the RL policy represented by the blue ellipse, was developed to run via a ROS2 node. 
  - The rest of the ROS2 architecture is shown. On the left are the microphone and imu inputs, and on the right the servo command outputs.
  - The closed loop feedback for the leg joints relies on modified servos. I soldered in a wire to the internal potentiometer of each servo to read their feedback.
  </div>

  <div class="img-text-row" markdown="1">
  <video autoplay loop muted playsinline style="width: 500px;">
    <source src="/assets/video/siminloop.mp4" type="video/mp4">
  </video>
  - Isaac Sim sim-in-loop strategy was used to prove the functionality of my control architecture. 
  - Interoceptive readings were taken from a simulated IMU and encoders. Which were read by the trained model on a Raspberry Pi over ROS2, and the command thetas were then routed back to the sim.
  - This was completed before any purchace order was filed saving time and money by proving our design could work before fabrication began.
  </div>

  <div class="img-text-row img-text-row--reverse" markdown="1">
  <video autoplay loop muted playsinline style="width: 500px;">
    <source src="/assets/video/first_walking_test_wide.mp4" type="video/mp4">
  </video>
  - This video shows my first attempt at deploying the trained policy, my first time seeing what it can do on physical hardware.
  - Since the policy was trained entirely in simulation it had encountered a "walk forward" command millions of times and knew exactly what to do to execute it. 
  - On our first test we acheived our functional goals and all that remained was refinement.
  </div>

<div class="section-header" markdown="1">
**Electrical Design Lead:** Selected electronic components and designed power systems.
</div>
  <div class="img-text-row" markdown="1">
  <img src="/assets/img/projects/bring-roar-to-life/fritzing.jpg" alt="Electrical Diagram Here" style="width: 700px;">
  - Fabricated and tested protoboards which miniaturized the footprint of sensors and controllers.
  - Designed power delivery and power safety schema for all systems.
  </div>

  <div class="img-text-row" markdown="1">
  <video autoplay loop muted playsinline style="width: 400px;">
    <source src="/assets/video/test_exposed_wiring.mp4" type="video/mp4">
  </video>
  - Wired and bench-tested the robot's power and signal harness before final assembly.
  - Verified all connections were sound before the electronics were enclosed.
  </div>

  <div class="img-text-row" markdown="1">
  <!-- add the file to assets/img/projects/bring-roar-to-life/ then uncomment:
  <img src="/assets/img/projects/bring-roar-to-life/servo_response_test.jpg" alt="Servo response time test setup" style="width: 400px;">
  -->

  - Created a test to measure response time and estimate the transfer function of servo motors, assuming a second-order system.
  </div>

<div class="section-header" markdown="1">
**Technical Lead:** Ensured that the team reached its stated goals and provided mentorship.
</div>

- Mentored teammates and classmates on programming, controls, and electromechanical design.
- Led weekly meetings and discussions for longitudinal and time-sensitive project milestones.
- Facilitated task delegation and milestone reporting to monitor progress at individual and team levels.

<div class="img-text-row" markdown="1">
<div class="img-pair">
<video autoplay loop muted playsinline style="width: 400px;">
  <source src="/assets/video/first_full_test.mp4" type="video/mp4">
</video>
<img src="/assets/img/projects/bring-roar-to-life/trophy.jpg" alt="Faculty's Choice Award trophy" style="width: 150px;">
</div>

Awarded the **Faculty's Choice Award** at the<br>University of Central Florida Senior Design Showcase.
</div>
