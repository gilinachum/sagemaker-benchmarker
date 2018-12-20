import temp_lib
benchmarker.fit_optimized(estimator, 
                          job_config = 
                          [ 
    {'instance_type' : 'ml.c4.2large'}, 
    {'instance_type' : 'ml.c5.4xlarge'}
])
