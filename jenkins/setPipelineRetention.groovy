#!groovy

import org.jenkinsci.plugins.workflow.job.WorkflowJob
import hudson.tasks.LogRotator

def allItems = Jenkins.instance.getAllItems(WorkflowJob)

allItems.each { job ->

  // defaults to use
  newArtifactDaysToKeep = 7
  newArtifactNumToKeep = 10
  newDaysToKeep = 30
  newNumToKeep = 100

  newDiscarder = false

  buildDiscarder = job.getBuildDiscarder()

  // if the buildDiscarder is already configured, then check if it is partially configured
  // and honour whatever settings are in the jenkinsfile
  if (buildDiscarder) {
    if (buildDiscarder instanceof LogRotator) {
      artifactDaysToKeep = buildDiscarder.getArtifactDaysToKeep()
      artifactNumToKeep = buildDiscarder.getArtifactNumToKeep()
      daysToKeep = buildDiscarder.getDaysToKeep()
      numToKeep = buildDiscarder.getNumToKeep()

      println "Existing config is: artifactDaysToKeep (${artifactDaysToKeep}) artifactNumToKeep (${artifactNumToKeep}) daysToKeep (${daysToKeep}) numToKeep (${numToKeep})"

      if ((artifactDaysToKeep < 1) || (artifactNumToKeep < 1) || (daysToKeep < 1) || (numToKeep < 1)) {
        newDiscarder = true
      }

      if (artifactDaysToKeep > 0) {
        newArtifactDaysToKeep = artifactDaysToKeep
      }

      if (artifactNumToKeep > 0) {
        newArtifactNumToKeep = artifactNumToKeep
      }

      if (daysToKeep > 0) {
        newDaysToKeep = daysToKeep
      }

      if (numToKeep > 0) {
        newNumToKeep = numToKeep
      }

    } else {
      // enforce LogRotator discarder just in case another appears
      newDiscarder = true
    }
  } else {
    // if no discarder is configured yet then we'll add our agreed defaults
    newDiscarder = true
  }

  if (newDiscarder == true) {
    // we'll persist this as that allows the settings to survive restart
    // note that a jenkinsfile will only touch this is properties() is set in it
    println "New config is: artifactDaysToKeep (${newArtifactDaysToKeep}) artifactNumToKeep (${newArtifactNumToKeep}) daysToKeep (${newDaysToKeep}) numToKeep (${newNumToKeep})"

    newBuildDiscarder = new LogRotator(newDaysToKeep, newNumToKeep, newArtifactDaysToKeep, newArtifactNumToKeep)

    job.setBuildDiscarder(newBuildDiscarder)
    job.save()
  }

  // At this point either we've set a configure or verified the Jenkinsfile for the workflow has already got values assigned
  println "Running cleanup of " + job.getFullName()
  job.logRotate()

}

return "completed"

