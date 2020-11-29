import numpy as np
import os
import cv2 as cv
import argparse
import glob


def main():

    # list of all content in a directory, filtered so only directories are returned
    dir_list = [ args.path + directory for directory in os.listdir( args.path) if os.path.isdir( args.path + directory)]
    print(dir_list)


    for i in dir_list:
        internal_directory = [i + '/' + directory for directory in os.listdir(i) if os.path.isdir(i + '/' + directory)]
        f0 = (os.path.basename(i))

        for j in internal_directory:
            if str(j).endswith('/training/disp_occ_1') or str(j).endswith('/validation/disp_occ_1'):
                continue
            listing = os.listdir(j)
            for img in listing:
                file0 = os.path.join(j, img)
                im = cv.imread(file0)

                width, height = im.shape[1], im.shape[0]
                assert width == height

                fov_omni = np.pi
                f_omni = width / fov_omni
                c = (width - 1) / 2

                K_omni = np.array([[f_omni, 0, c],
                                   [0, f_omni, c],
                                   [0, 0, 1]])

                # perspective field of view
                fov_deg = 60
                fov = fov_deg * np.pi / 180.0

                elev = fov / 2
                f_persp = width / (2 * np.tan(elev))
                print("f_persp:", f_persp)

                K_persp = np.array([[f_persp, 0, c],
                                    [0, f_persp, c],
                                    [0, 0, 1]])

                k_1, k_2, k_3, k_4 = 0.0, 0.0, 0.0, 0.0

                D = np.array([k_1, k_2, k_3, k_4])

                interpol = cv.INTER_LINEAR
                map_x = None
                map_y = None

                p_1, p_2 = 0.0, 0.0  # tangential distortion
                k_5, k_6 = 0.0, 0.0

                """
                             Undistorting the images
                """

                map_x, map_y = cv.fisheye.initUndistortRectifyMap(K=K_omni, D=D, R=np.eye(3),P=K_persp, size=(width, height), m1type=cv.CV_16SC2)

                if str(j).endswith('/training/disp_occ_0') or str(j).endswith('/validation/disp_occ_0') or str(j).endswith('/testing/disp_occ_0'):
                    dst3 = cv.remap(im[:,:,1], map_x, map_y, interpolation=interpol, borderMode=cv.BORDER_CONSTANT)
                else:
                    dst3 = cv.remap(im, map_x, map_y, interpolation=interpol, borderMode=cv.BORDER_CONSTANT)

                f1 = (os.path.basename(j))
                print(args.outputPath +  f0  + "/"+ f1)
                if os.path.isdir(args.outputPath +  f0  + "/"+ f1):
                    cv.imwrite(args.outputPath +  f0  + "/"+ f1 + "/" + img, dst3)
                else:
                    os.makedirs(args.outputPath +  f0  + "/"+ f1)
                    cv.imwrite(args.outputPath +  f0  + "/"+ f1  + "/"  + img, dst3)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('--path', default='/mnt/data/haahm/anynet/',
                        help='path')

    parser.add_argument('--outputPath', default='/mnt/data/haahm/Finalising_everything/',
                        help='outputPath')

    args = parser.parse_args()

    main()
