from clustertools_example_manager import *

if __name__ == '__main__':
    cluster_worker_script(work_class,
                          max_gpu=1, max_cpu=3,
                          named_pipe=True,
                          )
