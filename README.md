# gRPC Python Örneği

Bu repo, gRPC kullanarak basit bir istemci-sunucu uygulaması örneğini içerir. Uygulama, kullanıcıdan bir isim alıp "Merhaba [isim]!" şeklinde yanıt veren basit bir selamlama servisi sunar.

## Dosyalar

- `hello.proto`: gRPC servis tanımlaması
- `server.py`: gRPC sunucu uygulaması
- `client.py`: gRPC istemci uygulaması
- `hello_pb2.py`: Protocol Buffers tarafından oluşturulan Python kodu
- `hello_pb2_grpc.py`: gRPC tarafından oluşturulan Python kodu

## Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install grpcio grpcio-tools
```

2. Proto dosyasından Python kodlarını oluşturun:
```bash
python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. hello.proto
```

## Çalıştırma

1. Sunucuyu başlatın:
```bash
python server.py
```

2. Yeni bir terminal açın ve istemciyi çalıştırın:
```bash
python client.py
```

3. İstemci çalıştığında size isminizi soracak. İsminizi girin ve sunucudan gelen yanıtı görün.

## Medium Blog Post

Bu örnek kod, gRPC'yi Python ile nasıl kullanacağınızı anlatan Medium blog yazısı için hazırlanmıştır. Detaylı açıklamalar için blog yazısını okuyabilirsiniz. 