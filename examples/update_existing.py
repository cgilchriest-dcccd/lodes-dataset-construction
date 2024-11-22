
"""
this script demonstrates how you can build a lodes spatialdb from your scratch
the example is for texas but it would work for any state
note: the load_up_geometries function at the end would likely require the most work for a state other than texas
"""
import sys
sys.path.append(r"P:\Labor_Market_Intelligence\GIS Data Resources\Python Functions\LODES Dataset Construction\main")
from download_and_unzip import *
from build_database import *
import os

#define paths
wkd = r"C:\Users\cmg0003\Desktop"
spath = os.path.join(wkd,"lodes_tx_slim.db")

# --- processing
#get all the potential files
fps = get_all_possible_files(save=True,
                             savepath=wkd,
                             savename="state_dict")

#just download 2022
fouts = filter_for_single_year_files(links_dict=fps,year='2022',state_cd='tx')


#this unzips everything 
unzip_state_lodes_file(state_fold= state_fold)


# loads downloaded data into spatialite 
#build_db(spath=spath) #be careful - this build function overwrites existing data
#state_fold = r"C:\Users\cmg0003\Desktop\TX_Lodes_Download\tx"
load_lodes_into_db(folder_path = state_fold,spath = spath, base_only = True)

