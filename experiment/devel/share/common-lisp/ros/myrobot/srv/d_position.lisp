; Auto-generated. Do not edit!


(cl:in-package myrobot-srv)


;//! \htmlinclude d_position-request.msg.html

(cl:defclass <d_position-request> (roslisp-msg-protocol:ros-message)
  ((dx
    :reader dx
    :initarg :dx
    :type cl:float
    :initform 0.0)
   (dy
    :reader dy
    :initarg :dy
    :type cl:float
    :initform 0.0)
   (dth
    :reader dth
    :initarg :dth
    :type cl:float
    :initform 0.0))
)

(cl:defclass d_position-request (<d_position-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <d_position-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'd_position-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name myrobot-srv:<d_position-request> is deprecated: use myrobot-srv:d_position-request instead.")))

(cl:ensure-generic-function 'dx-val :lambda-list '(m))
(cl:defmethod dx-val ((m <d_position-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:dx-val is deprecated.  Use myrobot-srv:dx instead.")
  (dx m))

(cl:ensure-generic-function 'dy-val :lambda-list '(m))
(cl:defmethod dy-val ((m <d_position-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:dy-val is deprecated.  Use myrobot-srv:dy instead.")
  (dy m))

(cl:ensure-generic-function 'dth-val :lambda-list '(m))
(cl:defmethod dth-val ((m <d_position-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:dth-val is deprecated.  Use myrobot-srv:dth instead.")
  (dth m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <d_position-request>) ostream)
  "Serializes a message object of type '<d_position-request>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'dx))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'dy))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'dth))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <d_position-request>) istream)
  "Deserializes a message object of type '<d_position-request>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dx) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dy) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dth) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<d_position-request>)))
  "Returns string type for a service object of type '<d_position-request>"
  "myrobot/d_positionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'd_position-request)))
  "Returns string type for a service object of type 'd_position-request"
  "myrobot/d_positionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<d_position-request>)))
  "Returns md5sum for a message object of type '<d_position-request>"
  "f82f197a7f2c41cf8d240b3b8b2f9316")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'd_position-request)))
  "Returns md5sum for a message object of type 'd_position-request"
  "f82f197a7f2c41cf8d240b3b8b2f9316")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<d_position-request>)))
  "Returns full string definition for message of type '<d_position-request>"
  (cl:format cl:nil "float64 dx~%float64 dy~%float64 dth~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'd_position-request)))
  "Returns full string definition for message of type 'd_position-request"
  (cl:format cl:nil "float64 dx~%float64 dy~%float64 dth~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <d_position-request>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <d_position-request>))
  "Converts a ROS message object to a list"
  (cl:list 'd_position-request
    (cl:cons ':dx (dx msg))
    (cl:cons ':dy (dy msg))
    (cl:cons ':dth (dth msg))
))
;//! \htmlinclude d_position-response.msg.html

(cl:defclass <d_position-response> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (th
    :reader th
    :initarg :th
    :type cl:float
    :initform 0.0))
)

(cl:defclass d_position-response (<d_position-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <d_position-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'd_position-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name myrobot-srv:<d_position-response> is deprecated: use myrobot-srv:d_position-response instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <d_position-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:x-val is deprecated.  Use myrobot-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <d_position-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:y-val is deprecated.  Use myrobot-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'th-val :lambda-list '(m))
(cl:defmethod th-val ((m <d_position-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-srv:th-val is deprecated.  Use myrobot-srv:th instead.")
  (th m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <d_position-response>) ostream)
  "Serializes a message object of type '<d_position-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'th))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <d_position-response>) istream)
  "Deserializes a message object of type '<d_position-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'th) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<d_position-response>)))
  "Returns string type for a service object of type '<d_position-response>"
  "myrobot/d_positionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'd_position-response)))
  "Returns string type for a service object of type 'd_position-response"
  "myrobot/d_positionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<d_position-response>)))
  "Returns md5sum for a message object of type '<d_position-response>"
  "f82f197a7f2c41cf8d240b3b8b2f9316")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'd_position-response)))
  "Returns md5sum for a message object of type 'd_position-response"
  "f82f197a7f2c41cf8d240b3b8b2f9316")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<d_position-response>)))
  "Returns full string definition for message of type '<d_position-response>"
  (cl:format cl:nil "float64 x~%float64 y~%float64 th~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'd_position-response)))
  "Returns full string definition for message of type 'd_position-response"
  (cl:format cl:nil "float64 x~%float64 y~%float64 th~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <d_position-response>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <d_position-response>))
  "Converts a ROS message object to a list"
  (cl:list 'd_position-response
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':th (th msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'd_position)))
  'd_position-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'd_position)))
  'd_position-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'd_position)))
  "Returns string type for a service object of type '<d_position>"
  "myrobot/d_position")