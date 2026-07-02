#pragma once

#include <random>
#include <string>

class FakeSensor
{
public:
  FakeSensor(double minDistance = 0.1, double maxDistance = 5.0); // 构造函数，可以用来初始化随机数生成器，温度和距离分布的分布范围

  double readDistance();                 // double类型的读取距离方法
  double readTemperature();              // double类型的读取温度
  bool isWarning(double distance) const; // 这里的const表示这个方法不会修改类的成员变量
  void seed(unsigned value);             // void类型的seed方法，用来设置随机数生成种子

  static constexpr double WARNING_DISTANCE_M = 0.8; // 警告距离，表示距离传感器读取的距离小于0.8米时，表示有障碍物

  std::string formatReading(int frame, double distance, double temperature) const; // 格式化读取到的距离和温度，返回一个字符串 且const表示这个方法不会修改类的成员变量

private:
  std::mt19937 gen_;                                 // 产生随机数的生成器
  std::uniform_real_distribution<> distanceDist_;    // 落在距离分布范围内的随机数,可以让随机数落在这个范围内,distanceDist_是距离分布的分布范围
  std::uniform_real_distribution<> temperatureDist_; // 落在温度分布范围内的随机数,可以让随机数落在这个范围内,temperatureDist_是温度分布的分布范围
};
