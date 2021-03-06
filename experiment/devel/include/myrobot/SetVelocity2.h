// Generated by gencpp from file myrobot/SetVelocity2.msg
// DO NOT EDIT!


#ifndef MYROBOT_MESSAGE_SETVELOCITY2_H
#define MYROBOT_MESSAGE_SETVELOCITY2_H

#include <ros/service_traits.h>


#include <myrobot/SetVelocity2Request.h>
#include <myrobot/SetVelocity2Response.h>


namespace myrobot
{

struct SetVelocity2
{

typedef SetVelocity2Request Request;
typedef SetVelocity2Response Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetVelocity2
} // namespace myrobot


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::myrobot::SetVelocity2 > {
  static const char* value()
  {
    return "7f8ecd2d213b118d540a9b1a31647365";
  }

  static const char* value(const ::myrobot::SetVelocity2&) { return value(); }
};

template<>
struct DataType< ::myrobot::SetVelocity2 > {
  static const char* value()
  {
    return "myrobot/SetVelocity2";
  }

  static const char* value(const ::myrobot::SetVelocity2&) { return value(); }
};


// service_traits::MD5Sum< ::myrobot::SetVelocity2Request> should match 
// service_traits::MD5Sum< ::myrobot::SetVelocity2 > 
template<>
struct MD5Sum< ::myrobot::SetVelocity2Request>
{
  static const char* value()
  {
    return MD5Sum< ::myrobot::SetVelocity2 >::value();
  }
  static const char* value(const ::myrobot::SetVelocity2Request&)
  {
    return value();
  }
};

// service_traits::DataType< ::myrobot::SetVelocity2Request> should match 
// service_traits::DataType< ::myrobot::SetVelocity2 > 
template<>
struct DataType< ::myrobot::SetVelocity2Request>
{
  static const char* value()
  {
    return DataType< ::myrobot::SetVelocity2 >::value();
  }
  static const char* value(const ::myrobot::SetVelocity2Request&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::myrobot::SetVelocity2Response> should match 
// service_traits::MD5Sum< ::myrobot::SetVelocity2 > 
template<>
struct MD5Sum< ::myrobot::SetVelocity2Response>
{
  static const char* value()
  {
    return MD5Sum< ::myrobot::SetVelocity2 >::value();
  }
  static const char* value(const ::myrobot::SetVelocity2Response&)
  {
    return value();
  }
};

// service_traits::DataType< ::myrobot::SetVelocity2Response> should match 
// service_traits::DataType< ::myrobot::SetVelocity2 > 
template<>
struct DataType< ::myrobot::SetVelocity2Response>
{
  static const char* value()
  {
    return DataType< ::myrobot::SetVelocity2 >::value();
  }
  static const char* value(const ::myrobot::SetVelocity2Response&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MYROBOT_MESSAGE_SETVELOCITY2_H
