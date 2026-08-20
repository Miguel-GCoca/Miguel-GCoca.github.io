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

Anky is a low-cost physical AI deployment platform built from 3d printed parts, and hobby level electronics. 
Designed and built by a fully student lead team of 5 mechanical engineering majors, we set out to prove what can be acheived by to-be-grads with no outside guidance.
It is by far the most exciting project I've been a part of.
Project goals:
- Locomotion controlled by a machine learning model developed in Isaac Lab and inferenced in ROS2.
- Resembling an ankylosaurus in proportions, motion, and anatomy.
- Voice controlled teleoperation prompted with keyphrase "hey, Anky!" 

<div class="img-pair">
<img src="/assets/img/projects/bring-roar-to-life/team_photo.jpg" alt="ROAR team" style="width: 300px;">
<img src="/assets/img/projects/bring-roar-to-life/anky_insim_4-3.jpg" style="width: 300px;">
<img src="/assets/img/projects/bring-roar-to-life/anky_irl.jpg" style="width: 300px;">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 300px;">
<source src="/assets/video/reboot_sequence.mp4" type="video/mp4">
</video>
</div>

<div class="section-header" markdown="1">
Project role - **Control Architecture Lead:** Developed a machine learning policy and ROS2 nodes to control the robot.
</div>

The video below shows the second generation Anky learning to walk over 6 thousand iterations (top right corner).
Each iteration had 1024 individual robot environments which brings total amount of training instances to over 6 million.
On a RTX 2070 laptop this took about 6 hours to train.

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/training.mp4" type="video/mp4">
</video>

- The team's CAD assembly was converted to URDF format and imported to NVIDIA's Isaac Lab 3.0.
- This software is where we can write custom reward and penalty functions that "motivate" toward a certain goal.
- Expected conditions can also be simulated. For example and in Anky's case the robot had a high magnitude impulse randomly induced in a random direction to teach it how to react to being pushed in real life.
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/bring-roar-to-life/rqt_graph_horizontal.jpg" style="width: 500px;">
</div>
- The rest of the ROS2 architecture is shown. On the left are the microphone and imu inputs, and on the right the servo command outputs.
- An inference method for the RL policy represented by the blue ellipse, was developed to run via a ROS2 node.
- The closed loop feedback for the leg joints relies on modified servos. (see further below)
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/siminloop.mp4" type="video/mp4">
</video>
- Isaac Sim sim-in-loop strategy was used to prove the functionality of my control architecture.
- I used a simulated IMU and encoders which were read by the trained model on a Raspberry Pi over ROS2. The command thetas were then routed back to the sim.
- This was completed before any purchace order was filed saving time and money by proving our design could work before fabrication began.
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/first_walking_test_wide.mp4" type="video/mp4">
</video>
- This video shows my first attempt at deploying the trained policy, my first time seeing what it can do on physical hardware.
- Since the policy was trained entirely in simulation it had encountered a "walk forward" command millions of times and knew exactly what to do to execute it.
- On our first test we acheived our functional goals and all that remained was refinement.
</div>

<div class="section-header" markdown="1">
Project role - **Electrical Design Lead:** Selection of electronic components and design of power and safety systems.
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/bring-roar-to-life/fritzing.jpg" style="width: 500px;">
</div>
- When designing power delivery for the servos it became clear that the worst case scenario of all servos reaching stall torque would draw over 40 amps, at 8.4 volts per servo it became clear that a fuse was necessary to prevent damaging critical components.
- Capacitors were wired in parallel to the servos to smooth out voltage drops that happen when the servos draw power.
- Not seen in this image is the analog feedback wiring. 
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/bring-roar-to-life/custom_shield.jpg" style="width: 300px;">
</div>
- The protoboard pictured, is a custom made arduino mega hat, it integrates the servo driver, IMU, analog reading points, I2C communication, and power for all components. 
- This piece was integral to the project, it condenced the footprint of all of these components to the area of the arduino. 
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/test_exposed_wiring.mp4" type="video/mp4">
</video>
- Wired and bench-tested the robot's power and signal harness before final assembly.
- Verified all connections were sound before the electronics were enclosed.
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<div class="img-stack">
<img src="/assets/img/projects/bring-roar-to-life/servo_open.jpg" alt="Servo response time test setup" style="width: 250px;">
<img src="/assets/img/projects/bring-roar-to-life/servo_closed.jpg" alt="Servo response time test setup" style="width: 250px;">
</div>
<video class="lazy-video" loop muted playsinline preload="none" style="width: 260px;">
<source src="/assets/video/servo_measurement.mp4" type="video/mp4">
</video>
</div>
- In order to acquire positional feedback all that needed to be done was to solder in a wire that could read the internal potentiometer of the servo.
- Once this was placed I was able to estimate the transfer function of servo motors, assuming a second-order system.
</div>

<div class="section-header" markdown="1">
**Technical Lead:** Ensured that the team reached its stated goals and provided mentorship.
</div>

- Mentored teammates and classmates on programming, controls, and electromechanical design.
- Led weekly meetings and discussions for longitudinal and time-sensitive project milestones.
- Facilitated task delegation and milestone reporting to monitor progress at individual and team levels.

<div class="img-text-row" markdown="1">
<div class="img-pair">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 400px;">
<source src="/assets/video/first_full_test.mp4" type="video/mp4">
</video>
<img src="/assets/img/projects/bring-roar-to-life/trophy.jpg" style="width: 150px;">
</div>
Awarded the **Faculty's Choice Award** at the University of Central Florida Senior Design Showcase.
</div>
