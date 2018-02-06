# A2C_NAS
Supplementary to HELICON2018

In order to run the experiments, the A2C.py script must be called, with two options: the first is mandatory and concerns the dataset on which the agent will be trained (mnist/cifar10). The second option concerns the full or partial training of the generated architectures. By enabling the flag -t, the architectures are fully trained, otherwise they are partially trained.

The main libraries required to run the experiments are mpi4py, tensorflow, keras.
It is possible to run the project with only 1 process (i.e. mpiexec -n 1 python A2C.py "cifar10").
