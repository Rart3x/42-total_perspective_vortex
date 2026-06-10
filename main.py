from mne.datasets import eegbci

raw_files = eegbci.load_data(subjects=1, runs=[1, 2, 3], path="./dataset")