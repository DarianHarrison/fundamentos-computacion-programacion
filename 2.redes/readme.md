# Práctica

desde una terminal en cualquier sistema opeartivo:

verificar si los siguientes DNS'es resuelven a la direccion(ip) de los siguientes sitios

```
ping google.com
ping www.google.com
ping am.com.mx
```

ejemplo
```
C:\Users\harrisod>ping google.com

Pinging google.com [2607:f8b0:4012:819::200e] with 32 bytes of data:
Reply from 2607:f8b0:4012:819::200e: time=18ms
Reply from 2607:f8b0:4012:819::200e: time=19ms
Reply from 2607:f8b0:4012:819::200e: time=27ms
Reply from 2607:f8b0:4012:819::200e: time=15ms

Ping statistics for 2607:f8b0:4012:819::200e:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 15ms, Maximum = 27ms, Average = 19ms
```

(nota: el "ping" es casi siempre la primer herramienta para verificar si nuestra red funciona de forma adecuada).
En el ejemplo anterior, los 4 ping que mandamos llegaron exitosamente a su destino y no hubo pérdida de datos.