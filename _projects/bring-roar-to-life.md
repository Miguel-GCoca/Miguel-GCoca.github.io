---
title: "Bring ROAR to Life: \"Hey, Anky!\""
excerpt: "Award winning robot dinosaur. Physical AI brain with reinforcement learning training and voice control."
order: 1
img: bring-roar-to-life/anky_insim.jpg
img-position: 40% 50%
---
<div class="section-header" markdown="1">
**Senior Capstone Project — Completed July 2026**
</div>

Anky is a low-cost physical AI deployment platform built from 3d printed parts, and hobby level electronics. 
Designed and built by a fully student lead team of 5 mechanical engineering majors, we set out to prove what can be acheived by to-be-grads with zero guidance.
It is by far the most exciting project I've been a part of.
<br>
**Project goals:**
- Locomotion controlled by a machine learning model developed in Isaac Lab and inferenced in ROS2 on Linux Ubuntu.
- Resembling an ankylosaurus in proportions, motion, and anatomy.
- Voice controlled teleoperation prompted with activation phrase "hey, Anky!" 

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/bring-roar-to-life/team_photo.jpg" alt="ROAR team" style="width: 300px;">
<img src="/assets/img/projects/bring-roar-to-life/anky_insim_4-3.jpg" style="width: 300px;">
<img src="/assets/img/projects/bring-roar-to-life/anky_irl.jpg" style="width: 300px;">
</div>
</div>

<div class="section-header" markdown="1">
Project role - **Control Architecture Lead:** Developed a machine learning policy and ROS2 nodes in Linux Ubuntu.
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
- Expected conditions can also be simulated. For example, in Anky's case the robot had a high magnitude impulse randomly induced in a random direction to teach it how to react to being pushed in real life.
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/bring-roar-to-life/rqt_graph_horizontal.jpg" style="width: 500px;">
- The rest of the ROS2 architecture is shown. On the left are the microphone and imu inputs, and on the right the servo command outputs.
- An inference method for the RL policy, represented by the blue ellipse, was run within a ROS2 node.
- The closed loop feedback for the leg joints relies on modified servos. (see electrical section)
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
<img src="/assets/img/projects/bring-roar-to-life/filtered_data.jpg" style="width: 500px;">
- A low-pass filter was used to smooth the IMU data. These graphs show the effect of the filter, the bottom image is the raw unfiltered angular velocity data with ample noise, and the top is the filtered result. 
- It was essential to add filtering to the IMU and positional feedback readings. Without the filter the robot would wildly try to correct for these random fluctuations.
- ROS2 bag was used to record this data for analysis in graphing software. 
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
- When designing power delivery for the servos it became clear that the worst case scenario of all servos reaching stall torque would draw over 40 amps, at 8.4 volts our battery would deplete in minutes.
- Capacitors were wired in parallel to the servos to smooth out voltage drops that happen when the servos draw power
- The buck converters were rated for 20 amps each, since the motors could draw above 40 I used two bucks.
- Not seen in this image is the analog feedback wiring. 
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<div class="img-stack">
<img src="/assets/img/projects/bring-roar-to-life/servo_open.jpg" alt="Servo response time test setup" style="width: 220px;">
<img src="/assets/img/projects/bring-roar-to-life/servo_closed.jpg" alt="Servo response time test setup" style="width: 220px;">
</div>
<video class="lazy-video" loop muted playsinline preload="none" style="width: 260px;">
<source src="/assets/video/servo_measurement.mp4" type="video/mp4">
</video>
</div>
- To acquire positional feedback all that was needed was a wire soldered to the internal potentiometer of the servo.
- Once the potentiometer reading was calibrated I was able to estimate the transfer function of servo motors using a step-response test, assuming a second-order system.
- This test was repeated with the limbs attached. The response time and the second moment of inertia of each limb segment were used to calculate the stiffness and damping of each joint for accurate simulation and training in Isaac Lab
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/bring-roar-to-life/custom_shield.jpg" style="width: 350px;">
- The protoboard pictured, is a custom made Arduino Mega hat, it integrates the servo driver, IMU, analog reading points, I2C communication, and power for all components.
- The 12 analog reading solder points being so close to one another necessitated EMI shielded wires be used to carry the servo potentiometer feedback signal without crosstalk.
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/test_exposed_wiring.mp4" type="video/mp4">
</video>
- Verified all connections were sound before the electronics were enclosed.
- We had not received the Arduino Mega, this test had three Arduino Unos for joint position reading.
- The AI model had no idea what to do while upside down so it moves seemingly randomly.
</div>

<div class="section-header" markdown="1">
Awarded the **Faculty's Choice Award** at the University of Central Florida Summer '26 Senior Design Showcase.
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 400px;">
<source src="/assets/video/first_full_test.mp4" type="video/mp4">
</video>
<video class="lazy-video" loop muted playsinline preload="none" style="width: 400px;">
<source src="/assets/video/reboot_sequence.mp4" type="video/mp4">
</video>
<img src="/assets/img/projects/bring-roar-to-life/trophy.jpg" style="width: 150px;">
</div>
</div>
