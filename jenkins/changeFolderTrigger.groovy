#!groovy

for (f in Jenkins.instance.getAllItems(jenkins.branch.MultiBranchProject.class)) {
  if (f.parent instanceof jenkins.branch.OrganizationFolder) {
 f.addTrigger(new com.cloudbees.hudson.plugins.folder.computed.PeriodicFolderTrigger("1m"));
  }
}
