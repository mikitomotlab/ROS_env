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

class d_positionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.dx = null;
      this.dy = null;
      this.dth = null;
    }
    else {
      if (initObj.hasOwnProperty('dx')) {
        this.dx = initObj.dx
      }
      else {
        this.dx = 0.0;
      }
      if (initObj.hasOwnProperty('dy')) {
        this.dy = initObj.dy
      }
      else {
        this.dy = 0.0;
      }
      if (initObj.hasOwnProperty('dth')) {
        this.dth = initObj.dth
      }
      else {
        this.dth = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type d_positionRequest
    // Serialize message field [dx]
    bufferOffset = _serializer.float64(obj.dx, buffer, bufferOffset);
    // Serialize message field [dy]
    bufferOffset = _serializer.float64(obj.dy, buffer, bufferOffset);
    // Serialize message field [dth]
    bufferOffset = _serializer.float64(obj.dth, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type d_positionRequest
    let len;
    let data = new d_positionRequest(null);
    // Deserialize message field [dx]
    data.dx = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [dy]
    data.dy = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [dth]
    data.dth = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'myrobot/d_positionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'dd3d01521300016efa8257bacff641ee';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 dx
    float64 dy
    float64 dth
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new d_positionRequest(null);
    if (msg.dx !== undefined) {
      resolved.dx = msg.dx;
    }
    else {
      resolved.dx = 0.0
    }

    if (msg.dy !== undefined) {
      resolved.dy = msg.dy;
    }
    else {
      resolved.dy = 0.0
    }

    if (msg.dth !== undefined) {
      resolved.dth = msg.dth;
    }
    else {
      resolved.dth = 0.0
    }

    return resolved;
    }
};

class d_positionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.th = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('th')) {
        this.th = initObj.th
      }
      else {
        this.th = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type d_positionResponse
    // Serialize message field [x]
    bufferOffset = _serializer.float64(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float64(obj.y, buffer, bufferOffset);
    // Serialize message field [th]
    bufferOffset = _serializer.float64(obj.th, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type d_positionResponse
    let len;
    let data = new d_positionResponse(null);
    // Deserialize message field [x]
    data.x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [th]
    data.th = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 24;
  }

  static datatype() {
    // Returns string type for a service object
    return 'myrobot/d_positionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '000e435776f4fd6ba555d25d7a61ed8f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 x
    float64 y
    float64 th
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new d_positionResponse(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.th !== undefined) {
      resolved.th = msg.th;
    }
    else {
      resolved.th = 0.0
    }

    return resolved;
    }
};

module.exports = {
  Request: d_positionRequest,
  Response: d_positionResponse,
  md5sum() { return 'f82f197a7f2c41cf8d240b3b8b2f9316'; },
  datatype() { return 'myrobot/d_position'; }
};
