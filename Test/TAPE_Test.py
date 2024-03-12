# basic example
from TAPE import Deconvolution

Sigm, Pred = Deconvolution('Kidney_ref.txt', 'Kidney_test.txt',sep='\t',
                           datatype='counts', genelenfile='./GeneLength.txt',
                           mode='overall', adaptive=True,
                           save_model_name = None)