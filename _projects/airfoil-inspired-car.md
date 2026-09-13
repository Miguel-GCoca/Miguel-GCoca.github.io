---
title: "Airfoil Inspired Car"
excerpt: "Miniature car with an SD7062 airfoil-inspired design for drag coefficient and flow analysis in a laser vapor wind tunnel."
order: 3
completed: "July 2025"
img: airfoil-inspired-car/full_car_iso.jpg
# img-position: 50% 50%  # e.g. "30% 70%" to nudge proportionally, or "left 20px top 10px" for an exact pixel offset
---
<div class="section-header" markdown="1">
**EML 3303C Mechanical Engineering Measurements — Completed July 2025**
</div>

The task set before me in the course was to design a car and measure its drag coefficient experimentally. The car was placed in a laser vapor wind tunnel for two purposes,
to measure the drag force on the car by attaching it to a strain gauge and to visualize the fluid boundary layer.
I used concepts learned in EAS 3101 Fundamentals of Aerodynamics to guide the design.
<br>
**Project goals:**
- Design a small-scale car that minimizes drag under wind-tunnel testing while meeting the project's mass constraints.
- Use an inverted-airfoil body to generate downforce, increasing tire friction as a way to counteract drag.
- Fabricate and experimentally validate the design's drag performance against a benchmark car.

<div class="img-text-row" markdown="1">
<video class="lazy-video" loop muted playsinline preload="none" style="width: 500px;">
<source src="/assets/video/airfoil_car_tunnel.mp4" type="video/mp4">
</video>
- The fundamental concept underpinning my design was the idea that the higher the weight of the car the higher the friction between axle and body and between wheel and ground. This friction could prove useful to counteract drag force. 
- Therefore the fundamental question is how do I increase the total weight of the car beyond what the mass constraints of the project seem to allow. 
- The solution I came up with was to use an inverted wing design. Inducing downforce would add to the weight of the car increasing the friction of the system and decreasing measured drag force.
</div>

<div class="section-header" markdown="1">
Project role - **Lead CAD Designer:** Modeling the car after an inverted airfoil.
</div>

<div class="img-text-row" markdown="1">
<img src="/assets/img/projects/airfoil-inspired-car/original_foil_graphed.jpg" alt="SD7062 airfoil profile plotted" style="width: 500px;">
- The SD7062 foil was chosen for being optimized for low Reynolds number flow, giving a high lift coefficient even at the chamber's low airspeeds.
- Its thicker cambered body was also necessary to fill the cavity of the 3d print with sand to meet the weight requirement.
- It was pitched at -4 degrees, chosen due to the results of the foil's drag polars show below.
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/airfoil-inspired-car/drag_polars_1.jpg" alt="SD7062 drag polar plots, Cl vs Cd and Cl vs alpha" style="width: 500px;">
<img src="/assets/img/projects/airfoil-inspired-car/drag_polars_2.jpg" alt="SD7062 drag polar plots, Cl/Cd vs alpha and Cd vs alpha" style="width: 500px;">
</div>
- Here are the SD7062 airfoil's drag polars (Cl vs Cd, Cl vs alpha, Cl/Cd vs alpha, and Cd vs alpha), plotted at four different Reynolds numbers to pick an angle of attack (AOA).
- The Cl/Cd vs alpha graph peaks at 4 degrees AOA for low Reynold's flow, with efficiency improving at higher Reynolds number.
</div>

<div class="img-text-row" markdown="1">
<div class="img-pair">
<img src="/assets/img/projects/airfoil-inspired-car/3d_base_foil.jpg" alt="3D-printed airfoil base shape" style="width: 250px;">
<img src="/assets/img/projects/airfoil-inspired-car/full_car_iso.jpg" alt="Completed airfoil-inspired car, isometric view" style="width: 250px;">
</div>
- I saved the selected foil outline and camber line as a CVS which uploaded to Solidworks served as the outline for the base car model.
- The model was saved to .Step format and made on my 3d printer. While printing, the print was paused before the top layer was completed and filled with sand.
</div>

<div class="section-header" markdown="1">
**Testing & Results**
</div>

In the wind tunnel, the car was mounted to a strain-gauge drag sensor read out through a LabVIEW VI, with drag force computed from the measured scale weight as:
<br>
 <strong>D = 2.1W + 0.31</strong>. 
<br>
At maximum tunnel speed the car recorded drag forces of 22.15N, 28.03N, 24.46N, 21.94N, and 22.36N across five runs — noticeably higher than the 11.65N–15.64N measured on a TA-supplied benchmark car under the same conditions. The added downforce from the inverted-airfoil shape was doing its job of loading the wheels, but that same load showed up directly in the drag reading, since this test setup measures downforce-driven friction as part of the drag signal.

A hysteresis sweep was also run, ramping speed up from about a fifth of max to full speed and back down in five steps each direction. Results tracked closely between the up and down sweeps (e.g. 15.39 m/s → 20.26N ramping up vs. 15.18 m/s → 19.0N ramping down), showing little hysteresis in the car's drag response.

One hardware issue came up during testing: the wheels were repeatedly blown off the axle by the airflow. The fix was a wooden wedge cut and driven into the axle end to hold them in place for the rest of the test runs.
