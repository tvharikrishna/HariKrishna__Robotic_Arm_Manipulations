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
This project showcases the integration and control of the Franka Emika robot within NVIDIA Isaac Sim to automate the stacking of blocks. Utilizing sophisticated robotics control algorithms, this simulation demonstrates how precise robotic manipulation is achieved in complex tasks such as stacking, providing a platform for further research and development in automated robotics systems.
</p>

<p align="center">
  <a href="https://www.linkedin.com/feed/update/urn:li:activity:7130040549587243008?utm_source=share&utm_medium=member_desktop">
    <img src="https://img.shields.io/badge/My Project Video-Stacking Blocks w/ Franka Robot-blue" alt="Video" width="480" height="40"/>
  </a>
</p> <hr> <br> <br>

<!------ WHY ------>
<p align="center">
    <img src="readme_data/why.png" alt="why" width="600"/>
</p>

<p align="center"><h1>🎯 Project Vision</h1></p>
<p style="text-align: justify;">
The vision behind this project is to demonstrate the capabilities of robotic systems in performing precise and delicate tasks such as stacking, which require high accuracy and stability. Block stacking is fundamental to various applications, including automated warehousing, assembly lines in manufacturing, and construction robotics. By simulating these tasks within NVIDIA Isaac Sim, this project aims to provide insights into the challenges and solutions in robotics control, paving the way for implementing these techniques in real-world applications, where such skills can significantly enhance efficiency and precision.
</p> <hr> <br> <br>

<!------ HOW ------>
<p align="center">
    <img src="readme_data/how.png" alt="How" width="600"/>
</p>

<p align="center"><h1>🪓 Project Implementation</h1></p>
<p><h2>💠 Software Design & Tools </h2></p>
<p align='justify'>
The implementation leverages Ubuntu and Linux as the operating systems, with Python scripting within the NVIDIA Isaac Sim environment. The project utilizes advanced robotics simulation tools, including the precise control mechanisms provided by the Isaac Sim Pick and Place Controller, allowing for detailed manipulation and interaction with the simulated environment.
</p>

<p>
<img src="https://img.shields.io/badge/Ubuntu-E95420.svg?&style=flat-square&logo=ubuntu&logoColor=white" alt="Ubuntu" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Linux-FCC624.svg?&style=flat-square&logo=linux&logoColor=black" alt="Linux" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/Python-3776AB.svg?&style=flat-square&logo=python&logoColor=white" alt="Python" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/VS%20Code-007ACC.svg?&style=flat-square&logo=visual-studio-code&logoColor=white" alt="VS Code" style="height: 30px;"/> &nbsp;
<img src="https://img.shields.io/badge/NVIDIA%20Isaac%20SIM-76B900.svg?&style=flat-square&logo=nvidia&logoColor=white" alt="NVIDIA Isaac SIM" style="height: 30px;"/> &nbsp;
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
