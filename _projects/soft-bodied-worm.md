---
title: "Soft Bodied Red-Seeking Worm"
excerpt: "Soft-bodied robot designed to emulate worm inching and color-seeking behavior."
order: 9
img: soft-bodied-worm/full_assembly.jpg
# img-position: 50% 50%  # e.g. "30% 70%" to nudge proportionally, or "left 20px top 10px" for an exact pixel offset
---
<div class="section-header" markdown="1">
**EGN 4060C Intro to Robotics — Completed December 2023**
</div>

A soft-bodied robot built with two other ME students to emulate a worm's inching locomotion and seek out red targets using an RGB sensor.
<br>

**Project goals:**
- Emulate worm-like inching locomotion using a soft, flexible body instead of rigid linkages.
- Give the robot autonomous color-seeking behavior, triggering movement when it detects a red target.
- Balance body geometry and weight distribution so each end's motion adds up to net forward travel instead of just rocking in place.

<div class="section-header" markdown="1">
Project role - **CAD and Electronics Lead**
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/soft-bodied-worm/tiled_scale_body.jpg" style="width: 500px;">
- Designed the 3D-printed body: a rigid center chassis flanked by two flexible, tiled-scale arms, so most of the robot's weight stays centered and a single end's contraction can't just slide the whole robot instead of producing a net gait.
- The tiled scales keep each arm rigid in the horizontal plane while compressing, since the scales can't slide past one another — this let us add side-to-side wave motion as a stretch goal instead of just up-down motion.
- Routed nylon wire beneath each arm's joint with the chassis, so contracting it creates a moment that shifts more of the robot's weight onto that end, raising its friction against the ground at the right point in the gait.
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/soft-bodied-worm/full_assembly.jpg" style="width: 500px;">
- Built the power system and wiring for two SG90 servos, an Arduino Pro Mini, a TCS34725 RGB sensor, a 9V battery, and a voltage regulator.
- The Pro Mini has no onboard USB, so it was programmed by tethering it through an Arduino Uno wired to the host laptop.
- Wrote the control loop: the TCS34725 streams raw red/green/blue/clear values, and a conditional check for red dominance triggers the gait — contract both arms, then release the back arm before the front so it pushes the front forward.
</div>

<div class="section-header" markdown="1">
**Results**
</div>

The robot reproduced the worm's inching gait: contracting both ends, then releasing the back end first so it pushed the front end forward, the same way an organic worm moves. Getting there took a lot of iteration — the servo timing, wire tension, and component layout inside the body all needed reworking before the contraction/release delays lined up correctly.

The main limitation was speed. Published measurements put nematode worms at 15.9-250 micrometers per second; even accounting for the difference in scale, our robot moved orders of magnitude faster than that, but the slow, deliberate character of the gait itself remained. That points to speed being an inherent property of wave-like locomotion rather than something specific to our implementation — worth testing further with higher-torque servos or different flexible materials.
