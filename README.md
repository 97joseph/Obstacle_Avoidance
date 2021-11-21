# Obstacle_Avoidance

Obstacle Avoidance with Bug 2 Algorithm

## Introduction to Mobile Robotics

Obstacle Avoidance with Bug 2 Algorithm Introduction:

In this lab, you will write a ROS package for obstacle avoidance using Bug2 algorithm. The theory of Bug2 has been discussed in the class. You will implement a Bug2 algorithm to enable your robot to reach a goal position from a start position in a given map while avoiding an unplanned obstacle.  This lab has two components and will be completed in two weeks. Lab Work: Navigating  to  a  pre-defined  goal  while  avoiding  an  unplanned  obstacle  using  Bug2  algorithm requires implementation of two behaviors in the robot: “goal-seek” (where the robot will follow a planned trajectory to reach the goal) and “wall-follow” (where the robot will follow the wall of  the  obstacle  until  it  reaches  the  m-line).  The robot needs  to  continuously  localize  itself while executing these two behaviors. You will use AMCLfor localizing the robot(the same way you used AMCL inLab 4). 

We have provided a skeleton sub-class where you can implement the two listed behaviors. 

The sub-class builds upon your earlier work and therefore requires you to have a copy of your earlier code (from Lab 3 or 4) in the same scripts directory where you store this lab’s skeleton code.This lab marks a substantial increase in challenge and freedomover earlier labs. 

To that end you will  find  the  skeleton  code  is  far  more  sparse  than earlier codes.We strongly encourageyou  to consider the requirements of the given task and make any modifications to the code that you deem necessary to generate the desired result. (Note: you are free to use code/information from outside of the class to solve the assignmentbut remember to cite your sources properlyinyour reportto avoid penalty for plagiarism)[Additional Resourceson Bug 2 Implementation:

The Algorithm 2 in the reference bookPrinciple of Robot Motionis aBug 2algorithm that you may find useful to organize your thoughts. Section 2.3 of the same book discusses some implementation tricks for the wall  follow behaviorthat you may find useful]Goal-Seek Behavior:We will evaluate this behavior of your robot as it traversesa rectangular path from any starting point and stops after returningto that point. Throughout this process you will use a map that you built in Lab 4. This part of the lab is due on November 5. 1.Subscribe to the ‘amcl_pose’ rostopic.

2.Complete the goToGoaland driveStraightAMCLfunctions. The functions should use the controller you designed in Lab 3for smoothrobot motion.3.Modify executeTrajectory sothat the robot navigates along arectangular pathof your choiceand returns to where it started. Note: We will be checking to make sure that AMCL is used to identify the locationsalong the path4.Ensure that you publish visualization markersfor each goalto RViZ and can see them in the application.

The starter code provides an example ofhow to create visualization markers. You willhave to explicitlyinclude those markers in the RViZ following these steps: a.Press the add button located in the bottom left, b.select Marker,c.then select the appropriatetopic name.Wall-Follow Behavior:We will evaluate this behavior of your robot as it followsthe wall of a newly encounteredobstaclewhiletravelling ona given map. 

This part of the lab is due on October 29. 1.Subscribe to the ‘scan’and ‘amcl_pose’rostopics(discussedin Lab 4).2.Investigate the LaserScan message to understand its component parts. Note: It may also help to look at the laserscan_to_imagefunction we provided you in Lab4for additional context.3.In the laserscanCallback modify the variable “self.wall_following” variable to Trueif an obstacle is detectedso that the robot begins executing the WallFollowProtocol function (it should print out a message to let you know the function has been called).4.Complete the getTangentLine and WallFollowProtocol functions.There are various ways you can identify the tangent line to a set of points (corresponding to the laser scan of the obstacle). A simple slope-basedmethod was discussed in the theory class. 

The appendix 1of this manual discusses a more robust regression-basedmethod forfinding tangent linesand the starter code also provides a pseudo code (Note: linear regression was not discussed in the theory class; use this methodif you are comfortablewith regression). You can, however,use any method other than these two for calculating tangent lines. Complete Bug 2 Demonstration:Using the goal-seek andwall-followbehaviors, you will demonstrate how yourrobot avoids a newly encountered obstacle and reacha pre-defined goal location in a given map. This part of the lab is due on November 5.Functions:All units should be in meters, degrees, and meters/second.goToGoal(speed, goal_pos)
