import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SicaklikIzleyici(Node):
    def __init__(self):
        super().__init__('sicaklik_izleyici')
        # BONUS: Eşik değerini parametre yapıyoruz
        self.declare_parameter('esik_degeri', 30.0)
        
        self.subscription = self.create_subscription(
            Float32,
            'sicaklik',
            self.sicaklik_callback,
            10)

    def sicaklik_callback(self, msg):
        sicaklik = msg.data
        self.get_logger().info(f'Gelen Sıcaklık: {sicaklik:.2f} °C')
        
        esik = self.get_parameter('esik_degeri').get_parameter_value().double_value
        
        if sicaklik > esik:
            self.get_logger().warn(f'DİKKAT! Sıcaklık çok yüksek: {sicaklik:.2f} °C')

def main(args=None):
    rclpy.init(args=args)
    node = SicaklikIzleyici()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
