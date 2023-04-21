import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

    
@sio.event
def receive_data(data):
    print(f"Received random msg {data}")


if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.emit('recieve_msg', 'hello from client')
    sio.wait()