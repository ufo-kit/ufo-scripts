# This file is used to share params as a global variable
import yaml
import os
from collections import OrderedDict
from tofu.util import restrict_value

params = {}

def save_parameters(params, file_path):
    file_out = open(file_path, 'w')
    yaml.dump(params, file_out)
    print("Parameters file saved at: " + str(file_path))


EZVARS = OrderedDict()
EZVARS_aux = OrderedDict()

EZVARS_aux['find360olap'] = {
    'input-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),""),
        'type': str,
        'help': "TODO"},
    'output-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),"ezufo_360_olap_search"),
        'type': str,
        'help': "TODO"},
    'tmp-dir' : {
        'ezdefault': os.path.join(os.path.expanduser('~'),"ezufo_360_tmp"),
        'type': str,
        'help': "TODO"},
    'doRR': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'doPR': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'step': {
        'ezdefault': 1,
        'type': restrict_value((0, None), dtype=int),
        'help': "Increment in axis of rotation"},
    'start': {
        'ezdefault': 150,
        'type': restrict_value((0, None), dtype=int),
        'help': "Starting overlap"},
    'stop': {
        'ezdefault': 200,
        'type': restrict_value((0, None), dtype=int),
        'help': "Maximum overlap"},
    'row': {
        'ezdefault': 500,
        'type': restrict_value((0, None), dtype=int),
        'help': "Maximum overlap"},
    'patch-size': {
        'ezdefault': 2048,
        'type': restrict_value((0, None), dtype=int),
        'help': "Size of the slice fragment which will be reconstructed"},
}

EZVARS_aux['stitch360'] = {
    'input-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),""),
        'type': str,
        'help': "TODO"},
    'output-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),"ezufo_360_stitched"),
        'type': str,
        'help': "TODO"},
    'crop': {
        'ezdefault': True,
        'type': bool,
        'help': "TODO"},
    'olap_switch': {
        'ezdefault': 0,
        'type': restrict_value((0, 2), dtype=int),
        'help': ""},
    'olap_min': {
        'ezdefault': 1,
        'type': restrict_value((0, None), dtype=int),
        'help': ""},
    'olap_max': {
        'ezdefault': 1,
        'type': restrict_value((0, None), dtype=int),
        'help': ""},
    'olap_list': {
        'ezdefault': '',
        'type': str,
        'help': "Comma-separated list of overlaps without spaces"},
}

EZVARS_aux['half-acq'] = {
    'workdir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),"ezufo-halfacq"),
        'type': str,
        'help': "TODO"},
    'task_type': {
        'ezdefault': 1,
        'type': restrict_value((0, 1), dtype=int),
        'help': "What task was requested by user"},
    'list_dirs': {
        'ezdefault': '/data/foo',
        'type': str,
        'help': "Comma-separated list of outer loop directories which contain"
                "subdirectories with inner loop CT scans"},
    'list_olaps': {
        'ezdefault': '50',
        'type': str,
        'help': "Comma-separated list of overlaps for every subdirectory in"
                "lexicographic order"},
}

EZVARS_aux['vert-sti'] = {
    'dovertsti': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'input-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'), ""),
        'type': str,
        'help': "TODO"},
    'output-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'), "ezufo_stitched_images"),
        'type': str,
        'help': "TODO"},
    'tmp-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'), "ezufo_stitched_tmp"),
        'type': str,
        'help': "TODO"},
    'subdir-name': {
        'ezdefault': "sli",
        'type': str,
        'help': "TODO"},
    'ort': {
        'ezdefault': True,
        'type': bool,
        'help': "TODO"},
    'step': {
        'ezdefault': 200,
        'type': restrict_value((0, None), dtype=int),
        'help': "Increment"},
    'start': {
        'ezdefault': 200,
        'type': restrict_value((0, None), dtype=int),
        'help': "Start"},
    'stop': {
        'ezdefault': 2000,
        'type': restrict_value((0, None), dtype=int),
        'help': ""},
    'reslice_all': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'flipud': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'task_type': {
        'ezdefault': 0,
        'type': restrict_value((0, 2), dtype=int),
        'help': "What task was requested by user"},
    'num_olap_rows': {
        'ezdefault': 60,
        'type': restrict_value((0, None), dtype=int),
        'help': "Increment in axis of rotation"},
    'estimate_num_olap_rows': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'ind_z00': {
        'ezdefault': 0,
        'type': restrict_value((0, None), dtype=int),
        'help': "Index of slice in 00 directory which will be used to find the overlap"},
    'ind_z01_start': {
        'ezdefault': 800,
        'type': restrict_value((0, None), dtype=int),
        'help': "Index of the beginning of the range of slices in 01 directory which will be used to find the overlap"},
    'ind_z01_stop': {
        'ezdefault': 850,
        'type': restrict_value((0, None), dtype=int),
        'help': "Stop index in z01 directory for the range of slices used to find the vertical overlap"},
    'clip_hist': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"},
    'min_int_val': {
        'ezdefault': -0.0003,
        'type': float,
        'help': "TODO"},
    'max_int_val': {
        'ezdefault': 0.0002,
        'type': float,
        'help': "TODO"},
    'conc_row_top': {
        'ezdefault': 40,
        'type': restrict_value((0, None), dtype=int),
        'help': "First row in the image"},
    'conc_row_bottom': {
        'ezdefault': 440,
        'type': restrict_value((0, None), dtype=int),
        'help': "Last row in the image"},
    'cor': {
        'ezdefault': 245,
        'type': restrict_value((0, None), dtype=int),
        'help': "Axis of rotation for half acq mode stitching"}
}


EZVARS_aux['axes-list'] = {
   # Template:
   #  '/data/TestBatch/foo2': # outer loop scan
   #      {'z02': 40, 'z03': 41},  # several inner loop scans
   # '/data/TestBatch':
   #     {'z02': 0},
   #   '/data/TestBatch/TestCT360-single-tifs':
   #      {z00: 50, z01: 49}
}

EZVARS['inout'] = {
    'input-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),""), 
        'type': str, 
        'help': "TODO"},
    'output-dir': {
        'ezdefault': os.path.join(os.path.expanduser('~'),"ezufo-rec"),
        'type': str, 
        'help': "TODO"},
    'tmp-dir' : {
        'ezdefault': os.path.join(os.path.expanduser('~'),"ezufo-tmp"),
        'type': str, 
        'help': "TODO"},
    'darks-dir': {
        'ezdefault': "darks",
        'type': str, 
        'help': "TODO"},
    'flats-dir': {
        'ezdefault': "flats",
        'type': str, 
        'help': "TODO"},
    'tomo-dir': {
        'ezdefault': "tomo",
        'type': str, 
        'help': "TODO"},
    'flats2-dir': {
        'ezdefault': "flats2",
        'type': str, 
        'help': "TODO"},
    'bigtiff-output': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'input_ROI': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'clip_hist': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'preprocess': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'preprocess-command': {
        'ezdefault': "remove-outliers size=3 threshold=500 sign=1", 
        'type': str, 
        'help': "TODO"},
    'output-ROI': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'output-x': {
        'ezdefault': 0,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Crop slices: x"},
    'output-width': {
        'ezdefault': 0,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Crop slices: width"},
    'output-y': {
        'ezdefault': 0,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Crop slices: y"},
    'output-height': {
        'ezdefault': 0,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Crop slices: height"},
    'dryrun': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'save-params': {
        'ezdefault': True, 
        'type': bool, 
        'help': "TODO"},
    'keep-tmp': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'open-viewer': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'shared-flatsdarks': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'path2-shared-darks': {
        'ezdefault': "Absolute path to darks", 
        'type': str, 
        'help': "TODO"},
    'path2-shared-flats': {
        'ezdefault': "Absolute path to flats", 
        'type': str, 
        'help': "TODO"},
    'shared-flats-after': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'path2-shared-flats2': {
        'ezdefault': "Absolute path to flats2", 
        'type': str, 
        'help': "TODO"},
    'shared-df-used': {
        'ezdefault': False,
        'type': bool,
        'help': "Internal variable; must be set to True once "
                "shared flats/darks were used in the recontruction pipeline"},
    'halfacq_dir': {
        'ezdefault': "Absolute path to half acqusition mode working directory",
        'type': str,
        'help': "TODO"},
}

EZVARS['COR'] = {
    'search-method': {
        'ezdefault': 1,
        'type': int, 
        'help': "TODO"},
    'search-interval': {
        'ezdefault': "1010,1030,0.5",
        'type': str, 
        'help': "TODO"},
    'patch-size': {
        'ezdefault': 800,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Size of reconstructed patch [pixel]"},
    'search-row': {
        'ezdefault': 400,
        'type': restrict_value((0,None), dtype=int), 
        'help': "Search in slice from row number"},
    'min-std-apply-pr': {
        'ezdefault': False,
        'type': bool,
        'help': "Will apply phase retreival but only while estimating the axis"},
    # 'user-defined-ax': {
    #     'ezdefault': 0.0,
    #     'type': restrict_value((0,None), dtype=float),
    #     'help': "Axis is in column No [pixel]"},
    'user-defined-ax': {
        'ezdefault': '0.0',
        'type': str,
        'help': "Axis is in column No [pixel] \n"
                "If "},
    'user-defined-dax': {
        'ezdefault': 0.0,
        'type': float, 
        'help': "TODO"},
}

EZVARS['retrieve-phase']= {
    'apply-pr': {
        'default': False,
        'ezdefault': False,
        'type': bool,
        'help': "Applies phase retrieval if checked"}
}

EZVARS['filters'] = {
    'rm_spots': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO-G"},
    'rm_spots_use_median': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO-G"},
    # 'spot-threshold': {
    #     'ezdefault': 1000,
    #     'type': restrict_value((0,None), dtype=float),
    #     'help': "TODO-G"}
}

EZVARS['RR'] = {
    'enable-RR': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO-G"},
    'use-ufo': {
        'ezdefault': True,
        'type': bool, 
        'help': "TODO-G"},
    'ufo-2d': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'sx': {
        'ezdefault': 13,
        'type': restrict_value((0,None),dtype=int), 
        'help': "ufo ring-removal sigma horizontal (try 3..31)"},
    'sy': {
        'ezdefault': 1,
        'type': restrict_value((0,None),dtype=int), 
        'help': "ufo ring-removal sigma vertical (try 1..5)"},
    'spy-narrow-window': {
        'ezdefault': 21,
        'type': restrict_value((0,None),dtype=int), 
        'help': "window size"},
    'spy-rm-wide': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'spy-wide-window': {
        'ezdefault': 91, 
        'type': restrict_value((0,None),dtype=int), 
        'help': "wind"},
    'spy-wide-SNR': {
        'ezdefault': 3, 
        'type': restrict_value((0,None),dtype=int), 
        'help': "SNR"},
}

EZVARS['flat-correction'] = {
    'smart-ffc': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'smart-ffc-method': {
        'ezdefault': "eigen",
        'type': str, 
        'help': "TODO"},
    'eigen-pco-reps': {
        'ezdefault': 4,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Flat Field Correction: Eigen PCO Repetitions"},
    'eigen-pco-downsample': {
        'ezdefault': 2,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Flat Field Correction: Eigen PCO Downsample"},
    'downsample': {
        'ezdefault': 4,
        'type': restrict_value((0,None),dtype=int), 
        'help': "Flat Field Correction: Downsample"},
    'dark-scale': {
        'ezdefault': 1.0,
        'type': float, 
        'help': "Scaling dark"}, #(?) has the same name in SECTION
    'flat-scale': {
        'ezdefault': 1.0,
        'type': float, 
        'help': "Scaling falt"}, #(?) has the same name in SECTION
}

#TODO ADD CHECKING NLMDN SETTINGS
EZVARS['nlmdn'] = {
    'do-after-reco': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'input-dir': {
        'ezdefault': os.getcwd(),
        'type': str, 
        'help': "TODO"},
    'input-is-1file': {
        'ezdefault': False, 
        'type': bool, 
        'help': "TODO"},
    'output_pattern': {
        'ezdefault': os.getcwd() + '-nlmfilt',
        'type': str, 
        'help': "TODO"},
    'bigtiff_output': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'search-radius': {
        'ezdefault': 10,
        'type': int, 
        'help': "TODO"},
    'patch-radius': {
        'ezdefault': 3,
        'type': int, 
        'help': "TODO"},
    'h': {
        'ezdefault': 0.0,
        'type': float, 
        'help': "TODO"},
    'sigma': {
        'ezdefault': 0.0,
        'type': float, 
        'help': "TODO"},
    'window': {
        'ezdefault': 0.0,
        'type': float, 
        'help': "TODO"},
    'fast': {
        'ezdefault': True,
        'type': bool, 
        'help': "TODO"},
    'estimate-sigma': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'dryrun': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
}


EZVARS['advanced'] = {
    'more-reco-params': {
        'ezdefault': False,
        'type': bool, 
        'help': "TODO"},
    'parameter-type': {
        'ezdefault': "", 
        'type': str, 
        'help': "TODO"},
    'enable-optimization': {
        'ezdefault': False,
        'type': bool,
        'help': "TODO"
    }   
}