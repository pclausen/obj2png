import sys
import os
import zipfile

# assumed being called from obj2png/
sys.path.append("./src")
sys.path.append("../src")

import numpy as np

# because of display issue on travis
# https://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server
import matplotlib as mpl

mpl.use("Agg")

import ObjFile

import unittest


class TestObjFile(unittest.TestCase):

    # changed from Doc Test to UnitTest
    def test_open_obj(self):

        """
        >>> obj_file = '../obj/bun_zipper_res2.obj'
        >>> out_file = '../obj/bun_zipper_res2.png'
        >>> obj = ObjFile(obj_file)
        >>> len(obj.nodes)==8147
        True
        >>> len(obj.faces)==16301
        True
        >>> nmin,nmax=obj.MinMaxNodes()
        >>> np.allclose(nmin, np.array([-0.094572,  0.      , -0.061874]) )
        True
        >>> np.allclose(nmax, np.array([0.060935, 0.186643, 0.05869 ]))
        True
        >>> obj.Plot(out_file)
        """

        obj_file = "./obj/bun_zipper_res2.obj"
        odir = "test_output"
        if not os.path.exists(odir):
            os.mkdir(odir)
        out_file = os.path.join(odir, "bun_zipper_res2.png")
        obj = ObjFile.ObjFile(obj_file)
        # print(obj.ObjInfo())
        self.assertTrue(len(obj.nodes) == 8147)
        self.assertTrue(len(obj.faces) == 16301)
        nmin, nmax = obj.MinMaxNodes()
        self.assertTrue(np.allclose(nmin, np.array([-0.094572, 0.0, -0.061874])))
        self.assertTrue(np.allclose(nmax, np.array([0.060935, 0.186643, 0.05869])))
        if os.path.isfile(out_file):
            os.unlink(out_file)
        obj.Plot(out_file)
        self.assertTrue(os.path.isfile(out_file))

    def test_obj_zip(self):
        obj_file_zip = "./obj/rp_janna_posed_004_30k.zip"
        odir = "test_output"
        obj_file = "./obj/rp_janna_posed_004_30k.obj"
        with zipfile.ZipFile(obj_file_zip, "r") as zip_ref:
            zip_ref.extract(os.path.basename(obj_file), os.path.dirname(obj_file))

        if not os.path.exists(odir):
            os.mkdir(odir)
        out_file = os.path.join(odir, "rp_janna_posed_004_30k.png")
        obj = ObjFile.ObjFile(obj_file)
        # print(obj.ObjInfo())
        self.assertTrue(len(obj.nodes) == 27555)
        self.assertTrue(len(obj.faces) == 55104)
        nmin, nmax = obj.MinMaxNodes()
        self.assertTrue(np.allclose(nmin, np.array([-0.799216, -1.091205, -0.126377])))
        self.assertTrue(np.allclose(nmax, np.array([0.80038, 0.517024, 0.153965])))
        if os.path.isfile(out_file):
            os.unlink(out_file)
        obj.Plot(out_file)
        self.assertTrue(os.path.isfile(out_file))

    def test_face_format(self):
        obj_file = "./obj/test.obj"
        obj = ObjFile.ObjFile(obj_file)


if __name__ == "__main__":
    unittest.main()
