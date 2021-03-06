import socket
import threading


# 主线程　专门以　接收屏幕输入　－－－－> 发送　－－退出
# 创建一个子线程　专门用来收数据

def send_msg(udp_socket):
    """发送一次数据"""
    data = input("请输入你想说的话:")
    IP = input('请输入你想要聊天的ＩＰ地址:')
    port = int(input("请输入对方使用的端口:"))
    udp_socket.sendto(data.encode(), (IP, port))


def recv_msg(udp_socket):
    """循环接收数据"""
    while True:
        data, remote_address = udp_socket.recvfrom(4096)
        print("接收到来自%s 的数据:%s" % (str(remote_address), data.decode()))


def main():
    # 创建ＵＤＰ套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(('', 9999))

    # 创建一个子线程收数据
    recv_thd = threading.Thread(target=recv_msg, args=(udp_socket,))
    recv_thd.start()

    while True:
        op = input("请输入你要进行的操作: 1 发送数据　２接收数据　３退出")
        if op == '1':
            send_msg(udp_socket)
        # elif op == '2':
        #     recv_msg(udp_socket)
        elif op == '3':
            break
        else:
            print("你输入有误")

    # 关掉套接字
    udp_socket.close()

if __name__ == '__main__':
    main()