import os
import sys
import argparse
from openslide import OpenSlide
from PIL import Image
from multiprocessing import Pool, cpu_count

def resize_svs_to_multiple_images(svs_file_path, output_folder, output_format='JPEG', scale_factors=[1.0, 0.5, 0.25, 0.125]):
    slide = OpenSlide(svs_file_path)

    for scale_factor in scale_factors:
        new_width = int(slide.dimensions[0] * scale_factor)
        new_height = int(slide.dimensions[1] * scale_factor)

        region = slide.read_region((0, 0), 0, slide.dimensions)
        resized_image = region.resize((new_width, new_height), Image.ANTIALIAS)

        base_name = os.path.splitext(os.path.basename(svs_file_path))[0]
        output_file_path = os.path.join(output_folder, f"{base_name}_{int(scale_factor * 100)}x.{output_format.lower()}")

        resized_image.save(output_file_path, output_format)

def process_svs_file(args):
    input_svs_file, output_folder, output_image_format, scale_factors = args
    resize_svs_to_multiple_images(input_svs_file, output_folder, output_image_format, scale_factors)

def process_multiple_svs_files(input_folder, output_folder, output_image_format='JPEG', scale_factors=[1.0, 0.5, 0.25, 0.125], num_processes=None):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    svs_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.lower().endswith('.svs')]

    args = [(svs_file, output_folder, output_image_format, scale_factors) for svs_file in svs_files]

    if num_processes is None:
        num_processes = cpu_count()

    with Pool(processes=num_processes) as pool:
        pool.map(process_svs_file, args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process multiple SVS files and save resized images')
    parser.add_argument('-i', '--input', type=str, required=True, help='Input folder containing SVS files')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output folder for resized images')
    parser.add_argument('--scale_factors', nargs='+', type=float, default=[1.0, 0.5, 0.25, 0.125], help='Space-separated list of scale factors (default: 40x, 20x, 10x, 5x)')
    parser.add_argument('--num_processes', type=int, default=None, help='Number of processes to use (default: all available CPU cores)')
    parser.add_argument('--format', type=str, choices=['JPEG', 'PNG'], default='JPEG', help='Output image format (default: JPEG)')

    args = parser.parse_args()

    process_multiple_svs_files(args.input, args.output, args.format, args.scale_factors, args.num_processes)
