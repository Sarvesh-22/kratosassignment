Week 3- assignment
Question 1-
  pub_hello.py- creates a publisher node to publish hello world! at the rate of 1 Hz
  sub_hello.py- subscribes from pub_hello.py using the new method and displays the same message as the publisher at a given rate
 
Question 2-
  signal1.py- publishes red or green depending upon the time interval of 10 seconds using s1 topic
  signal2.py- subscribes from signal1 with the topic s1 and publishes the opposite
              (of red or green) of signal1 using s2

Question 3-
  rover_cust.py- publishes a sequence of messages based on the custom messages in rover.msg to display the details of the rover
  changes were also made to CMakeLists.txt and Package.xml to allow message generation during runtime
 
 Question 4-
  timesec.py- publishes at a rate of 1 Hz after incrementing at each second till it reaches 59 and then reverts back to zero
  timemin.py- subscribes from /second and increments minute after one cycle of timesec
  timehrs.py- subscribes from /second and /minnute to increment /hour after one cycle of timemin
  timeclocks.py- subscribes from /second, /minnute and /hour to display string of time which increments /clock at each second
 
 In addition, each file was declared executable after creating it. 
