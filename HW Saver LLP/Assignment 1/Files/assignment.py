import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os


def get_image_ready(img_path, threshold=120, crop=(5, 5)):
    """
    Does preprocessing on the image

    Parameters
    ----------
    img_path : str
        Path to the image
    threshold : int, optional
        Threshold value for the image. The default is 120.
    crop : tuple, optional
        x and y crop pixels for the image. The default is (5,5).

    Returns
    -------
    numpy.ndarray
        Image after preprocessing
    """
    img = cv.imread(img_path)
    if crop:
        img = img[crop[1] : img.shape[0] - crop[1], crop[0] : img.shape[1] - crop[0]]
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    _, binary_image = cv.threshold(gray_image, threshold, 1, cv.THRESH_BINARY)
    return binary_image


def y_coordinates(img, a):
    """
    Gets the y coordinates of the top and bottom sides of the checkbox

    Parameters
    ----------
    img : numpy.ndarray
        Image to be processed
    a : int
        index of the column to be looped over

    Returns
    -------
    tuple ((x,yt), (x,yb))
        coordinates of the top and bottom of the checkbox
    """
    col = np.nonzero(img[:, a])[0]
    colshifted = np.concatenate([col[1:], np.array([0])])
    c1 = col[(-col + colshifted > 1)][0]
    colshifted = np.concatenate([np.array([0]), col[:-1]])
    c2 = col[(col - colshifted > 1)][-1]
    return (a, c1), (a, c2)


def x_coordinates(img, a):
    """
    Gets the x coordinates of the left and right sides of the checkbox

    Parameters
    ----------
    img : numpy.ndarray
        Image to be processed
    a : int
        index of the row to be looped over

    Returns
    -------
    tuple ((xl,y), (xr,y))
        coordinates of the left and right of the checkbox
    """
    row1 = np.nonzero(img[a, :])[0]
    row1shifted = np.concatenate([row1[1:], np.array([0])])
    c1 = row1[(-row1 + row1shifted > 1)][0]
    row1shifted = np.concatenate([np.array([0]), row1[:-1]])
    c2 = row1[(row1 - row1shifted > 1)][-1]
    return (c1, a), (c2, a)


def checked(img, percent=35):
    """
    Returns `True` if the checkbox is checked, `False` otherwise

    Parameters
    ----------
    img : numpy.ndarray
        Image to be processed
    percent : int, optional
        Percentage of the image to be checked. The default is 20.

    Returns
    -------
    bool
        `True` if the checkbox is checked, `False` otherwise
    """
    h, w = img.shape
    # The area of cropped image will be 1/4 of the original image
    all_pixels = 3 * h * w / 4
    h_check = h // 8
    w_check = w // 8
    # cropping the center part of image
    white_pixels = (img[h_check : h - h_check, w_check : w - w_check]).sum()
    white_percent = white_pixels * 100 / all_pixels
    black_percent = 100 - white_percent
    return black_percent > percent


def putting_together(
    img_path,
    threshold=140,
    point=None,
    crop=(5, 5),
    percent=35,
    plot=True,
    save=False,
    pad=0,
):
    """
    Detects the checkbox as well as whether it is checked or not

    Parameters
    ----------
    img_path : str
        Path to the image
    threshold : int, optional
        Threshold value for the image. The default is 140.
    point : tuple, optional
        x and y coordinates to loop over in `x_coordinates` and `y_coordinates` function. The default is None.
    crop : tuple, optional
        x and y crop pixels for the image. The default is (5,5).
    percent : int, optional
        Percentage used in the `checked` function. The default is 20.
    plot : bool, optional
        Whether to plot the image. The default is True.
    save : bool, optional
        Whether to save the cropped image. The default is False.
    pad : int, optional
        Padding to be added to the final cropped. The default is 0.
    """
    # Getting the image ready
    img_original = cv.imread(img_path)
    img = get_image_ready(img_path, threshold, crop=crop)

    # Getting the coordinates of the checkbox if not given
    if point is None:
        h, w = img.shape
        point = (w // 2, h // 2)
    (x, yt), (x, yb) = y_coordinates(img, point[1])
    (xl, y), (xr, y) = x_coordinates(img, point[0])

    # Determining whether the checkbox is checked or not
    checked_or_not = checked(
        img[crop[1] + yt : crop[1] + yb, crop[0] + xl : crop[0] + xr], percent
    )

    # Plotting the image
    if plot:
        fig, axes = plt.subplots(1, 2)
        # Adding a supertitle
        fig.suptitle(f"{img_path}", fontsize=16)

        # Plotting the image with the top-left and bottom-right coordinates
        axes[0].imshow(img_original)
        axes[0].scatter(crop[0] + xl, crop[1] + yt, c="r", s=30)
        axes[0].scatter(crop[0] + xr, crop[1] + yb, c="r", s=30)
        axes[0].scatter(crop[0] + xl, crop[1] + yt, c="r", s=30)
        axes[0].scatter(crop[0] + xr, crop[1] + yb, c="r", s=30)
        axes[0].set_title("Original Image")

        # Plotting the cropped image
        img_f = img_original[
            crop[1] + yt - pad : crop[1] + yb + pad,
            crop[0] + xl - pad : crop[0] + xr + pad,
            :,
        ]
        axes[1].imshow(img_f)
        axes[1].set_title("Cropped Image")
        # Adding whether the checkbox is checked or not
        color = "g" if checked_or_not else "b"
        axes[1].annotate(
            f"Checked: {checked_or_not}",
            (0, 0),
            (10, -20),
            xycoords="axes fraction",
            textcoords="offset points",
            va="top",
            fontsize=14,
            color=color,
        )

    if save:
        # Saving the image
        img_f = img_original[
            crop[1] + yt - pad : crop[1] + yb + pad,
            crop[0] + xl - pad : crop[0] + xr + pad,
            :,
        ]
        img_name = img_path.split(os.path.sep)[-1]
        img_dir = "os.path.sep".join(img_path.split(os.path.sep)[:-1])
        img_dir = os.path.join(img_dir, "cropped", "clean_" + img_name)
        plt.imsave(img_dir, img_f)
    return img_f, checked_or_not


def main():
    """
    The main function
    """
    images_dir = "Raw_Dataset"
    images = os.listdir(images_dir)
    images = [os.path.join(images_dir, i) for i in images if i.endswith(".jpg")]
    checked_dict = {}
    for img in images:
        img_f, checked_ = putting_together(img, plot=False, save=True)
        checked_dict[img] = checked_

    print(checked_dict)

    cleaned_imgs = os.listdir(os.path.join(images_dir, "cropped"))
    cleaned_imgs = [
        os.path.join(images_dir, "cropped", i)
        for i in cleaned_imgs
        if i.endswith(".jpg")
    ]
    plt.figure(figsize=(15, 15))
    plt.suptitle("Detected Checkboxes", fontsize=16)
    for i, img in enumerate(cleaned_imgs):
        plt.subplot(3, 3, i + 1)
        plt.imshow(cv.imread(img))
        plt.title(f"{img}")
        plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
