---
title: "Dynamic Swept Wing"
excerpt: "Morphing airfoil for submersed flow analysis with user-controlled telescopic span and variable sweep angle."
order: 5
img: dynamic-swept-wing/piv_tank.jpg
# img-position: 50% 50%  # e.g. "30% 70%" to nudge proportionally, or "left 20px top 10px" for an exact pixel offset
---
<div class="section-header" markdown="1">
**Research, WEAR Lab — Completed April 2024**
</div>

A morphing airfoil for submersed flow analysis, with user-controlled telescopic span and variable sweep angle.
<br>

**Project goals:**
- Allow independent, user-controlled adjustment of wing span and sweep angle during underwater flow testing.
- Create bowden cable wingspan telescoping mechanism, and cable tensioning system.
- Deliver responsive, accurate control suitable for real-time flow experiments.

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/dynamic-swept-wing/swept_wing_irl.jpg" style="width: 250px;">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 250px;">
<source src="/assets/video/wing_animation.mp4" type="video/mp4">
</video>
</div>
- Linear actuator controlled sweep angle.
- Servo controlled wingspan.
- User input to Arduino Uno over serial.
</div>

<div class="section-header" markdown="1">
Project role - **Systems Integrator:** Responsible for coalescing various pieces and prototypes into one deliverable.
</div>


<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 600px;">
<source src="/assets/video/tensioning_sidebyside.mp4" type="video/mp4">
</video>
- Using principles from EML 3262 - Kinematics of Mechanisms.
- Once 4-bar linkage reaches toggle position the links are locked in place.
- This pulls the bowden cables in a vice-lock tensioning the pulley system that engages the telescopic wingspan.
</div>


<div class="section-header" markdown="1">
**Experimental Application**
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/dynamic-swept-wing/tank_diagram.jpg" style="width: 300px;">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 400px;">
<source src="/assets/video/wing_in_tank.mp4" type="video/mp4">
</video>
</div>
- Wing rig lowered into a water tank, actuated by plunging and pitching motors and instrumented with a force sensor to capture hydrodynamic loads.
- A laser sheet and camera positioned along the tank enable Particle Image Velocimetry (PIV), tracking seeded flow around the wing as span and sweep change.
</div>

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/tank_flow_results.mp4" type="video/mp4">
</video>
- Raw PIV footage: the laser sheet illuminates tracer particles seeded in the tank, with the wing's edge visible cutting through the flow.
- These particle fields are what get post-processed into velocity vectors, letting us see how the wake changes with sweep angle.
</div>
