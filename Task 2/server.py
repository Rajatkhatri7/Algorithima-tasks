import socketio
import eventlet

sio = socketio.Server()

@sio.event
def connect(sid,enviorn):
    print('Client connected:', sid)

@sio.event
def disconnect(sid):
    print('Client disconnected:', sid)
        
@sio.on('recieve_msg')
def on_random(sid, data):
    print(f"Received message {data} : {sid}")
    sio.emit('receive_data', 'hi from server')

if __name__ == '__main__':
    
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
