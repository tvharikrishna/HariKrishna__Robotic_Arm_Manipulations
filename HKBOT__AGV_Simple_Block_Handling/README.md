<!------ PROJECT TITLE ------>
<p align="center">
    <img src="readme_data/project_title.png" alt="project title" width="1111"/>
</p> <br> <br>

<!------ WHAT ------>
<p align="center">
    <img src="readme_data/what.png" alt="what" width="600"/>
</p>

<p align="center"><h1>🎀 Essence of the Project</h1></p>
<p align='justify'>
This project focuses on developing a specialized algorithm for the HKBOT, which is equipped with an NVIDIA Jetson Nano and a 6-DOF robotic arm. The algorithm enhances 'pick and place' operations, dynamically adapting to different payload configurations and optimizing the spatial arrangement of blocks on the robot’s chassis. Integrated safety protocols ensure the robot operates in compliance with guidelines for mobile robots and autonomous guided vehicles.
</p>

<p align="center">
  <a href="https://www.youtube.com/watch?v=6aXYBVMJuC0">
    <img src="https://img.shields.io/badge/My Project Video-HKBOT Block Manipulation-blue" alt="Video" width="450" height="40"/>
  </a>
</p> <hr> <br> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="why" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
The aim of this project is to advance block manipulation by integrating a specialized non-autonomous algorithm with a 6-DOF robotic arm, serving as a beginner project in robotic arm and block manipulation. This initiative seeks to enhance operational efficiency and robotic mobility through the use of mecanum wheels for precise omnidirectional movement, coupled with dynamic adaptation to various payload configurations. Safety protocols are implemented to ensure compliance with the highest standards, promoting secure and efficient operations in autonomous mobile robotics.
</p> <hr> <br> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="How" width="600"/>
</p>

<p align="center"><h1>🪓 Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
This project employs a robust suite of tools to support the development and operation of HKBOT. Ubuntu and Linux provide a stable and versatile operating system environment. C++ is utilized for scripting, enhancing the project's efficiency and scalability. Communication and remote control functionalities are handled through SSH, PuTTY, and VNC Viewer, ensuring secure and flexible remote access. ROS and RViz are essential for managing robotic operations and visualizations.
</p>
<p align='justify'>
<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/C++-00599C.svg?&style=flat-square&logo=cplusplus&logoColor=white" alt="C++" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/SSH-4D4D4D.svg?&style=flat-square&logo=windows-terminal&logoColor=white" alt="SSH" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/PuTTY-007ACC.svg?&style=flat-square&logo=windows-terminal&logoColor=white" alt="PuTTY" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/VNC%20Viewer-ED1C24.svg?&style=flat-square&logo=CodeSandbox&logoColor=white" alt="VNC Viewer" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/RVIZ-000000.svg?&style=flat-square&logo=ros&logoColor=white" alt="RViz" style="height: 30px;"/> &nbsp;
</p> <br>

<!------ Technical Terms ------>
<p align="center"><h2>💠 Project Technical Terms & Concepts </h2></p>
<p align="center"><h3>▸ What is an AGV Robot?</h3></p>
<p style="text-align: justify;">
An AGV (Automated Guided Vehicle) Robot is an autonomous robot used primarily in industrial settings to transport materials around a manufacturing facility or warehouse. AGVs follow predefined paths marked by wires, tapes, or lasers, performing tasks that typically require minimal deviation from set routes. They are known for improving operational efficiency, reducing labor costs, and enhancing workplace safety.
</p> <br>

<p align="center"><h3>▸ What is an AMR Robot?</h3></p>
<p style="text-align: justify;">
An AMR (Autonomous Mobile Robot) is a more advanced type of autonomous robot that, unlike AGVs, can navigate in an environment without the need for predefined paths. AMRs use sophisticated sensors, cameras, and algorithms to understand their environment, making decisions in real-time to find the most efficient routes, avoid obstacles, and adapt to changes. This capability makes them highly versatile and suitable for a variety of applications beyond industrial logistics, including healthcare and service industries.
</p> <br>

<p align="center"><h3>▸ What is an AMMR Robot?</h3></p>
<p style="text-align: justify;">
AMMR (Autonomous Mobile Manipulation Robot) combines the capabilities of AMRs with robotic arms or other manipulators, enabling not only autonomous navigation but also the ability to interact physically with their environment. These robots can perform more complex tasks such as picking, sorting, and handling of objects, integrating the mobility of AMRs with the functionality of robotic manipulators. AMMRs are particularly useful in environments where both mobility and manipulative actions are required, such as in automated production lines or fulfillment centers.
</p> <br>

<p align="center"><h2>💠 Deployment and Testing</h2></p>
<p style="text-align: justify;">
<p align="center"><h3>▸ Manipulation Sequence Planning</h2></p>
I have designed the algorithm for the robotic arm in a way that is referred to as 'manipulation sequence' or 'manipulation planning' in robotics. When the robot's chassis already holds one or two blocks, it needs space to place an additional block. My developed algorithm directs the arm to push the existing blocks slightly backward, creating room for the new one. This process can repeat for any number of blocks, as demonstrated in the video. <br>

<p align="center"><h3>▸ Implemented Safety Measures for Operating AMRs/AGVs</h2></p>
As we all know, robots can pose a hazard if we enter their operational zone. To address safety concerns on sites and factories that use mobile robots and Autonomous Guided Vehicles (AGVs), I have programmed an algorithm to enhance safety communications. When the robot is performing a manipulation task, it emits a flashing red light. Conversely, when the robot is merely moving around, it emits a green light, signaling to humans that it is safe to approach. However, it is unsafe to approach when the robot flashes a red light. </p> <br>

<p align="center"><h2>Red: Danger</h2></p>
<p align="center">
  <img src="readme_data/project_observation_1.png" alt="Deployment and Testing Images" width="1111"/>
</p> <br>

<p align="center"><h2>Green: Safe</h2></p>
<p align="center">
  <img src="readme_data/project_observation_2.png" alt="Deployment and Testing Images" width="1111"/>
</p> <hr> <br> <br>

<!----- End Image ----->
<p align="center">
    <img src="readme_data/HKbot_endquote.png" alt="endquote" width="1500"/>
</p>
