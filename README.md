# Resizing-and-Saving-SVS-Files-to-JPG
Resizing and convert .svs files (commonly used for high-resolution medical images) to .jpg or .png format

In this example, the process_multiple_svs_files function has a new num_processes parameter, which defaults to None. If the num_processes parameter is not specified, the function uses all available CPU cores. If you want to set a fixed number of processes, pass it as an argument when calling the process_multiple_svs_files function. In this example, num_processes is set to half of the available CPU cores with cpu_count() // 2.

Make sure to install the OpenSlide and Pillow libraries in your Python environment:
pip install openslide-python pillow
pip install pillow

An argparse.ArgumentParser is created with options for input and output folders, scale factors, the number of processes, and the output image format. The user can now provide these options when running the script. For example:
python script.py -i input_svs_files -o output_images --scale_factors 1.0 0.5 0.125 --num_processes 4 --format JPEG
