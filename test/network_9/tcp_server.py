
import socket

def main():
    # 创建TCP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 端口复用，避免重启提示占用
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', 8888))
    server_socket.listen(128)
    print("服务端已启动，监听 8888 端口...")

    while True:
        try:
            client_socket, client_addr = server_socket.accept()
            print(f"客户端连接: {client_addr}")

            full_data = b""
            # 限制最大接收1024字节，防止恶意发包
            while len(full_data) < 1024:
                chunk = client_socket.recv(1)
                if not chunk:
                    break
                full_data += chunk
                if chunk in (b'\n', b'\r'):
                    break

            if full_data:
                text = full_data.decode('utf-8').strip()
                print(f"收到: {text}")
                response = f"服务端收到: {text}\n".encode('utf-8')
                client_socket.send(response)

        except Exception as e:
            print(f"异常: {e}")
        finally:
            client_socket.close()
            print("客户端连接已关闭\n")

if __name__ == '__main__':
    main()
