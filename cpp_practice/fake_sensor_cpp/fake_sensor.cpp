#include "fake_sensor.hpp"

#include <sstream>

FakeSensor::FakeSensor(double minDistance, double maxDistance) // 构造函数，用来初始化随机数生成器，距离分布和温度分布
    : gen_(std::random_device{}()),                            // 初始化随机数生成器，std::random_device{}()是用来生成一个随机数，std::random_device是用来生成一个随机数设备
      distanceDist_(minDistance, maxDistance),                 // 初始化距离分布，minDistance是距离的最小值，maxDistance是距离的最大值
      temperatureDist_(18.0, 35.0)                             // 初始化温度分布，18.0是温度的最小值，35.0是温度的最大值
{
} // 构造函数，用来初始化随机数生成器，距离分布和温度分布

void FakeSensor::seed(unsigned value) // seed是用来设置随机数生成器的种子，value是种子值
{
  gen_.seed(value);
} // 设置随机数生成器的种子，value是种子值

double FakeSensor::readDistance()
{
  return distanceDist_(gen_); // 生成一个距离分布范围内的随机数，这里就是先从gen_生成一个随机数，然后经过distanceDist_分布，得到一个距离分布范围内的随机数
}

double FakeSensor::readTemperature()
{
  return temperatureDist_(gen_); // 生成一个温度分布范围内的随机数，这里就是先从gen_生成一个随机数，然后经过temperatureDist_分布，得到一个温度分布范围内的随机数
}

bool FakeSensor::isWarning(double distance) const
{
  return distance < WARNING_DISTANCE_M;
}

std::string FakeSensor::formatReading(int frame, double distance, double temperature) const
{
  std::ostringstream oss; // 创建一个字符串流，用来存储格式化后的字符串
  const bool warning = isWarning(distance);
  oss << "Frame " << frame << ": distance=" << distance << " m, "
      << "temp=" << temperature << " C, "
      << "status=" << (warning ? "WARNING: obstacle close" : "OK");
  return oss.str();
}
