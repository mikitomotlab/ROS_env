// Auto-generated. Do not edit!

// (in-package myrobot.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetVelocity2Request {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.linear_velocity = null;
      this.angular_velocity = null;
    }
    else {
      if (initObj.hasOwnProperty('linear_velocity')) {
        this.linear_velocity = initObj.linear_velocity
      }
      else {
        this.linear_velocity = 0.0;
      }
      if (initObj.hasOwnProperty('angular_velocity')) {
        this.angular_velocity = initObj.angular_velocity
      }
      else {
        this.angular_velocity = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetVelocity2Request
    // Serialize message field [linear_velocity]
    bufferOffset = _serializer.float64(obj.linear_velocity, buffer, bufferOffset);
    // Serialize message field [angular_velocity]
    bufferOffset = _serializer.float64(obj.angular_velocity, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetVelocity2Request
    let len;
    let data = new SetVelocity2Request(null);
    // Deserialize message field [linear_velocity]
    data.linear_velocity = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [angular_velocity]
    data.angular_velocity = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'myrobot/SetVelocity2Request';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e55b2cec3678035367208627e07de350';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 linear_velocity
    float64 angular_velocity
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetVelocity2Request(null);
    if (msg.linear_velocity !== undefined) {
      resolved.linear_velocity = msg.linear_velocity;
    }
    else {
      resolved.linear_velocity = 0.0
    }

    if (msg.angular_velocity !== undefined) {
      resolved.angular_velocity = msg.angular_velocity;
    }
    else {
      resolved.angular_velocity = 0.0
    }

    return resolved;
    }
};

class SetVelocity2Response {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.linear_velocity = null;
      this.angular_velocity = null;
    }
    else {
      if (initObj.hasOwnProperty('linear_velocity')) {
        this.linear_velocity = initObj.linear_velocity
      }
      else {
        this.linear_velocity = 0.0;
      }
      if (initObj.hasOwnProperty('angular_velocity')) {
        this.angular_velocity = initObj.angular_velocity
      }
      else {
        this.angular_velocity = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetVelocity2Response
    // Serialize message field [linear_velocity]
    bufferOffset = _serializer.float64(obj.linear_velocity, buffer, bufferOffset);
    // Serialize message field [angular_velocity]
    bufferOffset = _serializer.float64(obj.angular_velocity, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetVelocity2Response
    let len;
    let data = new SetVelocity2Response(null);
    // Deserialize message field [linear_velocity]
    data.linear_velocity = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [angular_velocity]
    data.angular_velocity = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a service object
    return 'myrobot/SetVelocity2Response';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e55b2cec3678035367208627e07de350';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 linear_velocity
    float64 angular_velocity
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetVelocity2Response(null);
    if (msg.linear_velocity !== undefined) {
      resolved.linear_velocity = msg.linear_velocity;
    }
    else {
      resolved.linear_velocity = 0.0
    }

    if (msg.angular_velocity !== undefined) {
      resolved.angular_velocity = msg.angular_velocity;
    }
    else {
      resolved.angular_velocity = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: SetVelocity2Request,
  Response: SetVelocity2Response,
  md5sum() { return '7f8ecd2d213b118d540a9b1a31647365'; },
  datatype() { return 'myrobot/SetVelocity2'; }
};
