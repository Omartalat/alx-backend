#!/usr/bin/env node

const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }
  for (const jobObj of jobs) {
    const job = queue.create("push_notification_code_2", jobObj);
    job
      .on("enqueue", () => {
        console.log("Notification job created: " + job.id);
      })
      .on("complete", () => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on("failed", (errorMessage) => {
        console.log(
          "Notification job JOB_ID failed: " + errorMessage.toString()
        );
      })
      .on("progress", (progress) => {
        console.log(`Notification job ${job.id} $${progress}% complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
