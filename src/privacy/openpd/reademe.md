# Tutorial on opendp

In this tutorial we will cover some basic examples using openpd python library.

openpd is differential privacy library on python.

- website: https://opendp.org/
- docs: https://docs.opendp.org/en/stable/index.html
- original examples:
    1. opendp examples - https://github.com/opendp/opendp/tree/main/docs/source/examples
    2. smartnoise samples - https://github.com/opendp/smartnoise-samples

### 1. install opendp
https://docs.opendp.org/en/stable/user/getting-started.html

to install openpd run the following commands on noto epfl.

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

    # create jupyter kernel 
    my_kernels_create opendpd_env "opendp_env"

### 2. Tutorial
1. calculate mean using laplacian mechanism
   * "1. opendp - average - laplacian noise.ipynb"
2. calculate count -  histrogram.
    *
3. openpd - ml