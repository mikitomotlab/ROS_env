; Auto-generated. Do not edit!


(cl:in-package myrobot-msg)


;//! \htmlinclude dpos.msg.html

(cl:defclass <dpos> (roslisp-msg-protocol:ros-message)
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

(cl:defclass dpos (<dpos>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <dpos>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'dpos)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name myrobot-msg:<dpos> is deprecated: use myrobot-msg:dpos instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <dpos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-msg:x-val is deprecated.  Use myrobot-msg:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <dpos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-msg:y-val is deprecated.  Use myrobot-msg:y instead.")
  (y m))

(cl:ensure-generic-function 'th-val :lambda-list '(m))
(cl:defmethod th-val ((m <dpos>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader myrobot-msg:th-val is deprecated.  Use myrobot-msg:th instead.")
  (th m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <dpos>) ostream)
  "Serializes a message object of type '<dpos>"
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
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <dpos>) istream)
  "Deserializes a message object of type '<dpos>"
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
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<dpos>)))
  "Returns string type for a message object of type '<dpos>"
  "myrobot/dpos")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'dpos)))
  "Returns string type for a message object of type 'dpos"
  "myrobot/dpos")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<dpos>)))
  "Returns md5sum for a message object of type '<dpos>"
  "000e435776f4fd6ba555d25d7a61ed8f")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'dpos)))
  "Returns md5sum for a message object of type 'dpos"
  "000e435776f4fd6ba555d25d7a61ed8f")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<dpos>)))
  "Returns full string definition for message of type '<dpos>"
  (cl:format cl:nil "float64 x~%float64 y~%float64 th~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'dpos)))
  "Returns full string definition for message of type 'dpos"
  (cl:format cl:nil "float64 x~%float64 y~%float64 th~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <dpos>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <dpos>))
  "Converts a ROS message object to a list"
  (cl:list 'dpos
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':th (th msg))
))
