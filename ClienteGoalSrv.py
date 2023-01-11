#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Pose2D

from tb3_cmd.srv import Goal


def GoalCliente(param): 
    rospy.loginfo("En espera de respuesta del servicio Goal...")
    rospy.wait_for_service('/goalService')
    try: 
        goalServ = rospy.ServiceProxy('/goalService', Goal)
        srv_response = goalServ(param)
        print("Verificar que el servicio se haya efectuado")
        return srv_response

    except rospy.ServiceException as e: 
        print("Falló el servicio: %s"%e)

if __name__ == "__main__":
    param = Pose2D()
    param.x = 2
    param.y = 3
    param.theta = 0
    rospy.loginfo("Prueba")
    srv = GoalCliente(param)
    print ("%s"%(srv))
    rospy.logerr("Llamado de servicio concluido")