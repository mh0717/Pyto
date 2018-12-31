# This file is generated by /Users/adrianlabbe/Desktop/numpy-1.11.1/setup.py
# It contains system_info results at the time of building this package.
__all__ = ["get_info","show"]

blas_mkl_info={}
openblas_info={}
atlas_3_10_blas_threads_info={}
atlas_3_10_blas_info={}
atlas_blas_threads_info={'language': 'c', 'define_macros': [('HAVE_CBLAS', None), ('NO_ATLAS_INFO', -1)], 'libraries': ['ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/local/lib']}
blas_opt_info={'language': 'c', 'define_macros': [('HAVE_CBLAS', None), ('NO_ATLAS_INFO', -1)], 'libraries': ['ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/local/lib']}
openblas_lapack_info={}
mkl_info={}
lapack_mkl_info={}
atlas_3_10_threads_info={}
atlas_3_10_info={}
atlas_threads_info={'language': 'c', 'libraries': ['lapack', 'ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/local/lib'], 'define_macros': [('NO_ATLAS_INFO', -1)]}
lapack_opt_info={'language': 'c', 'libraries': ['lapack', 'ptf77blas', 'ptcblas', 'atlas', 'ptf77blas', 'ptcblas'], 'library_dirs': ['/usr/local/lib'], 'define_macros': [('NO_ATLAS_INFO', -1)]}

def get_info(name):
    g = globals()
    return g.get(name, g.get(name + "_info", {}))

def show():
    for name,info_dict in globals().items():
        if name[0] == "_" or type(info_dict) is not type({}): continue
        print(name + ":")
        if not info_dict:
            print("  NOT AVAILABLE")
        for k,v in info_dict.items():
            v = str(v)
            if k == "sources" and len(v) > 200:
                v = v[:60] + " ...\n... " + v[-60:]
            print("    %s = %s" % (k,v))
    