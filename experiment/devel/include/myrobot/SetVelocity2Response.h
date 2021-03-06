// Generated by gencpp from file myrobot/SetVelocity2Response.msg
// DO NOT EDIT!


#ifndef MYROBOT_MESSAGE_SETVELOCITY2RESPONSE_H
#define MYROBOT_MESSAGE_SETVELOCITY2RESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace myrobot
{
template <class ContainerAllocator>
struct SetVelocity2Response_
{
  typedef SetVelocity2Response_<ContainerAllocator> Type;

  SetVelocity2Response_()
    : linear_velocity(0.0)
    , angular_velocity(0.0)  {
    }
  SetVelocity2Response_(const ContainerAllocator& _alloc)
    : linear_velocity(0.0)
    , angular_velocity(0.0)  {
  (void)_alloc;
    }



   typedef double _linear_velocity_type;
  _linear_velocity_type linear_velocity;

   typedef double _angular_velocity_type;
  _angular_velocity_type angular_velocity;





  typedef boost::shared_ptr< ::myrobot::SetVelocity2Response_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::myrobot::SetVelocity2Response_<ContainerAllocator> const> ConstPtr;

}; // struct SetVelocity2Response_

typedef ::myrobot::SetVelocity2Response_<std::allocator<void> > SetVelocity2Response;

typedef boost::shared_ptr< ::myrobot::SetVelocity2Response > SetVelocity2ResponsePtr;
typedef boost::shared_ptr< ::myrobot::SetVelocity2Response const> SetVelocity2ResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::myrobot::SetVelocity2Response_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::myrobot::SetVelocity2Response_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace myrobot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'myrobot': ['/home/miki/experiment/src/myrobot/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::myrobot::SetVelocity2Response_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::myrobot::SetVelocity2Response_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::myrobot::SetVelocity2Response_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
{
  static const char* value()
  {
    return "e55b2cec3678035367208627e07de350";
  }

  static const char* value(const ::myrobot::SetVelocity2Response_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xe55b2cec36780353ULL;
  static const uint64_t static_value2 = 0x67208627e07de350ULL;
};

template<class ContainerAllocator>
struct DataType< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
{
  static const char* value()
  {
    return "myrobot/SetVelocity2Response";
  }

  static const char* value(const ::myrobot::SetVelocity2Response_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 linear_velocity\n\
float64 angular_velocity\n\
\n\
";
  }

  static const char* value(const ::myrobot::SetVelocity2Response_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.linear_velocity);
      stream.next(m.angular_velocity);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetVelocity2Response_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::myrobot::SetVelocity2Response_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::myrobot::SetVelocity2Response_<ContainerAllocator>& v)
  {
    s << indent << "linear_velocity: ";
    Printer<double>::stream(s, indent + "  ", v.linear_velocity);
    s << indent << "angular_velocity: ";
    Printer<double>::stream(s, indent + "  ", v.angular_velocity);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYROBOT_MESSAGE_SETVELOCITY2RESPONSE_H
