import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

# Greeter servisini implement eden sınıf
class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        # Gelen istekteki ismi al ve selamlama mesajı oluştur
        message = f"Merhaba {request.name}!"
        # Yanıt mesajını oluştur ve gönder
        return hello_pb2.HelloResponse(message=message)

def serve():
    # Sunucu oluştur
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Servisi sunucuya ekle
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    
    # Portu dinlemeye başla
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Sunucu başlatıldı. Port: 50051")
    
    # Sunucuyu çalışır durumda tut
    server.wait_for_termination()

if __name__ == '__main__':
    serve()