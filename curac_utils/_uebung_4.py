# -*- coding: utf-8 -*-

from skimage import io, img_as_float
import numpy as np
import pkg_resources


class Uebung_4():

    @staticmethod
    def aufg_1_get_pointclouds():

        x_1 = np.array([
            [50, 100, 50, 1],
            [100, 100, 50, 1],
            [75, 75, 75, 1],
            [50, 50, 50, 1],
            [100, 50, 50, 1],
            [50, 100, 100, 1],
            [100, 100, 100, 1],
            [50, 50, 100, 1],
            [100, 50, 100, 1],
        ])

        x_2 = np.array([
            [101.19, 116.87, 70.00, 1],
            [148.17, 99.77, 70.00, 1],
            [116.13, 84.83, 95.00, 1],
            [84.09, 69.88, 70.00, 1],
            [131.07, 52.78, 70.00, 1],
            [101.19, 116.87, 120.00, 1],
            [148.17, 99.77, 120.00, 1],
            [84.09, 69.88, 120.00, 1],
            [131.07, 52.78, 120.00, 1],
        ])

        return x_1, x_2

    @staticmethod
    def aufg_2_b_get_imgs():

        ct_path = pkg_resources.resource_filename(__name__, 'data/ct_g.jpg')
        mrt_path = pkg_resources.resource_filename(__name__, 'data/mrt_g.jpg')

        ct_g = img_as_float(io.imread(ct_path))
        mrt_g = img_as_float(io.imread(mrt_path))

        return ct_g, mrt_g

    @staticmethod
    def aufg_2_c_get_imgs():

        ct_path = pkg_resources.resource_filename(__name__, 'data/ct_fid1.jpg')
        mrt_path = pkg_resources.resource_filename(__name__, 'data/mrt_fid1_t1.jpg')

        ct_g = img_as_float(io.imread(ct_path))
        mrt_g = img_as_float(io.imread(mrt_path))

        return ct_g, mrt_g

    @staticmethod
    def aufg_2_d_get_imgs():

        ct_path = pkg_resources.resource_filename(__name__, 'data/ct_fid2.jpg')
        mrt_path = pkg_resources.resource_filename(__name__, 'data/mrt_fid2_t1.jpg')

        ct_g = img_as_float(io.imread(ct_path))
        mrt_g = img_as_float(io.imread(mrt_path))

        return ct_g, mrt_g

    @staticmethod
    def aufg_3_get_imgs():
        x_1 = np.array([
            [2,2,7,7,7,3,3],
            [2,2,2,2,2,2,2],
            [1,1,1,2,3,3,3],
            [6,4,7,3,4,5,5],
            [6,6,6,4,4,2,2],
            [6,6,6,4,4,2,2],
            [6,6,6,4,4,2,2]
        ])

        x_2 = np.array([
            [4,4,8,8,8,5,5],
            [4,4,4,4,4,4,4],
            [1,1,1,4,5,5,5],
            [2,4,8,3,4,6,6],
            [2,2,2,4,4,4,4],
            [2,2,2,4,4,4,4],
            [2,2,2,4,4,4,4],
        ])

        return x_1, x_2

    @staticmethod
    def aufg_4_d_get_pointclouds():

        pc1_path = pkg_resources.resource_filename(__name__, 'data/pointcloud1.xyz1')
        pc2_path = pkg_resources.resource_filename(__name__, 'data/pointcloud2.xyz1')

        pc1 = np.loadtxt(pc1_path)
        pc2 = np.loadtxt(pc2_path)

        return pc1, pc2
