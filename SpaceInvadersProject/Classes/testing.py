import sys
import os


base_path = os.path.dirname(os.path.abspath(__file__))  # Path to the current file's directory
image_path = os.path.join(base_path, r"..\Assets\Sprites\SpaceShip")

print(image_path)