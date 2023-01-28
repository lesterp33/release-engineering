#!groovy

Jenkins.instance.getItemByFullName("Folder/Job/branchjob")
        .getBuildByNumber(JobNumber)
        .finish(hudson.model.Result.ABORTED, new java.io.IOException("Aborting build"));