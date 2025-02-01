import grpc
import hello_pb2
import hello_pb2_grpc

def run():
    # Sunucuya bağlan (50051 portuna)
    with grpc.insecure_channel('localhost:50051') as channel:
        # Greeter servisinin stub'ını oluştur
        stub = hello_pb2_grpc.GreeterStub(channel)
        
        # Kullanıcıdan isim al
        name = input("İsminizi girin: ")
        
        # İstek oluştur ve gönder
        response = stub.SayHello(hello_pb2.HelloRequest(name=name))
        
        # Sunucudan gelen yanıtı göster
        print("Sunucudan gelen yanıt:", response.message)

if __name__ == '__main__':
    run()