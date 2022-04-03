; Auto-generated. Do not edit!


(cl:in-package myrobot-srv)


;//! \htmlinclude SetVelocity2-request.msg.html

(cl:defclass <SetVelocity2-request> (roslisp-msg-protocol:ros-message)
  ((linear_velocity
    :reader linear_velocity
    :initarg :linear_velocity
    :type cl:float
    :initform 0.0)
   (angular_velocity
    :reader angular_velocity
    :initarg :angular_velocity
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetVelocity2-request (<SetVelocity2-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetVelocity2-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetVelocity2-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name myrobot-srv:<SetVelocity2-request> is deprecated: use myrobot-srv:SetVelocity2-request instead.")))

(cl:ensure-generic-function 'linear_velocity-val :lambda-list '(m))
(cl:defmethod linear_velocity-val ((m <SetVelocity2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:linear_velocity-val is deprecated.  Use myrobot-srv:linear_velocity instead.")
  (linear_velocity m))

(cl:ensure-generic-function 'angular_velocity-val :lambda-list '(m))
(cl:defmethod angular_velocity-val ((m <SetVelocity2-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:angular_velocity-val is deprecated.  Use myrobot-srv:angular_velocity instead.")
  (angular_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetVelocity2-request>) ostream)
  "Serializes a message object of type '<SetVelocity2-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'linear_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angular_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetVelocity2-request>) istream)
  "Deserializes a message object of type '<SetVelocity2-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear_velocity) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_velocity) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetVelocity2-request>)))
  "Returns string type for a service object of type '<SetVelocity2-request>"
  "myrobot/SetVelocity2Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetVelocity2-request)))
  "Returns string type for a service object of type 'SetVelocity2-request"
  "myrobot/SetVelocity2Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetVelocity2-request>)))
  "Returns md5sum for a message object of type '<SetVelocity2-request>"
  "7f8ecd2d213b118d540a9b1a31647365")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetVelocity2-request)))
  "Returns md5sum for a message object of type 'SetVelocity2-request"
  "7f8ecd2d213b118d540a9b1a31647365")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetVelocity2-request>)))
  "Returns full string definition for message of type '<SetVelocity2-request>"
  (cl:format cl:nil "float64 linear_velocity~%float64 angular_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetVelocity2-request)))
  "Returns full string definition for message of type 'SetVelocity2-request"
  (cl:format cl:nil "float64 linear_velocity~%float64 angular_velocity~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetVelocity2-request>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetVelocity2-request>))
  "Converts a ROS message object to a list"
  (cl:list 'SetVelocity2-request
    (cl:cons ':linear_velocity (linear_velocity msg))
    (cl:cons ':angular_velocity (angular_velocity msg))
))
;//! \htmlinclude SetVelocity2-response.msg.html

(cl:defclass <SetVelocity2-response> (roslisp-msg-protocol:ros-message)
  ((linear_velocity
    :reader linear_velocity
    :initarg :linear_velocity
    :type cl:float
    :initform 0.0)
   (angular_velocity
    :reader angular_velocity
    :initarg :angular_velocity
    :type cl:float
    :initform 0.0))
)

(cl:defclass SetVelocity2-response (<SetVelocity2-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SetVelocity2-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SetVelocity2-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name myrobot-srv:<SetVelocity2-response> is deprecated: use myrobot-srv:SetVelocity2-response instead.")))

(cl:ensure-generic-function 'linear_velocity-val :lambda-list '(m))
(cl:defmethod linear_velocity-val ((m <SetVelocity2-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:linear_velocity-val is deprecated.  Use myrobot-srv:linear_velocity instead.")
  (linear_velocity m))

(cl:ensure-generic-function 'angular_velocity-val :lambda-list '(m))
(cl:defmethod angular_velocity-val ((m <SetVelocity2-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:angular_velocity-val is deprecated.  Use myrobot-srv:angular_velocity instead.")
  (angular_velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SetVelocity2-response>) ostream)
  "Serializes a message object of type '<SetVelocity2-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'linear_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'angular_velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SetVelocity2-response>) istream)
  "Deserializes a message object of type '<SetVelocity2-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'linear_velocity) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'angular_velocity) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SetVelocity2-response>)))
  "Returns string type for a service object of type '<SetVelocity2-response>"
  "myrobot/SetVelocity2Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetVelocity2-response)))
  "Returns string type for a service object of type 'SetVelocity2-response"
  "myrobot/SetVelocity2Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SetVelocity2-response>)))
  "Returns md5sum for a message object of type '<SetVelocity2-response>"
  "7f8ecd2d213b118d540a9b1a31647365")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SetVelocity2-response)))
  "Returns md5sum for a message object of type 'SetVelocity2-response"
  "7f8ecd2d213b118d540a9b1a31647365")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SetVelocity2-response>)))
  "Returns full string definition for message of type '<SetVelocity2-response>"
  (cl:format cl:nil "float64 linear_velocity~%float64 angular_velocity~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SetVelocity2-response)))
  "Returns full string definition for message of type 'SetVelocity2-response"
  (cl:format cl:nil "float64 linear_velocity~%float64 angular_velocity~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SetVelocity2-response>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SetVelocity2-response>))
  "Converts a ROS message object to a list"
  (cl:list 'SetVelocity2-response
    (cl:cons ':linear_velocity (linear_velocity msg))
    (cl:cons ':angular_velocity (angular_velocity msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'SetVelocity2)))
  'SetVelocity2-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'SetVelocity2)))
  'SetVelocity2-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SetVelocity2)))
  "Returns string type for a service object of type '<SetVelocity2>"
  "myrobot/SetVelocity2")