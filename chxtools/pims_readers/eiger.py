"""
This reader opens images taken using an Eiger detector at NSLS-II.
It expects a "master file" and a "data file" in the same directory.

It requires h5py and the hdf5-lz4 library from Dectris. The latter
has been packaged for conda and is available on the NSLS-II internal
conda channels and externally from:

conda install -c danielballan hdf5-lz4
"""
# for backwards compatibility reasons:
from eiger_io.pims_reader import EigerImages
