# 习佳佳：打造爆款中文编程语言（逃）

```cpp
#include "xijiajia.h"

整数 主函数() {
    标准库::标准输出流 << "你好，世界！" << 标准库::行结束符;
    返回 0;
}
```

```cpp
#include "xijiajia.h"

整型 主函数() {
    标准库::矢量<整型> 数的矢量;
    循环 (整型 数 = 0; 数 < 32; 数++) {
        数的矢量.推入至末尾((数 * 114514 + 31415) % 256);
    }
    排序(开始(数的矢量), 结束(数的矢量));
    循环 (自动 数: 数的矢量) {
        标准库::标准输出流 << 数 << 标准库::行结束符;
    }
    返回 0;
}
```

## 使用方法

只需将本仓库中的 `xijiajia.h` 这个文件，和你要编译的 `.cpp` 源文件，放在同一个目录，然后 `#include "xijiajia.h"` ，就可以开启中文编程啦！
Windows 用户请注意将编辑器（IDE）切换到 UTF-8 编码格式，方便编译器识别。

## 工作原理

利用了 C++11 的变量名（包括宏名）可以为任意 UTF-8 字符串的特性，在 `xijiajia.h` 中包含了一堆形如 `#define 主函数 main` 的宏定义，从而在预处理期
完成中译英的转换，可以看做是要转换的关键字列表，欢迎通过 PR 贡献可能遗漏的字词：）

## 另一种使用方式……

使用单头文件虽然容易，但美中不足的是像 `#include` 这样的宏指令没办法使用中文编程，因此我们还可以借助 `compile.py` 实现习佳佳和 C++ 之间的转换。

将习佳佳语言的源文件 `hello.xjj` 转换为 C++：
```bash
./compile.py hello.xjj -o hello.cpp
```

将 C++ 源文件 `hello.cpp` 转换为习佳佳语言：
```bash
./compile.py -d hello.cpp -o hello.xjj
```
