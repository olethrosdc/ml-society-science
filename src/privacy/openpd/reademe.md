# Tutorial on differential private tools

In this tutorial we will present some usefully python library for differential privacy.

Differential privacy library on python.

- opendp
  - website: https://opendp.org/
  - docs: https://docs.opendp.org/en/stable/index.html
  - python api docs: https://docs.opendp.org/en/stable/api/python/index.html
  - notebook tutorials:
      1. opendp examples - https://github.com/opendp/opendp/tree/main/docs/source/examples
      2. opendp-smartnoise samples - https://github.com/opendp/smartnoise-samples

- diffprivlib
  - website: https://diffprivlib.readthedocs.io/en/latest/
  - github: https://github.com/IBM/differential-privacy-library
  - notebook tutorials: https://github.com/IBM/differential-privacy-library/tree/main/notebooks


### 1. install libraries

https://docs.opendp.org/en/stable/user/getting-started.html

- install libraries on local machine


    # create vitrual env in note
    python3 -m venv opendp_env
    
    # activate the enviroment
    source path_to_lib/bin/activate opendp_env
    
    # install basic libraries
    pip install pandas numpy seaborn matplotlib sklearn 

    # install opendp
    pip install opendp

    # install smartnoise
    pip install opendp-smartnoise

    # install diffprivlib
    pip install diffprivlib

    # install jupyter
    pip install jupyter

    # create jupyter kernel 
    python3 -m ipykernel install --user --name opendp_env --display-name "opendp_env"

to install libraries on [noto epfl](https://noto.epfl.ch/hub/login?next=%2Fhub%2F).

    # create vitrual env in note
    my_venvs_create opendp_env
    
    # activate the enviroment
    my_venvs_activate opendp_env
    
    # install basic libraries
    pip install pandas numpy seaborn matplotlib sklearn 

    # install opendp
    pip install opendp

    # install smartnoise
    pip install opendp-smartnoise

    # install diffprivlib
    pip install diffprivlib

    # create jupyter kernel 
    my_kernels_create opendpd_env "opendp_env"