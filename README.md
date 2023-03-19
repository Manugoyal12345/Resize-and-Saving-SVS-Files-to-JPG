# Resizing-and-Saving-SVS-Files-to-JPG
Resizing and convert .svs files (commonly used for high-resolution medical images) to .jpg or .png format

Make sure to install the OpenSlide and Pillow libraries in your Python environment:
pip install openslide-python pillow
pip install pillow

An argparse.ArgumentParser is created with options for input and output folders, scale factors, the number of processes, and the output image format. The user can now provide these options when running the script. For example:

python script.py -i input_svs_files -o output_images --scale_factor 0.5 --num_processes 4 --format JPEG

By default, the num_processes parameter is set to None. In the process_multiple_svs_files function, if num_processes is None, it will use all available CPU cores on the system. This is achieved using the cpu_count() function from the multiprocessing module:

if num_processes is None:
    num_processes = cpu_count()

So, the default value for num_processes will be the total number of CPU cores available on the system where the script is executed.

