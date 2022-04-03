
(cl:in-package :asdf)

(defsystem "myrobot-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetVelocity" :depends-on ("_package_SetVelocity"))
    (:file "_package_SetVelocity" :depends-on ("_package"))
    (:file "SetVelocity2" :depends-on ("_package_SetVelocity2"))
    (:file "_package_SetVelocity2" :depends-on ("_package"))
    (:file "d_position" :depends-on ("_package_d_position"))
    (:file "_package_d_position" :depends-on ("_package"))
  ))