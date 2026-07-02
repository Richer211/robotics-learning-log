#include "fake_sensor.hpp"

#include <chrono>
#include <fstream>
#include <iostream>
#include <thread>

int main()
{
  FakeSensor sensor;
  const int frames = 10;
  std::ofstream logFile("sensor_log.txt");

  std::cout << "Starting C++ sensor simulation..." << std::endl;
  sensor.seed(42);
  for (int i = 0; i < frames; ++i)
  {
    const double distance = sensor.readDistance();
    const double temperature = sensor.readTemperature();
    const std::string line = sensor.formatReading(i, distance, temperature);

    std::cout << line << std::endl;
    logFile << line << std::endl;

    std::this_thread::sleep_for(std::chrono::milliseconds(10));
  }

  std::cout << "Saved readings to sensor_log.txt" << std::endl;
  return 0;
}
