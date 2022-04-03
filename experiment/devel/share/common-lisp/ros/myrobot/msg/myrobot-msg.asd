
(cl:in-package :asdf)

(defsystem "myrobot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "dpos" :depends-on ("_package_dpos"))
    (:file "_package_dpos" :depends-on ("_package"))
  ))