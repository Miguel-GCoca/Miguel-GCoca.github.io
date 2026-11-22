---
title: "Dynamic Swept Wing"
excerpt: "Morphing airfoil for submersed flow analysis with user controlled telescopic span and variable sweep angle."
order: 4
completed: "April 2025"
img: dynamic-swept-wing/piv_tank.jpg
# img-position: 50% 50%  # e.g. "30% 70%" to nudge proportionally, or "left 20px top 10px" for an exact pixel offset
---
<div class="section-header" markdown="1">
**Research, WEAR Lab. Completed April 2025**
</div>

A morphing airfoil for submersed flow analysis, with user controlled telescopic span and variable sweep angle.
<br>

**Project goals**
- Allow independent, user controlled adjustment of wingspan and sweep angle during underwater flow testing.
- Create a Bowden cable mechanism that telescopes the wingspan, plus a cable tensioning system.
- Deliver responsive, accurate control suitable for real time flow experiments.

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/dynamic-swept-wing/swept_wing_irl.jpg" alt="Assembled dynamic swept wing rig" style="width: 250px;">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 250px;">
<source src="/assets/video/wing_animation.mp4" type="video/mp4">
</video>
</div>
- A linear actuator controls the sweep angle.
- A servo controls the wingspan.
- The user sends input to an Arduino Uno over serial.
- Wrote and optimized the control firmware in C/C++ for speed, accuracy and ease of use.
</div>

<div class="section-header" markdown="1">
Project role: **Systems Integrator**. I was responsible for bringing the separate pieces and prototypes together into one deliverable.
</div>


<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 600px;">
<source src="/assets/video/tensioning_sidebyside.mp4" type="video/mp4">
</video>
- The tensioning mechanism uses principles from EML 3262 Kinematics of Mechanisms.
- Once the 4-bar linkage reaches its toggle position, the links lock in place.
- The locked linkage holds the Bowden cables tight like a vise. That tensions the pulley system that engages the telescopic wingspan.
</div>


<div class="section-header" markdown="1">
**Experimental application**
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/dynamic-swept-wing/tank_diagram.jpg" alt="Diagram of the wing rig mounted in the water tank" style="width: 300px;">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 400px;">
<source src="/assets/video/wing_in_tank.mp4" type="video/mp4">
</video>
</div>
- The wing rig is lowered into a water tank, actuated by plunging and pitching motors and instrumented with a force sensor to capture hydrodynamic loads.
- A laser sheet and camera positioned along the tank enable Particle Image Velocimetry (PIV), which tracks seeded flow around the wing as span and sweep change.
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/tank_flow_results.mp4" type="video/mp4">
</video>
- This is raw PIV footage. The laser sheet lights up tracer particles seeded in the tank, and the wing's edge is visible cutting through the flow.
- These particle fields get post processed into velocity vectors, which show how the wake changes with sweep angle.
</div>
