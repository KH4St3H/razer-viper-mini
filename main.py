'''

Simple script to use razer viper mini in linux

'''

import sys
from gui import Window

try:
    from openrazer.client import DeviceManager, __version__
    from openrazer.client.fx import SingleLed

except ImportError:
    print('Could not detect openrazer library, try installing it first')
    sys.exit(0)

if int(__version__[:__version__.find('.')])<3:
    print('Razer viper mini requires openrazer>=3')
    sys.exit(0)



if __name__=='__main__':
    device_manager = DeviceManager()
    devices = device_manager.devices

    mouse = None
    for dev in devices:
        if dev.name=='Razer Viper Mini':
            mouse = dev
            break

    if not mouse:
        print('Could not detect mouse')
        sys.exit(0)

    led_manager = SingleLed(mouse.serial, mouse.capabilities)

    window = Window(mouse, led_manager)
    window.run()
