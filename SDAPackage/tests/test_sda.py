import unittest
import numpy as np
from SDA import *

class SDATestCase(unittest.TestCase):

    def setUp(self):
        self.obstacle_map = ObstacleMap(np.array([0,0,0]), np.array([[-1, -1], [-1, 100], [100, 100], [100, -1]]))

    def test_add_obstacles(self):
        """
        Test ObstacleMap's add_obstacle() method
        """
        new_obstacle = StationaryObstacle(np.array([0, 10, 0]), 5, 20)

        self.obstacle_map.add_obstacle(np.array([new_obstacle]))

        self.assertEqual(self.obstacle_map.get_obstacles().size, 1)

    def test_reset_obstacles(self):
        """
        Test ObstacleMap's reset_obstacles() method
        """
        new_obstacle = StationaryObstacle(np.array([0, 10, 0]), 5, 20)

        self.obstacle_map.add_obstacle(np.array([new_obstacle]))
        self.obstacle_map.reset_obstacles()

        self.assertEqual(self.obstacle_map.get_obstacles().size, 0)

    def test_reset_waypoints(self):
        """
        Test ObstacleMap's reset_waypoints() method
        """
        self.obstacle_map.reset_obstacles()
        self.obstacle_map.reset_obstacles()
        self.obstacle_map.set_drone_position(np.array([0,0,0]))
        waypoint = np.array([20, 0, 0])

        self.obstacle_map.add_waypoint(waypoint)

        self.obstacle_map.reset_waypoints()
        self.assertEqual(len(self.obstacle_map.get_drone().get_waypoint_holder()), 0)

    def test_obstacle_in_path_detection_false(self):
        """
        Test ObstacleMap's ability to determine if obstacles intersect with
        waypoint path. This test includes an obstacle that is not in the path
        of the UAV.
        """
        self.obstacle_map.reset_obstacles()
        self.obstacle_map.reset_waypoints()
        self.obstacle_map.set_drone_position(np.array([0,0,0]))
        obstacle_in_path = StationaryObstacle(np.array([50, 0, 0]), 5, 20)
        waypoint = np.array([50, 50, 0])

        self.obstacle_map.add_obstacle(obstacle_in_path)
        self.obstacle_map.add_waypoint(waypoint)

        obstacle_in_path_boolean, avoid_paths = self.obstacle_map.is_obstacle_in_path()
        self.assertEqual(obstacle_in_path_boolean, False)

    def test_obstacle_in_path_detection_true(self):
        """
        Test ObstacleMap's ability to determine if obstacles intersect with
        waypoint path. This test includes an obstacle that is in the path of
        the UAV.
        """
        self.obstacle_map.reset_obstacles()
        self.obstacle_map.reset_waypoints()
        self.obstacle_map.set_drone_position(np.array([0,0,0]))
        obstacle_in_path = StationaryObstacle(np.array([50, 0, 0]), 5, 20)
        waypoint = np.array([100, 0, 0])

        self.obstacle_map.add_obstacle(obstacle_in_path)
        self.obstacle_map.add_waypoint(waypoint)

        obstacle_in_path_boolean, avoid_paths = self.obstacle_map.is_obstacle_in_path()
        self.assertEqual(obstacle_in_path_boolean, True)

    def test_obstacle_under_waypoint_path_false(self):
        """
        Test ObstacleMap's ability to go above an obstacle
        """
        self.obstacle_map.reset_obstacles()
        self.obstacle_map.reset_waypoints()
        self.obstacle_map.set_drone_position(np.array([0,0,0]))
        obstacle_in_path = StationaryObstacle(np.array([50, 0, 0]), 5, 10)
        waypoint = np.array([100, 0, 25])
        new_uav_position = np.array([0, 0, 25])

        self.obstacle_map.add_obstacle(obstacle_in_path)
        self.obstacle_map.add_waypoint(waypoint)
        self.obstacle_map.set_drone_position(new_uav_position)

        obstacle_in_path_boolean, avoid_paths = self.obstacle_map.is_obstacle_in_path()
        self.assertEqual(obstacle_in_path_boolean, False)

    def test_obstacle_under_waypoint_path_true(self):
        """
        Test ObstacleMap's ability to go above an obstacle
        """
        self.obstacle_map.reset_obstacles()
        self.obstacle_map.reset_waypoints()
        self.obstacle_map.set_drone_position(np.array([0,0,0]))
        obstacle_in_path = StationaryObstacle(np.array([50, 0, 0]), 5, 15)
        waypoint = np.array([100, 0, 25])
        new_uav_position = np.array([0, 0, 25])

        self.obstacle_map.add_obstacle(obstacle_in_path)
        self.obstacle_map.add_waypoint(waypoint)
        self.obstacle_map.set_drone_position(new_uav_position)

        obstacle_in_path_boolean, avoid_paths = self.obstacle_map.is_obstacle_in_path()
        self.assertEqual(obstacle_in_path_boolean, True)
