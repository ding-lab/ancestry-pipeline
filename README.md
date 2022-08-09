# ancestry-pipeline
Ding lab ancestry pipeline

## Usage 

#### Running on compute1

The ancestry pipeline is current set up to run on compute1 through scripts generated via a jupyter notebook.

###### Launching the jupyter notebook

More details on how to run jupyter notebooks on compute1 are in this [wiki page](https://dlwiki.wusm.wustl.edu/wiki/Jupyter_Notebooks#Compute1). But for a quick start follow the below steps.

On compute1, once you have cloned the repo you'll need to modify `compute1/launch_notebook.sh`.

- modify the `export LSF_DOCKER_VOLUMES` string to map whatever directories you need to map. This will require you changing `/home/estorrs` to `/home/<USERNAME>` where your compute1 username is <USERNAME>. Also, if you are not a part of the dinglab you will need to modify the paths to point to your labs storage1 allocation. Additionally, change the `LSF_DOCKER_PORTS` and `select` string to map a port besides 8181 (I like using 8181 and dont want to have to change it :)). To use a different port replace 8181 with a port between 8000-12000. For example, `LSF_DOCKER_PORTS='12345:8888'` and `select[mem>100GB,port12345=1]`.

Once you have made those modifications, launch the jupyter notebook by running the script from the root of the repository.

```bash
bash compute1/launch_notebook.sh
```

To connect to the notebook from your browser you need to run a few steps. Notice the link that is output by the launch notebook command, it should look something like this `http://compute1-exec-199.ris.wustl.edu:8888/?token=c18c61acb19c4d0bb6c5de67fdb76c1b089bfde95f2f99e4`. Take note of what # host you are on (in this case I am on compute1-exec-199). In a seperate terminal on YOUR LOCAL MACHINE, run the following to map your local machine to compute1, where <PORT> is the port you replaced in `launch_notebook.sh`, <HOST> is the host the notebook is running on (for example compute1-exec-199), and <USERNAME> is your compute1 username.

```bash
ssh -L <PORT>:<HOST>:<PORT> -N <USERNAME>@compute1-client-1.ris.wustl.edu
```

Now, paste into your browser the following link the launch notebook command output, but replacing everthing before `/?token` with `localhost:<PORT>`, where <PORT> is the port you replaced in `launch_notebook.sh`. For example, my link would look something like `localhost:8181/?token=c18c61acb19c4d0bb6c5de67fdb76c1b089bfde95f2f99e4`.

You should now be inside a running jupyter notebook.

###### Running the pipeline

The tutorial/example notebook you can use to generate the bsub commands that run the ancestry pipeline is [`notebooks/run_ancestry.ipynb`](https://github.com/ding-lab/ancestry-pipeline/blob/main/notebooks/run_ancestry.ipynb)

I would recommend putting your run directory inside `/scratch1` as tools tend to run faster in scratch1 than in storage1.

NOTE: you will likely need to make some small changes to the example notebook to specify input/output files, etc.

## Output format

There are two main output folders: `super_population` and `sub_population`. `super_population` contains predictions for the five major ancestry categories used by the 1k genomes project. `sub_population` includes predictions for the many sub-categories used by 1k genomes.

The major ancestry classfications are as follows:
+ EUS - european
+ AFR - african
+ AMR - american
+ SAS - south asian
+ EAS - east asian

The files produced by the pipeline are:
+ predictions.tsv - ancestry predictions and probabilities for each sample
+ samples.pcs - PCs for each sample
+ stats.yaml - classifier performance statistics
+ thousand_genomes.test.pcs - PCs for thousand genome test set samples
+ thousand_genomes.training.pcs - PCs for thousand genome test set samples
+ various plots

## Methods description

*exact numbers may vary depending on composition of prediction cohort, the below paragraph is an example methods paragraph

We used a reference panel of genotypes and clustering based on principal components to identify likely ancestry. We selected 107,765 coding SNPs with a minor allele frequency > 0.02 from the 1000 Genomes Project (PMID 20981092, http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/). From this set of loci, we measured the depth and allele counts of each sample in our cohort using the tool bam-readcount (https://github.com/genome/bam-readcount, version 0.8.0). Genotypes were then called for each sample based on the following criteria: 0/0 if reference count ≥ 8 and alternate count < 4; 0/1 if reference count ≥ 4 and alternate count ≥ 4; 1/1 if reference count < 4 and alternate count ≥ 8; and ./. (missing) otherwise. After filtering markers with missingness > 5%, 58,991 markers were left for analysis. We performed principal component analysis (PCA) on the 1000 Genomes samples to identify the top 20 principal components. We then projected our cohort onto the 20-dimensional space representing the 1000 Genomes data. We then trained a random forest classifier with the 1000 Genomes dataset using these 20 principal components. The 1000 Genomes dataset was split 80/20 for training and validation respectively. On the validation dataset our classifier achieved 99.6% accuracy. We then used the fitted classifier to predict the likely ancestry of our cohort.

