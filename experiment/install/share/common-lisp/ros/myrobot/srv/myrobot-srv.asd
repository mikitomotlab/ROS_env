
(cl:in-package :asdf)

(defsystem "myrobot-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SetVelocity" :depends-on ("_package_SetVelocity"))
    (:file "_package_SetVelocity" :depends-on ("_package"))
  ))