import  rclpy
from rclpy.node  import Node
from std_msgs.msg import Float32
import random

class RobotLogger(Node):
	def __init__(self):
		super().__init__('robot_monitor')
		self.battery_publisher=self.create_publisher(Float32,'/robot/battery_percentage',10)
		self.temperature_publisher=self.create_publisher(Float32,'/robot/temperature_celsius',10)
		self.battery=random.uniform(0,100)
		self.temperature=random.uniform(10,30)
		self.timer=self.create_timer(1.0,self.publish_status)

	def publish_status(self):
		self.battery=random.uniform(0,100)
		self.temperature=random.uniform(10,30)
		battery_msg=Float32()
		battery_msg.data=self.battery
		self.battery_publisher.publish(battery_msg)

		temperature_msg=Float32()
		temperature_msg.data=self.battery
		self.temperature_publisher.publish(temperature_msg)
		self.get_logger().info(f'Battery Level is: {self.battery:.1f} %  | 'f'Temperature is : {self.temperature:.1f} C')

def main(args=None):
	rclpy.init(args=args)
	node=RobotLogger()
	try:
		rclpy.spin(node)
	finally:
		node.destroy_node()
		rclpy.shutdown()

if __name__  =='__manin__':
        main()
