import socket
import serial

# 아두이노 연결 설정
arduino = serial.Serial('/dev/ttyUSB0', 9600)

host='0.0.0.0'
port=12345

# 소켓 설정
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Server listening on {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # 데이터 수신
    data = client_socket.recv(1024).decode()
    if not data:
        break
    print(f"Received data: {data}")

    # 데이터 파싱
    speed, car_type = data.split(',')  # 데이터 형식: "30,소형"
    speed = int(speed)
    
     #속도 값에 따라 아두이노로 모터 각도 전송
    if speed >= 10 and speed <= 30:
        if car_type == 'small':
            arduino.write(b'30\n')
        elif car_type == 'medium':
            arduino.write(b'40\n')
        elif car_type == 'big':
            arduino.write(b'50\n')
    elif speed > 30:
        arduino.write(b'60\n')
    else:
        arduino.write(b'0\n')


    client_socket.close()

