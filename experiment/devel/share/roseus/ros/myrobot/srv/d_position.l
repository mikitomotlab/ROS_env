;; Auto-generated. Do not edit!


(when (boundp 'myrobot::d_position)
  (if (not (find-package "MYROBOT"))
    (make-package "MYROBOT"))
  (shadow 'd_position (find-package "MYROBOT")))
(unless (find-package "MYROBOT::D_POSITION")
  (make-package "MYROBOT::D_POSITION"))
(unless (find-package "MYROBOT::D_POSITIONREQUEST")
  (make-package "MYROBOT::D_POSITIONREQUEST"))
(unless (find-package "MYROBOT::D_POSITIONRESPONSE")
  (make-package "MYROBOT::D_POSITIONRESPONSE"))

(in-package "ROS")





(defclass myrobot::d_positionRequest
  :super ros::object
  :slots (_dx _dy _dth ))

(defmethod myrobot::d_positionRequest
  (:init
   (&key
    ((:dx __dx) 0.0)
    ((:dy __dy) 0.0)
    ((:dth __dth) 0.0)
    )
   (send-super :init)
   (setq _dx (float __dx))
   (setq _dy (float __dy))
   (setq _dth (float __dth))
   self)
  (:dx
   (&optional __dx)
   (if __dx (setq _dx __dx)) _dx)
  (:dy
   (&optional __dy)
   (if __dy (setq _dy __dy)) _dy)
  (:dth
   (&optional __dth)
   (if __dth (setq _dth __dth)) _dth)
  (:serialization-length
   ()
   (+
    ;; float64 _dx
    8
    ;; float64 _dy
    8
    ;; float64 _dth
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _dx
       (sys::poke _dx (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _dy
       (sys::poke _dy (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _dth
       (sys::poke _dth (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _dx
     (setq _dx (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _dy
     (setq _dy (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _dth
     (setq _dth (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass myrobot::d_positionResponse
  :super ros::object
  :slots (_x _y _th ))

(defmethod myrobot::d_positionResponse
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:th __th) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _th (float __th))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:th
   (&optional __th)
   (if __th (setq _th __th)) _th)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _th
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _th
       (sys::poke _th (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _th
     (setq _th (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass myrobot::d_position
  :super ros::object
  :slots ())

(setf (get myrobot::d_position :md5sum-) "f82f197a7f2c41cf8d240b3b8b2f9316")
(setf (get myrobot::d_position :datatype-) "myrobot/d_position")
(setf (get myrobot::d_position :request) myrobot::d_positionRequest)
(setf (get myrobot::d_position :response) myrobot::d_positionResponse)

(defmethod myrobot::d_positionRequest
  (:response () (instance myrobot::d_positionResponse :init)))

(setf (get myrobot::d_positionRequest :md5sum-) "f82f197a7f2c41cf8d240b3b8b2f9316")
(setf (get myrobot::d_positionRequest :datatype-) "myrobot/d_positionRequest")
(setf (get myrobot::d_positionRequest :definition-)
      "float64 dx
float64 dy
float64 dth
---
float64 x
float64 y
float64 th

")

(setf (get myrobot::d_positionResponse :md5sum-) "f82f197a7f2c41cf8d240b3b8b2f9316")
(setf (get myrobot::d_positionResponse :datatype-) "myrobot/d_positionResponse")
(setf (get myrobot::d_positionResponse :definition-)
      "float64 dx
float64 dy
float64 dth
---
float64 x
float64 y
float64 th

")



(provide :myrobot/d_position "f82f197a7f2c41cf8d240b3b8b2f9316")


