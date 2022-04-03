// Generated by gencpp from file myrobot/d_position.msg
// DO NOT EDIT!


#ifndef MYROBOT_MESSAGE_D_POSITION_H
#define MYROBOT_MESSAGE_D_POSITION_H

#include <ros/service_traits.h>


#include <myrobot/d_positionRequest.h>
#include <myrobot/d_positionResponse.h>


namespace myrobot
{

struct d_position
{

typedef d_positionRequest Request;
typedef d_positionResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct d_position
} // namespace myrobot


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::myrobot::d_position > {
  static const char* value()
  {
    return "f82f197a7f2c41cf8d240b3b8b2f9316";
  }

  static const char* value(const ::myrobot::d_position&) { return value(); }
};

template<>
struct DataType< ::myrobot::d_position > {
  static const char* value()
  {
    return "myrobot/d_position";
  }

  static const char* value(const ::myrobot::d_position&) { return value(); }
};


// service_traits::MD5Sum< ::myrobot::d_positionRequest> should match 
// service_traits::MD5Sum< ::myrobot::d_position > 
template<>
struct MD5Sum< ::myrobot::d_positionRequest>
{
  static const char* value()
  {
    return MD5Sum< ::myrobot::d_position >::value();
  }
  static const char* value(const ::myrobot::d_positionRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::myrobot::d_positionRequest> should match 
// service_traits::DataType< ::myrobot::d_position > 
template<>
struct DataType< ::myrobot::d_positionRequest>
{
  static const char* value()
  {
    return DataType< ::myrobot::d_position >::value();
  }
  static const char* value(const ::myrobot::d_positionRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::myrobot::d_positionResponse> should match 
// service_traits::MD5Sum< ::myrobot::d_position > 
template<>
struct MD5Sum< ::myrobot::d_positionResponse>
{
  static const char* value()
  {
    return MD5Sum< ::myrobot::d_position >::value();
  }
  static const char* value(const ::myrobot::d_positionResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::myrobot::d_positionResponse> should match 
// service_traits::DataType< ::myrobot::d_position > 
template<>
struct DataType< ::myrobot::d_positionResponse>
{
  static const char* value()
  {
    return DataType< ::myrobot::d_position >::value();
  }
  static const char* value(const ::myrobot::d_positionResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MYROBOT_MESSAGE_D_POSITION_H
