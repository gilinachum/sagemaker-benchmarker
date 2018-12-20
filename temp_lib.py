def fit_optimized(estimator, job_config):
    #print(estimator.latest_training_job.name)
    print(str(job_config))
    jobs = job_config
    save_instance_type = estimator.train_instance_type
    print(f'About to launch {len(jobs)} jobs: {jobs}')
    for job in job_config:
        estimator.train_instance_type = job['instance_type']
        # TODO add detailed monitoring.
        estimator.fit(inputs, wait=False)
        job['training_job'] = estimator.latest_training_job
        print(f'Started {job["training_job"].job_name}')
        print(f'{job}')
    print('Finished launching {len(jobs)} jobs')
    estimator.train_instance_type = save_instance_type

print("hi")
def complete_jobs():
    import time
    sm_client = sagemaker_session.sagemaker_client
    is_completed = False
    while not is_completed:
        is_completed = True
        for job_count, job in enumerate(jobs):
            training_job_name = job['training_job'].job_name
            job_details = sm_client.describe_training_job(TrainingJobName=training_job_name)
            status = job_details["TrainingJobStatus"]
            secondary_status = job_details["SecondaryStatus"]
            #print(job_details)
            print(f'config[{job_count}]={job["instance_type"]}, job name={training_job_name},'+ 
                  f' status=[{status}, {secondary_status}]')
            job_already_completed = True if status == 'Completed' or status == 'Failed' or status == 'Stopped' else False
            is_completed = False if not job_already_completed else is_completed
        time.sleep(3)
