基本介绍
Rust是一门系统编程语言,注重安全性和性能。它具有以下主要特征:
1. 安全且高效。Rust通过其独特的所有权系统和 borrowing 检查机制实现了内存安全,而不会影响性能。
2. 快速和轻量级。Rust编译器产生的代码与 C/C++ 同等速度和体积。
3. 表达力丰富。Rust拥有丰富的语法,支持泛型、Traits、模式匹配、类型推导等特性。
4. 可管理的性能。Rust提供了很好的控制性能的手段,通过所有权、类型系统,可以达到"零成本抽象"。
5. 并发支持。Rust原生支持并发,其所有权系统确保了并发程序的安全。

安装部署
● 如果是mac下面，直接运行下面这句
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


Helloworld编程
● 下面这个脚本复制成hello.rs
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Hello World!");
}
● 在命令行之下运行
rustc hello.rs
./hello
● 然后就得到结果



参考材料
● https://doc.rust-lang.org/rust-by-example/hello.html
● https://www.rust-lang.org/zh-CN/tools/install
