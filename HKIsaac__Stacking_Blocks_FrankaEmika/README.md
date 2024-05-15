<!------ Copyrights ------>
<p align="right">© 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻 𝗯𝘆 𝘁𝘃𝗵𝗮𝗿𝗶𝗸𝗿𝗶𝘀𝗵𝗻𝗮</p>
<p align="right">5 𝘮𝘪𝘯𝘶𝘵𝘦 𝘳𝘦𝘢𝘥 📚 </p> <br>

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
  <a href="https://www.linkedin.com/feed/update/urn:li:activity:7130040549587243008?utm_source=share&utm_medium=member_desktop">
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
<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/C++-00599C.svg?&style=flat-square&logo=cplusplus&logoColor=white" alt="C++" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/SSH-4D4D4D.svg?&style=flat-square&logo=windows-terminal&logoColor=white" alt="SSH" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/PuTTY-007ACC.svg?&style=flat-square&logo=windows-terminal&logoColor=white" alt="PuTTY" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/VNC%20Viewer-ED1C24.svg?&style=flat-square&logo=CodeSandbox&logoColor=white" alt="VNC Viewer" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/ROS-22314E.svg?&style=flat-square&logo=ros&logoColor=white" alt="ROS" style="height: 25px;"/> &nbsp;
<img src="https://img.shields.io/badge/RVIZ-000000.svg?&style=flat-square&logo=ros&logoColor=white" alt="RViz" style="height: 25px;"/> &nbsp;
</p> <br>

<p align="center"><h2>💠 Deployment and Testing</h2></p>
<p style="text-align: justify;">
    
<p align="center"><h2>▸ Manipulation Sequence Planning</h2></p>
▸ I have designed the algorithm for the robotic arm in a way that is referred to as 'manipulation sequence' or 'manipulation planning' in robotics. When the robot's chassis already holds one or two blocks, it needs space to place an additional block. My developed algorithm directs the arm to push the existing blocks slightly backward, creating room for the new one. This process can repeat for any number of blocks, as demonstrated in the video. <br>

<p align="center"><h2>▸ Implemented Safety Measures for Operating AMRs/AGVs</h2></p>
As we all know, robots can pose a hazard if we enter their operational zone. To address safety concerns on sites and factories that use mobile robots and Autonomous Guided Vehicles (AGVs), I have programmed an algorithm to enhance safety communications. When the robot is performing a manipulation task, it emits a flashing red light. Conversely, when the robot is merely moving around, it emits a green light, signaling to humans that it is safe to approach. However, it is unsafe to approach when the robot flashes a red light. </p> <br>

<p align="center"><h2>Red: Danger</h2></p>
<p align="center">
  <img src="readme_data/project_observation_1.png" alt="Project Observation 1" width="1111"/>
</p> <br>

<p align="center"><h2>Green: Safe</h2></p>
<p align="center">
  <img src="readme_data/project_observation_2.png" alt="Project Observation 2" width="1111"/>
</p> <hr> <br> <br>

<!----- End Image ----->
<p align="center">
    <img src="readme_data/HKbot_endquote.png" alt="Alt text for your image" width="1500"/>
</p>
