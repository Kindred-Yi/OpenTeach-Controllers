#!/usr/bin/env python3
"""
Delto Gripper Basic Control Test Script

This script demonstrates how to use delto_modbus_TCP.py for basic gripper control
including sending commands to return the gripper to initial position.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from delto_modbus_TCP import Communication
import time

def main():
    # Create communication object
    comm = Communication()
    
    try:
        # Connect to gripper using default IP and port
        print("Connecting to Delto gripper...")
        if comm.connect('169.254.186.72', 502):
            print("Connected successfully!")
        else:
            print("Failed to connect!")
            return
        
        # Get current position
        print("\nGetting current position...")
        current_pos = comm.get_position()
        print(f"Current position: {current_pos}")
        
        # Send gripper to initial position (all joints to 0 degrees)
        print("\nSending gripper to initial position...")
        initial_position = [0.0] * 12  # 12 joints all set to 0 degrees
        comm.set_position(initial_position)
        time.sleep(2)  # Wait for movement to complete
        
        # Verify position
        new_pos = comm.get_position()
        print(f"New position: {new_pos}")
        
        # Test grasp functionality
        print("\nTesting grasp functionality...")
        comm.grasp_mode(1)  # Set to basic grasp mode
        time.sleep(1)
        
        # Execute grasp
        print("Executing grasp...")
        comm.grasp(True)
        time.sleep(2)
        
        # Release grasp
        print("Releasing grasp...")
        comm.grasp(False)
        time.sleep(1)
        
        # Test half-open position
        print("\nTesting half-open position...")
        half_open = [45.0] * 12  # All joints to 45 degrees
        comm.set_position(half_open)
        time.sleep(2)
        
        # Return to initial position again
        print("\nReturning to initial position...")
        comm.set_position(initial_position)
        time.sleep(2)
        
        # Set joints to free mode
        print("\nSetting joints to free mode...")
        comm.set_free(True)
        
        print("\nTest completed successfully!")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        
    finally:
        # Always disconnect
        print("\nDisconnecting...")
        comm.disconnect()
        print("Disconnected.")

if __name__ == "__main__":
    main()