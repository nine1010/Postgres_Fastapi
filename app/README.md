# Notice 
ยังไม่สามารถ create/read/update ผ่านทาง API route ต่างๆ ได้ เนื่องจากติดปัญหาด้าน database refuse access เมื่อดึงผ่าน API


Error ทีพบ

`conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Connection refused (0x0000274D/10061)
        Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused (0x0000274D/10061)
        Is the server running on that host and accepting TCP/IP connections?`