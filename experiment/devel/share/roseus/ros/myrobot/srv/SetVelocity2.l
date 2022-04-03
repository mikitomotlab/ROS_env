;; Auto-generated. Do not edit!


(when (boundp 'myrobot::SetVelocity2)
  (if (not (find-package "MYROBOT"))
    (make-package "MYROBOT"))
  (shadow 'SetVelocity2 (find-package "MYROBOT")))
(unless (find-package "MYROBOT::SETVELOCITY2")
  (make-package "MYROBOT::SETVELOCITY2"))
(unless (find-package "MYROBOT::SETVELOCITY2REQUEST")
  (make-package "MYROBOT::SETVELOCITY2REQUEST"))
(unless (find-package "MYROBOT::SETVELOCITY2RESPONSE")
  (make-package "MYROBOT::SETVELOCITY2RESPONSE"))

(in-package "ROS")





(defclass myrobot::SetVelocity2Request
  :super ros::object
  :slots (_linear_velocity _angular_velocity ))

(defmethod myrobot::SetVelocity2Request
  (:init
   (&key
    ((:linear_velocity __linear_velocity) 0.0)
    ((:angular_velocity __angular_velocity) 0.0)
    )
   (send-super :init)
   (setq _linear_velocity (float __linear_velocity))
   (setq _angular_velocity (float __angular_velocity))
   self)
  (:linear_velocity
   (&optional __linear_velocity)
   (if __linear_velocity (setq _linear_velocity __linear_velocity)) _linear_velocity)
  (:angular_velocity
   (&optional __angular_velocity)
   (if __angular_velocity (setq _angular_velocity __angular_velocity)) _angular_velocity)
  (:serialization-length
   ()
   (+
    ;; float64 _linear_velocity
    8
    ;; float64 _angular_velocity
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _linear_velocity
       (sys::poke _linear_velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _angular_velocity
       (sys::poke _angular_velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _linear_velocity
     (setq _linear_velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _angular_velocity
     (setq _angular_velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass myrobot::SetVelocity2Response
  :super ros::object
  :slots (_linear_velocity _angular_velocity ))

(defmethod myrobot::SetVelocity2Response
  (:init
   (&key
    ((:linear_velocity __linear_velocity) 0.0)
    ((:angular_velocity __angular_velocity) 0.0)
    )
   (send-super :init)
   (setq _linear_velocity (float __linear_velocity))
   (setq _angular_velocity (float __angular_velocity))
   self)
  (:linear_velocity
   (&optional __linear_velocity)
   (if __linear_velocity (setq _linear_velocity __linear_velocity)) _linear_velocity)
  (:angular_velocity
   (&optional __angular_velocity)
   (if __angular_velocity (setq _angular_velocity __angular_velocity)) _angular_velocity)
  (:serialization-length
   ()
   (+
    ;; float64 _linear_velocity
    8
    ;; float64 _angular_velocity
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _linear_velocity
       (sys::poke _linear_velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _angular_velocity
       (sys::poke _angular_velocity (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _linear_velocity
     (setq _linear_velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _angular_velocity
     (setq _angular_velocity (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass myrobot::SetVelocity2
  :super ros::object
  :slots ())

(setf (get myrobot::SetVelocity2 :md5sum-) "7f8ecd2d213b118d540a9b1a31647365")
(setf (get myrobot::SetVelocity2 :datatype-) "myrobot/SetVelocity2")
(setf (get myrobot::SetVelocity2 :request) myrobot::SetVelocity2Request)
(setf (get myrobot::SetVelocity2 :response) myrobot::SetVelocity2Response)

(defmethod myrobot::SetVelocity2Request
  (:response () (instance myrobot::SetVelocity2Response :init)))

(setf (get myrobot::SetVelocity2Request :md5sum-) "7f8ecd2d213b118d540a9b1a31647365")
(setf (get myrobot::SetVelocity2Request :datatype-) "myrobot/SetVelocity2Request")
(setf (get myrobot::SetVelocity2Request :definition-)
      "float64 linear_velocity
float64 angular_velocity
---
float64 linear_velocity
float64 angular_velocity

")

(setf (get myrobot::SetVelocity2Response :md5sum-) "7f8ecd2d213b118d540a9b1a31647365")
(setf (get myrobot::SetVelocity2Response :datatype-) "myrobot/SetVelocity2Response")
(setf (get myrobot::SetVelocity2Response :definition-)
      "float64 linear_velocity
float64 angular_velocity
---
float64 linear_velocity
float64 angular_velocity

")



(provide :myrobot/SetVelocity2 "7f8ecd2d213b118d540a9b1a31647365")


