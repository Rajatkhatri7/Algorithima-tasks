import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.event
def send_message():
    sio.emit(event='response',data = {'message':'client sends a message'})
    print("data sent to server")
    
@sio.event
def receive_data(data):
    print(f"Received random value {data} from server")


if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    sio.emit('recieve_msg', 'hello from client')
    sio.wait()