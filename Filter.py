import numpy as np
import cv2 as cv
import os
from matplotlib import pyplot as plt
import argparse
import shutil

def main():
    # list of all content in a directory, filtered so only directories are returned
    dir_list = [args.path + directory for directory in os.listdir(args.path) if os.path.isdir(args.path + directory)]
    print(dir_list)

    for i in dir_list:
        internal_directory = [i + '/' + directory for directory in os.listdir(i) if os.path.isdir(i + '/' + directory)]
        f0 = (os.path.basename(i))
        
        listing = os.listdir(internal_directory[1])
        for img in listing:
                file0 = os.path.join(internal_directory[1], img)
                im = cv.imread(file0)

                gray = cv.cvtColor(im,cv.COLOR_BGR2GRAY)
                height, width = im.shape[0],im.shape[1]
                area_shape = height * width

                ret, thresh = cv.threshold(gray, 100, 255, 0)
                contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

                cv.imshow('image',cv.drawContours(im, contours, -1, (0,255,0), 3))
                cv.waitKey(0)
                exit(0)

                largest_area=0;
                largest_contour_index=0

                for cnt in contours:
                    area = cv.contourArea(cnt)
                    if (area>largest_area):
                        largest_area=area
                        largest_contour_index=cnt
                print('Largest contour',largest_area)
                discard_probability = (largest_area/area_shape) * 100
                print('Probability',discard_probability)

                if (discard_probability <=70.0):

                    f1 = os.path.basename(internal_directory[1])
                    disp_occ_0 = os.path.basename(internal_directory[0])
                    image_2 = os.path.basename(internal_directory[2])

                    if os.path.isdir(args.outputPath + f0 + "/" + f1):
                        cv.imwrite(args.outputPath + f0 + "/" + f1 + "/" + img, im)

                        disp_occ_0_path = i + "/" + disp_occ_0 +'/'
                        file1 = os.path.join(disp_occ_0_path, img)
                        shutil.copy(file1, args.outputPath + f0 + '/'+disp_occ_0)

                        image_2_path = i + "/" + image_2 + '/'
                        file2 = os.path.join(image_2_path, img)
                        shutil.copy(file2, args.outputPath + f0 + '/' + image_2)

                    else:
                        os.makedirs(args.outputPath + f0 + "/" + f1)
                        cv.imwrite(args.outputPath + f0 + "/" + f1 + "/" + img, im)

                        disp_occ_0_path = i + "/" + disp_occ_0 +'/'
                        file1 = os.path.join(disp_occ_0_path, img)
                        shutil.copy(file1, args.outputPath + '/'+ f0 + '/' + disp_occ_0)

                        image_2_path = i + "/" + image_2 + '/'
                        file2 = os.path.join(image_2_path, img)
                        print('file2',file2)
                        shutil.copy(file2, args.outputPath + '/' + f0 + '/' + image_2)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Describe input and Output paths+'
                                                 '')
    parser.add_argument('--path', default='/mnt/data/haahm/Finalising_everything/',
                        help='path')

    parser.add_argument('--outputPath', default='/mnt/data/haahm/Finalising_everything_after_filter/',
                        help='outputPath')
    args = parser.parse_args()







    main()
