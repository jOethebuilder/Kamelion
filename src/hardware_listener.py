import time
import re
import threading
import serial
import serial.tools.list_ports

class KamelionHardwareListener:
    def __init__(self, callback_on_data_received=None):
        self.callback = callback_on_data_received
        self.is_running = False
        self.serial_connection = None
        self.listener_thread = None
        self.target_port = None
        self.data_pattern = re.compile(r"TD:\s*([\d.]+),\s*HEX:\s*(#[a-fA-F0-9]{6})")

    def start_background_scanning(self):
        if not self.is_running:
            self.is_running = True
            self.listener_thread = threading.Thread(target=self._port_monitoring_loop, daemon=True)
            self.listener_thread.start()

    def stop_background_scanning(self):
        self.is_running = False
        if self.serial_connection:
            try:
                self.serial_connection.close()
            except Exception:
                pass

    def execute_hardware_port_reset(self):
        if self.target_port:
            try:
                conn = serial.Serial(self.target_port, 115200, timeout=1.0)
                conn.setDTR(False)
                conn.setRTS(False)
                time.sleep(0.1)
                conn.setDTR(True)
                conn.setRTS(True)
                conn.close()
                return True
            except Exception:
                pass
        return False

    def _port_monitoring_loop(self):
        while self.is_running:
            if not self.serial_connection:
                ports = list(serial.tools.list_ports.comports())
                for p in ports:
                    if "usb" in p.description.lower() or "pico" in p.description.lower() or "serial" in p.description.lower():
                        try:
                            self.target_port = p.device
                            self.serial_connection = serial.Serial(p.device, 115200, timeout=1.0)
                            break
                        except Exception:
                            pass
                if not self.serial_connection:
                    time.sleep(2.0)
                    continue
            try:
                if self.serial_connection.in_waiting > 0:
                    line = self.serial_connection.readline().decode('utf-8', errors='ignore').strip()
                    match = self.data_pattern.search(line)
                    if match and self.callback:
                        self.callback(float(match.group(1)), match.group(2))
                else:
                    time.sleep(0.1)
            except Exception:
                self.serial_connection = None
                time.sleep(2.0)
