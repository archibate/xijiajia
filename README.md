# xijiajia
论如何把C++变成中文编程语言（习佳佳）

`table.txt` 中包含了要转换的关键字列表

将习佳佳中文编程语言的源文件 `你好.习佳佳` 转换为 C++：
```bash
./compile.py 你好.习佳佳 hello.cpp
```

将 C++ 源文件 `hello.cpp` 转换为习佳佳中文编程语言：
```bash
./compile.py --en2cn hello.cpp 你好.习佳佳
```
