import scipy as sp
import imageio as iio
import numpy as np
import matplotlib.pyplot as plt
import time
import sys


# def progressbar(current, total):
#     progress = int(current / total * 50)
#     barstatus = "│" + ("█" * progress) + ("░" * (49 - progress)) + "│ " + str(int((progress / 50 * 100) + 2)) + "%"
#     print(f'\r{barstatus}', end='')


def rgb_to_bw(im):
    im_bw = 0.299 * im[:, :, 0] + 0.587 * im[:, :, 1] + 0.114 * im[:, :, 2]
    im_bw -= np.amin(im_bw)
    im_bw *= 255 / np.amax(im_bw)
    # return im_bw
    return np.rint(im_bw).astype(int)


def conv_2d(x, h):
    h = np.fliplr(h)
    h = np.flipud(h)

    x_height, x_width = x.shape

    return_array = np.zeros((x_height, x_width))

    padding_to_add = int(h.shape[0] / 2) * 2
    start = int(padding_to_add / 2)
    padded_array = np.zeros((x_height + padding_to_add, x_width + padding_to_add))

    padded_array[start:-start, start:-start] = x

    left = 0
    top = 0
    right = int(left + h.shape[1])
    bottom = int(top + h.shape[0])

    for col in range(x_height):
        for row in range(x_width):
            return_array[col, row] = np.sum(np.multiply(padded_array[top:bottom, left:right], h))
            # print(left, x_width)
            if left < x_width - 1:
                left += 1
            else:
                top += 1
                left = 0
            right = int(left + h.shape[1])
            bottom = int(top + h.shape[0])
    return return_array


#
def normalize(im, im_min=0, im_max=255):
    im = np.clip(im, im_min, im_max)
    return im


def blur(im):
    gaussian_blur_kernel = np.array([[1, 4, 7, 4, 1],
                                     [4, 16, 26, 16, 4],
                                     [7, 26, 41, 26, 7],
                                     [4, 16, 26, 16, 4],
                                     [1, 4, 7, 4, 1]])
    gaussian_blur_kernel = (1 / 273) * gaussian_blur_kernel
    temp = conv_2d(im, gaussian_blur_kernel)
    temp = normalize(temp)
    # diff = 0
    # for ii in range(im.shape[0]):
    #     for jj in range(im.shape[1]):
    #         diff += np.absolute(im[ii, jj] - temp[ii, jj])
    #         # if np.absolute(im[ii,jj] - temp[ii,jj]) < 0.0001:
    #         #     diff += 1
    # print(diff / im.size)
    return temp


def sharpen(im, strength):
    laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    temp_gaussian = blur(im)
    temp_gaussian_edge_detect = conv_2d(temp_gaussian, laplacian_kernel)
    return normalize(temp_gaussian_edge_detect + im)


def main():
    try:
        if len(sys.argv) < 5:
            strength = 1
        else:
            strength = sys.argv[4]

        proc_type = sys.argv[1]
        img = sys.argv[2]
        output_name = sys.argv[3]

        valid_proc = ['blur', 'sharpen', 'bw']  # Check Proc
        assert (proc_type in valid_proc)

        img = iio.imread(img).astype(float)

        grayscale = 0

        if proc_type == 'blur':  # Run correct method
            processed_img = blur(img)
        if proc_type == 'sharpen':
            processed_img = sharpen(img, strength)
        if proc_type == 'bw':
            processed_img = rgb_to_bw(img)

        iio.imwrite(processed_img)

        # plt.imshow(grayscale, cmap='gray')
        # plt.show()
    except AssertionError:
        err_string_proc = "processing type must be blur, sharpen, or bw"
        print(err_string_proc)
    except IndexError:
        err_string_usage = ("Usage:\n"
                            "    $ python imageprocessing.py <proc_type> "
                            "<input_image> <output_image> "
                            "[strength (default=1)]")
        print(err_string_usage)


if __name__ == "__main__":
    main()
