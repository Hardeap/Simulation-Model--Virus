from pyper import *
import matplotlib.pyplot as plt
deaths_num = []
Infectiousness_rate = []
r = R(RCMD="C:\\Program Files\\R\\R-3.4.2\\bin\\x64\\R")
r('Sys.setenv(JAVA_HOME="C:\\Program Files\\Java\\jre1.8.0_144")')
r('library(RNetLogo)')
r('nl.path <- "C:/Program Files/NetLogo 6.0.2/app"')
r('nl.jarname <- "netlogo-6.0.2.jar"')
r('NLStart(nl.path, nl.jarname=nl.jarname)')
r('model.path <- "/models/Sample Models/Biology/Virus test.nlogo"')
r('NLLoadModel(paste(nl.path,model.path,sep=""))')
for i in range(0, 13):
 print( '----------------', i*7, '---------------------')
 Infectiousness_rate.append(i*7)
 r('NLCommand("set infectiousness ' + str (i*7) + '")')
 r('NLCommand("setup")')
 r('NLDoCommand(1040, "go")')
 r('t_deaths <- NLReport("dead")')
 print(r.t_deaths)
 deaths_num.append(r.t_deaths)
plt.figure(figsize=(8,4))
plt.xlabel("infectiousness")
plt.ylabel("Deaths")
plt.plot(Infectiousness_rate, deaths_num)
plt.show()
r('NLQuit()')
