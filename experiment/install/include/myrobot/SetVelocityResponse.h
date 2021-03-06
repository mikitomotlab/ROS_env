// Generated by gencpp from file myrobot/SetVelocityResponse.msg
// DO NOT EDIT!


#ifndef MYROBOT_MESSAGE_SETVELOCITYRESPONSE_H
#define MYROBOT_MESSAGE_SETVELOCITYRESPONSE_H


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
struct SetVelocityResponse_
{
  typedef SetVelocityResponse_<ContainerAllocator> Type;

  SetVelocityResponse_()
    : success(false)  {
    }
  SetVelocityResponse_(const ContainerAllocator& _alloc)
    : success(false)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;





  typedef boost::shared_ptr< ::myrobot::SetVelocityResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::myrobot::SetVelocityResponse_<ContainerAllocator> const> ConstPtr;

}; // struct SetVelocityResponse_

typedef ::myrobot::SetVelocityResponse_<std::allocator<void> > SetVelocityResponse;

typedef boost::shared_ptr< ::myrobot::SetVelocityResponse > SetVelocityResponsePtr;
typedef boost::shared_ptr< ::myrobot::SetVelocityResponse const> SetVelocityResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::myrobot::SetVelocityResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::myrobot::SetVelocityResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace myrobot

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::myrobot::SetVelocityResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::myrobot::SetVelocityResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::myrobot::SetVelocityResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "358e233cde0c8a8bcfea4ce193f8fc15";
  }

  static const char* value(const ::myrobot::SetVelocityResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x358e233cde0c8a8bULL;
  static const uint64_t static_value2 = 0xcfea4ce193f8fc15ULL;
};

template<class ContainerAllocator>
struct DataType< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "myrobot/SetVelocityResponse";
  }

  static const char* value(const ::myrobot::SetVelocityResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n\
\n\
";
  }

  static const char* value(const ::myrobot::SetVelocityResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetVelocityResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::myrobot::SetVelocityResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::myrobot::SetVelocityResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MYROBOT_MESSAGE_SETVELOCITYRESPONSE_H
