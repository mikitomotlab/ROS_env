;; Auto-generated. Do not edit!


(when (boundp 'myrobot::dpos)
  (if (not (find-package "MYROBOT"))
    (make-package "MYROBOT"))
  (shadow 'dpos (find-package "MYROBOT")))
(unless (find-package "MYROBOT::DPOS")
  (make-package "MYROBOT::DPOS"))

(in-package "ROS")
;;//! \htmlinclude dpos.msg.html


(defclass myrobot::dpos
  :super ros::object
  :slots (_x _y _th ))

(defmethod myrobot::dpos
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

(setf (get myrobot::dpos :md5sum-) "000e435776f4fd6ba555d25d7a61ed8f")
(setf (get myrobot::dpos :datatype-) "myrobot/dpos")
(setf (get myrobot::dpos :definition-)
      "float64 x
float64 y
float64 th


")



(provide :myrobot/dpos "000e435776f4fd6ba555d25d7a61ed8f")


