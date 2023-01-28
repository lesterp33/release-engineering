#!python

import jenkins

server = jenkins.Jenkins('https://jenkins', username='yourname', password='pwortoken')
queue_info = server.get_queue_info()
#print(queue_info)
print (len(queue_info))

cat jenkins-plugins.groovy
def plugins = jenkins.model.Jenkins.instance.getPluginManager().getPlugins()
plugins.each {println "${it.getShortName()}: ${it.getVersion()}"}