import glob
from PIL import Image
import argparse
import os
import numpy as np
from natsort import natsorted
import cv2
from glob import glob
from tqdm import tqdm

def make_gif(frame_folder, type, total_time, repeat, result):
    files = natsorted(glob(os.path.join(frame_folder, f'*.{type}')))
    frames = [Image.open(image).convert('RGB').quantize(method=Image.MEDIANCUT) for image in files]
    frame_one = frames[0]
    frame_one.save(os.path.join(result, 'result.gif'), format="GIF", append_images=frames[1:],
                   save_all=True, duration=(total_time / len(frames)) * 1000, loop=repeat)


def make_essential_frames(restored, noise, type, scale, step, frame_dir):
    restored = cv2.imread(str(natsorted(glob(os.path.join(restored, f'*.{type}')))[0]))
    noise = cv2.imread(str(natsorted(glob(os.path.join(noise, f'*.{type}')))[0]))
    if restored.shape != noise.shape: raise Exception('\nTwo images have to be the same resolution!')
    h, w, c = restored.shape
    resize_restored = cv2.resize(restored, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_CUBIC)
    resize_noise = cv2.resize(noise, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_CUBIC)
    r_h, r_w, r_c = resize_restored.shape

    start_frame = resize_noise
    cv2.imwrite(os.path.join(frame_dir, f'frame_0000.{type}'), start_frame)

    data_file = 1
    for i in tqdm(range(0, (w//step)*step, step)):
        left = resize_restored[0:r_h, 0:(step + i)]
        right = resize_noise[0:r_h, (step + i):r_w]
        combine = np.concatenate((left, right), axis=1)
        cv2.imwrite(os.path.join(frame_dir, f'frame_{str(data_file).zfill(4)}.{type}'), combine)
        data_file += 1

    cv2.imwrite(os.path.join(frame_dir, f'frame_last.{type}'), resize_restored)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--frame_dir', default='./frames', type=str)
    parser.add_argument('--resize_scale', default=1, type=float)
    parser.add_argument('--step', default=10, type=int, help='each frame with [step] pixels')
    parser.add_argument('--type', default='png')
    parser.add_argument('--frequency', default=3, type=float, help='spending seconds in single loop')
    parser.add_argument('--repeat_GIF', default=0, type=int, help='0: repeat, 1: no repeat')
    parser.add_argument('--result_dir', default='.', type=str)
    args = parser.parse_args()

    frame_dir = args.frame_dir
    os.makedirs(frame_dir, exist_ok=True)

    dirRestored = './restored/'
    dirNoise = './noise/'
    type = args.type
    step = args.step
    resize_scale = args.resize_scale
    frequency = args.frequency
    repeat_GIF = args.repeat_GIF
    result_dir = args.result_dir
    os.makedirs(result_dir, exist_ok=True)
    print('Generate essential frames of gif: ')
    make_essential_frames(dirRestored, dirNoise, type, resize_scale, step, frame_dir)
    print('Generate GIF image: ')
    make_gif(frame_dir, type, frequency, repeat_GIF, result_dir)
    print('Finish !!')
