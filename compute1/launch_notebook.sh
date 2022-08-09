export LSF_DOCKER_VOLUMES="/storage1/fs1/dinglab:/storage1/fs1/dinglab /scratch1/fs1/dinglab:/scratch1/fs1/dinglab /home/estorrs:/home/estorrs"
export PATH="/miniconda/envs/ancestry/bin:$PATH"

LSF_DOCKER_PORTS='8282:8888' bsub -R 'select[mem>10GB,port8282=1] rusage[mem=10GB] span[hosts=1]' -M 11GB -q general-interactive -G compute-dinglab -Is -a 'docker(estorrs/ancestry-pipeline:0.0.1)' 'jupyter notebook --port 8888 --no-browser --ip=0.0.0.0'
