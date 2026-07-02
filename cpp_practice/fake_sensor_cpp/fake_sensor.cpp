#include "fake_sensor.hpp"

#include <sstream>

FakeSensor::FakeSensor(double minDistance, double maxDistance)
    : gen_(std::random_device{}()),
      distanceDist_(minDistance, maxDistance),
      temperatureDist_(18.0, 35.0)
{
}

void FakeSensor::seed(unsigned value)
{
  gen_.seed(value);
}

double FakeSensor::readDistance()
{
  return distanceDist_(gen_);
}

double FakeSensor::readTemperature()
{
  return temperatureDist_(gen_);
}

bool FakeSensor::isWarning(double distance) const
{
  return distance < WARNING_DISTANCE_M;
}

std::string FakeSensor::formatReading(int frame, double distance, double temperature) const
{
  std::ostringstream oss;
  const bool warning = isWarning(distance);
  oss << "Frame " << frame << ": distance=" << distance << " m, "
      << "temp=" << temperature << " C, "
      << "status=" << (warning ? "WARNING: obstacle close" : "OK");
  return oss.str();
}
