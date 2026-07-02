#include <iostream>
#include <random>

int main()
{
    std::mt19937 gen(42); // 创建随机引擎，种子为42，每次运行都一样，也可以改成99或者任意整数，只是不同的起点而已
    std::uniform_real_distribution<> dist(0.1, 5.0);

    for (int i = 0; i < 10; i++)
    {
        std::cout << dist(gen) << "\n";
    }
}
// 先创建随机引擎 gen(种子)，再创建均匀分布 dist(0.1, 5.0)。
// 循环里每次 dist(gen)：从 gen 取随机性，经 dist 变换成 [0.1, 5.0] 的浮点数并打印。
// 同一种子重复运行，序列相同；换种子则序列不同。