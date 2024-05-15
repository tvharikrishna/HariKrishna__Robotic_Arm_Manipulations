"""
Author: Venkata Harikrishna, Talapala
Github Username: tvharikrishna
YouTube Channel Name, Username: Harikrishna Robotics and AI, @harikrishnaroboticsai
LinkedIn Username: tvharikrishnahk
License for this code: Apache 2.0
"""

from omni.isaac.examples.base_sample import BaseSample
from omni.isaac.franka import Franka
from omni.isaac.core.objects import DynamicCuboid
from omni.isaac.core.objects import StaticCuboid
from omni.isaac.franka.controllers import PickPlaceController
import numpy as np

class HelloWorld(BaseSample):
    """
    Main class for initializing and controlling the Franka Emika robot
    in the NVIDIA Isaac Sim environment for a block stacking task.
    """
    def __init__(self) -> None:
        """
        Initialize the HelloWorld class and set up initial state tracking variables.
        """
        super().__init__()

        # Track the current cube being processed
        self.current_cube_index = 0 
        # Flag to track operation completion for each cube
        self.operation_completed = False  

    def setup_scene(self):
        """
        Set up the simulation environment, including the robotic arm and the cubes.
        """
        world = self.get_world()
        world.scene.add_default_ground_plane()
        self.franka = world.scene.add(Franka(prim_path="/World/Fancy_Franka", name="fancy_franka"))

        # Adjust initial positions for five cubes, ensuring proper spacing for stacking
        initial_positions = [
            np.array([0.3, 0.3, 0.3]),   # Position for Block 1
            np.array([0.5, 0.2, 0.3]),   # Position for Block 2
            np.array([0.6, 0.1, 0.3]),   # Position for Block 3
            np.array([0.6, -0.1, 0.3]),  # Position for Block 4 
            np.array([0.5, 0.0, 0.3])    # Position for Block 5 
        ]

        # Create and add dynamic cuboids as interactive cubes in the scene
        self.cubes = []
        for i, pos in enumerate(initial_positions):
            cube = world.scene.add(
                DynamicCuboid(
                    prim_path=f"/World/cube_{i}",
                    name=f"cube_{i}",
                    position=pos,
                    scale=np.array([0.0515, 0.0515, 0.0515]),
                    color=np.array([1.0, 0, 0])
                )
            )
            self.cubes.append(cube)

        # Initialize the controller for pick and place operations
        self.controller = PickPlaceController(
            name="pick_place_controller",
            gripper=self.franka.gripper,
            robot_articulation=self.franka,
        )

    async def setup_post_load(self):
        """
        Perform asynchronous tasks post-load, like starting the simulation.
        """
        self.world = self.get_world()
        self.world.add_physics_callback("sim_step", callback_fn=self.physics_step)
        await self.world.play_async()

    def physics_step(self, step_size):
        """
        Define the physics step operation to handle cube picking and stacking.
        """
        if self.current_cube_index < len(self.cubes) and not self.operation_completed:
            current_cube = self.cubes[self.current_cube_index]
            cube_position, _ = current_cube.get_world_pose()

            # Define the stacking position for each cube
            goal_position = np.array([-0.3, -0.3, 0.0515 / 2 + 0.0515 * self.current_cube_index])
            current_joint_positions = self.franka.get_joint_positions()

            # Calculate actions for the current step
            actions = self.controller.forward(
                picking_position=cube_position,
                placing_position=goal_position,
                current_joint_positions=current_joint_positions,
            )

            # Apply actions to the robotic arm
            self.franka.apply_action(actions)

            # Check if the placement task is completed
            if self.controller.is_done():
                # Set flag when a cube is placed
                self.operation_completed = True  

        elif self.operation_completed:
            # Move to the next cube
            self.current_cube_index += 1  
            # Reset the operation for the next cube
            if self.current_cube_index < len(self.cubes):  
                self.operation_completed = False
                self.controller.reset()

    async def setup_post_reset(self):
        """
        Reset the environment and variables post-simulation to ensure a clean state for re-runs.
        """
        self.controller.reset()
        self.franka.gripper.set_joint_positions(self.franka.gripper.joint_opened_positions)
        # Reset the cube index on reset
        self.current_cube_index = 0 
        # Reset operation completion flag
        self.operation_completed = False  
        await self.world.play_async()
