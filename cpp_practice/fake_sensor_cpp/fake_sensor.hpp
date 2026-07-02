#pragma once

#include <random>
#include <string>

class FakeSensor
{
public:
  FakeSensor(double minDistance = 0.1, double maxDistance = 5.0);

  double readDistance();
  double readTemperature();
  bool isWarning(double distance) const;
  void seed(unsigned value);

  static constexpr double WARNING_DISTANCE_M = 0.8;

  std::string formatReading(int frame, double distance, double temperature) const;

private:
  std::mt19937 gen_;
  std::uniform_real_distribution<> distanceDist_;
  std::uniform_real_distribution<> temperatureDist_;
};
