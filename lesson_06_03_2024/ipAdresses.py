class IPAddress:
    def __init__(self, ip_address):
        self.ip_address = ip_address

    def display(self):
        print(self.ip_address)

class IPAddressChecked(IPAddress):
    def __init__(self, ip_address):
        super().__init__(ip_address)
        self.is_valid = self.check_ip_validity(ip_address)

    def display(self):
        super().display()
        print('- Правильно' if self.is_valid else '- Неправильно')

    def check_ip_validity(self, ip_address):
        segments = ip_address.split('.')
        if len(segments) != 4:
            return False
        for segment in segments:
            if not segment.isdigit():
                return False
            if int(segment) < 0 or int(segment) > 255:
                return False
        return True

# Приклад використання
ip_checked0 = IPAddressChecked('1.2.3.4')
ip_checked1 = IPAddressChecked('999.29.29.29')
ip_checked2 = IPAddressChecked('199.29.29.29')

ip_checked0.display()
ip_checked1.display()
ip_checked2.display()
