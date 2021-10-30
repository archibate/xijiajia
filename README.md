# 习佳佳：打造爆款中文编程语言（逃）

`table.txt` 中包含了要转换的关键字列表，欢迎通过 PR 贡献可能遗漏的字词：）

## 习佳佳 -> C++

将习佳佳语言的源文件 `你好.习佳佳` 转换为 C++：
```bash
./compile.py 你好.习佳佳 -o hello.cpp
```

## C++ -> 习佳佳

将 C++ 源文件 `hello.cpp` 转换为习佳佳语言：
```bash
./compile.py -d hello.cpp -o 你好.习佳佳
```
