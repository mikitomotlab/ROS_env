// Generated by gencpp from file myrobot/SetVelocity.msg
// DO NOT EDIT!


#ifndef MYROBOT_MESSAGE_SETVELOCITY_H
#define MYROBOT_MESSAGE_SETVELOCITY_H

#include <ros/service_traits.h>


#include <myrobot/SetVelocityRequest.h>
#include <myrobot/SetVelocityResponse.h>


namespace myrobot
{

struct SetVelocity
{

typedef SetVelocityRequest Request;
typedef SetVelocityResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetVelocity
} // namespace myrobot


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::myrobot::SetVelocity > {
  static const char* value()
  {
    return "f6aaad2e58fe90e46753c2e927c41798";
  }

  static const char* value(const ::myrobot::SetVelocity&) { return value(); }
};

template<>
struct DataType< ::myrobot::SetVelocity > {
  static const char* value()
  {
    return "myrobot/SetVelocity";
  }

  static const char* value(const ::myrobot::SetVelocity&) { return value(); }
};


// service_traits::MD5Sum< ::myrobot::SetVelocityRequest> should match 
// service_traits::MD5Sum< ::myrobot::SetVelocity > 
template<>
struct MD5Sum< ::myrobot::SetVelocityRequest>
{
  static const char* value()
  {
    return MD5Sum< ::myrobot::SetVelocity >::value();
  }
  static const char* value(const ::myrobot::SetVelocityRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::myrobot::SetVelocityRequest> should match 
// service_traits::DataType< ::myrobot::SetVelocity > 
template<>
struct DataType< ::myrobot::SetVelocityRequest>
{
  static const char* value()
  {
    return DataType< ::myrobot::SetVelocity >::value();
  }
  static const char* value(const ::myrobot::SetVelocityRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::myrobot::SetVelocityResponse> should match 
// service_traits::MD5Sum< ::myrobot::SetVelocity > 
template<>
struct MD5Sum< ::myrobot::SetVelocityResponse>
{
  static const char* value()
  {
    return MD5Sum< ::myrobot::SetVelocity >::value();
  }
  static const char* value(const ::myrobot::SetVelocityResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::myrobot::SetVelocityResponse> should match 
// service_traits::DataType< ::myrobot::SetVelocity > 
template<>
struct DataType< ::myrobot::SetVelocityResponse>
{
  static const char* value()
  {
    return DataType< ::myrobot::SetVelocity >::value();
  }
  static const char* value(const ::myrobot::SetVelocityResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MYROBOT_MESSAGE_SETVELOCITY_H
