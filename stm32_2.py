
import usb.core
import usb.util

# 找到 CH340 设备（VID:PID 为 1a86:7523）
dev = usb.core.find(idVendor=0x1A86, idProduct=0x7523)
if dev is None:
    print("找不到 CH340 设备，请检查连接和授权")
    exit()

# 配置设备
dev.set_configuration()
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    custom_match = \
    lambda e: \
        e.bEndpointAddress & usb.util.ENDPOINT_IN
)

out_ep = usb.util.find_descriptor(
    intf,
    custom_match = \
    lambda e: \
        e.bEndpointAddress & usb.util.ENDPOINT_OUT
)

print("=== STM32 LED 控制器 ===")
print("指令：1=亮  0=灭  s=翻转  q=退出\n")

while True:
    cmd = input("输入指令：")
    if cmd == "q":
        break
    out_ep.write(cmd.encode())
    # 读取返回信息
    try:
        data = ep.read(64, timeout=500)
        print(data.decode('utf-8', errors='ignore'))
    except usb.core.USBError:
        pass

usb.util.dispose_resources(dev)
