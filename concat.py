import sys
import biom
import h5py

output = sys.argv[1]
tables = [biom.load_table(f) for f in sys.argv[2:]]
merged = tables[0].concat(tables[1:])

with h5py.File(output,'w') as fp:
    merged.to_hdf5(fp, 'custom')
