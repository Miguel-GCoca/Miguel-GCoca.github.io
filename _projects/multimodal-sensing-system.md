---
title: "Multimodal Human and Ambient Sensing System"
excerpt: "Open source, wrist mounted health and activity monitor with IMU and PPG sensing."
order: 6
completed: "September 2023"
img: multimodal-sensing-system/muhass_custom_board.jpg
img-position: 50% 70%
---
<div class="section-header" markdown="1">
**Research project, WEAR Lab. Completed September 2023**
</div>

An open source, wrist mounted health and activity monitor with IMU and PPG sensing. Most wearable biomechanics and physiologic sensors are standalone systems with proprietary hardware and incompatible communication protocols. That makes it hard to combine several of them for synchronized, real time measurement in the field. This project fills that gap with a single wrist worn device and a companion app.
<br>
**Project goals**
- Combine IMU and PPG sensing into a single open source, wrist mounted device.
- Validate the device's accuracy against commercially available actigraphy devices.
- Minimize the device's footprint through a custom housing and wrist mount design.

<div class="section-header" markdown="1">
Project role: **Research Assistant**
</div>

<div class="img-text-row" markdown="1" data-toc-sub="System architecture">
<img src="/assets/img/projects/multimodal-sensing-system/muhass_architecture.jpg" alt="MUHASS system architecture diagram" style="width: 500px;">
- The device streams data over Bluetooth or Wi-Fi to a companion smartphone app for real time visualization and analysis. The app covers physical activity, heart rate, blood pressure, blood oxygenation, stress and body/ambient temperature.
- Implemented a protocol to assess the device's accuracy against commercially available actigraphy devices.
</div>

<div class="img-text-row" markdown="1" data-toc-sub="Custom PCB and housing">
<div class="img-pair">
<img src="/assets/img/projects/multimodal-sensing-system/muhass_custom_board.jpg" alt="Custom MUHASS sensor PCB" style="width: 300px;">
<img src="/assets/img/projects/multimodal-sensing-system/muhass_irl_board.jpg" alt="Assembled MUHASS wearable module" style="width: 300px;">
</div>
- A custom PCB integrates IMU, pressure, humidity, PPG (heart rate) and GSR sensors with a microcontroller and battery, stacked into a compact wearable module.
- Fabricated the housing and wrist mount for the electronics. It keeps the overall footprint small while leaving the board and battery accessible.
</div>

<div class="section-header" markdown="1">
**Research application**
</div>

I developed the testing method used to validate the device against commercially available actigraphy devices, working with the EMBRACE Lab. That collaboration led to an NIH funded study and to my co-authorship on the resulting publication in *Frontiers in Aging*.

Presented as a poster: *"Multimodal Human and Ambient Sensing System (MUHASS),"* Department of Mechanical and Aerospace Engineering, University of Central Florida.
