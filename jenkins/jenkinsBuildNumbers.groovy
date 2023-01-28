#!groovy

//get build number
Jenkins.instance.getItemByFullName("YourPipelineName/YourBranchName").getNextBuildNumber()

//set build number
Jenkins.instance.getItemByFullName("YourPipelineName/YourBranchName").updateNextBuildNumber(45)

import hudson.model.*

def q = Jenkins.instance.queue

q.items.each { q.cancel(it.task) }
