import argparse

import vtk


def main(png0, png1, threshold=0.15):
    # load the two input images
    img0 = vtk.vtkPNGReader()
    img0.SetFileName(png0)
    img0.Update()

    img1 = vtk.vtkPNGReader()
    img1.SetFileName(png1)
    img1.Update()

    # compare the two images
    imdiff = vtk.vtkImageDifference()
    imdiff.SetInputConnection(img0.GetOutputPort())
    imdiff.SetImageConnection(img1.GetOutputPort())
    imdiff.Update()

    err = round(imdiff.GetThresholdedError(), 3)

    if err > threshold:
        return (False, err)

    return (True, err)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="test image", type=str)
    parser.add_argument("ref", help="reference image", type=str)
    args = parser.parse_args()
    main(args.test, args.ref)
