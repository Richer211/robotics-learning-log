#include <iostream>
#include <random>
#include <chrono>
#include <thread>

double readFakeSensor()
{
    static std::random_device rd;
    static std::mt19937 gen(rd());
    static std::uniform_real_distribution<> dis(0.1, 5.0);
    return dis(gen);
}

int main()
{
    for (int i = 0; i < 10; i++)
    {
        double distance = readFakeSensor();
        std::cout << "Frame " << i << ": fake distance = " << distance << " meters" << std::endl;
        std::this_thread::sleep_for(std::chrono::milliseconds(500));
    }
    return 0;
}
