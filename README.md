# 习佳佳：打造爆款中文编程语言（逃）

```cpp
#包含 <输入输出之流>

整数 主函数() {
    标准库::标准输出流 << "你好，世界！" << 标准库::行结束符;
    返回 0;
}
```

## 如何添加关键字

`table.txt` 中包含了要转换的关键字列表，欢迎通过 PR 贡献可能遗漏的字词：）

## 习佳佳 -> C++

将习佳佳语言的源文件 `hello.xjj` 转换为 C++：
```bash
./compile.py hello.xjj -o hello.cpp
```

## C++ -> 习佳佳

将 C++ 源文件 `hello.cpp` 转换为习佳佳语言：
```bash
./compile.py -d hello.cpp -o hello.xjj
```
