# 1. Mini Project

- [1. Mini Project](#1-mini-project)
  - [1.1. Data Source](#11-data-source)
  - [1.2. Aim](#12-aim)
  - [1.3. Methodology](#13-methodology)
    - [1.3.1. Using OpenCV](#131-using-opencv)
    - [1.3.2. Preprocessing](#132-preprocessing)
  - [1.4. The Main Algorithm](#14-the-main-algorithm)
    - [1.4.1. Problems With The Main Algorithm](#141-problems-with-the-main-algorithm)
    - [1.4.2. Dynamic Cropping](#142-dynamic-cropping)
    - [1.4.3. Subtracting Images](#143-subtracting-images)
  - [1.5. The Second Algorithm: All Points Method](#15-the-second-algorithm-all-points-method)
    - [1.5.1. Why Another Algorithm?](#151-why-another-algorithm)
    - [1.5.2. Extracting All Points](#152-extracting-all-points)
    - [1.5.3. Fitting An Ellipse](#153-fitting-an-ellipse)
  - [1.6. The Final Algorithm](#16-the-final-algorithm)
  - [1.7. Results](#17-results)
  - [1.8. Question Section](#18-question-section)
    - [1.8.1. What were the most challenging aspect of the project and how you overtook it?](#181-what-were-the-most-challenging-aspect-of-the-project-and-how-you-overtook-it)
    - [1.8.2. What improvements can be made?](#182-what-improvements-can-be-made)
    - [1.8.3. Why did this algorithm work or didn't work?](#183-why-did-this-algorithm-work-or-didnt-work)
    - [1.8.4. If you were to do something differently, what would that be?](#184-if-you-were-to-do-something-differently-what-would-that-be)
    - [1.8.5. Some mistakes you made](#185-some-mistakes-you-made)

## 1.1. Data Source

The data was given to us by the professor. It was generated by previous year's Ph.D. students. They performed variuos experiments where they dropped the drop of water from various heights and also the angle of the thin film was also choses differently.

There are a number of videos each having frames ranging 50-200. Videos are typically of two types, one where the height is varied and other where the angle is varied.

## 1.2. Aim

Our goal was to write an algorithms which can extract the coordinates and radii of the center of the drop. Once we get these information, further studies can be performed on the data.

## 1.3. Methodology

We implemented a number of algorithms for this. These algorithms were implemented from scratch in Pyhton and numpy.

### 1.3.1. Using OpenCV

We tried using OpenCV, specifically the `HoughCircles` function. This function takes in the image and the parameters and returns the coordinates and radii of the circles. We tried using this function on the images and videos. The circles were not detected properly. We tried changing the parameters but the results were not satisfactory.

### 1.3.2. Preprocessing

There were a number of steps involved before we can feed the image to the algorithm. These steps were:

1. **Cropping:** The region of interest was just a small frcation of the image, so, the image was cropped to the region of interest.
2. The image was already grayscale, so, we did not have to convert it to grayscale.
3. **Subtracting From Base Image:** This was done to remove the background noise.
4. **Thresholding:** The image was thresholded to get a binary image. This was done to remove the noise from the image.

## 1.4. The Main Algorithm

The main idea behind the algorithm was to use the contrast between the background and the circumference of the drop to detect its center. The main algorithm is:

1. Loop through the rows and find the first and last pixel which is not black.
2. Repeat the same for the columns.
3. Use these four points to find the center of the drop and the radii.

### 1.4.1. Problems With The Main Algorithm

The main algorithm was unsuccessful while detecting the drop when it was near the needle or the thin film. Also, we needed to give the crop coordinates (`(x,y,h,w)`) of each the points for it to work. This was not a good solution. Solution to the second problem was by using dynammic cropping.

### 1.4.2. Dynamic Cropping

Here, the crop coordinates were calculated dynamically. The algorithm was:

1. Initialize by first giving the crop coordinates.
2. The algorithm determines the center of the drop and the radii.
3. Use this value of the center to calculate the new crop coordinates.
4. Reapeat the process.

Even dynamic programming was not able to solve all the problem. First, we still needed to give the first crop coordinates. Second, the algorithm was still not able to detect the drop when it was near the thin film. So basically, we needed to run the algorithm on three different regions of the image, providing the crop coordinates for each of them.

### 1.4.3. Subtracting Images

The next idea was to subtract the background from the image and then use the main algorithm. For this, an image with no drop was taken and subtracted from the image with the drop. This resulted in a image which had just the drop with some light noise which can then be removed by thresholding. Using the main algorithm with dynamic cropping and subtracting the images, we were able to detect the drop in almost all the cases.

## 1.5. The Second Algorithm: All Points Method

### 1.5.1. Why Another Algorithm?

The main algorithm, though working correctly, had some limitations. First, it was missing a lot of frames when the drop was near the thin film. Secondly, watching the videos, we observed that the drop was oscillating and we wanted to detect these oscillations. For this things, we needed another algorithm.

### 1.5.2. Extracting All Points

The first step was to extract all the points on the circumference of the drop. This was done again, by looping through rows and columns and adding each white pixel to a list.

### 1.5.3. Fitting An Ellipse

The next step was to fit an ellipse to the points. This was done using the `skimage.measure.fit_ellipse` function. This function takes in the points and returns the center, the major and minor axis and the angle of rotation.

## 1.6. The Final Algorithm

This was a combination of the second algorithm with dynamic cropping and subtracting the images. We also tried using the algorithm on grayscale images however the result was not good. So, we used the algorithm on the binary images.

## 1.7. Results

The coordinates of center and the radii, as well as the angle of rotation for over 40 videos (spanning over 5000 frames) were extracted. The results were stored in a csv file. The csv file was then used to do some rudimentary analysis.

## 1.8. Question Section

### 1.8.1. What were the most challenging aspect of the project and how you overtook it?

It was to generalize the algorithm we created. Even after cropping, the algorithm was not robust in a sense that we needed to give coordinates for crop of each frame. Also, if the drop was near the needle and the thin film, the algorith was not working. This problem was partially solved by using the dynamic cropping and by subtracting images.

### 1.8.2. What improvements can be made?

The algorithm still is not detecting drops all the time. When the drop is near the thin film, it fails. Also, for some frames, the coordinates extracted by the drop is not at the position of the drop. We can improve our algorithm to take into account these problems.

### 1.8.3. Why did this algorithm work or didn't work?

The algorithm assumes that there are not white points other than that formed by the circumference of the drop. If it finds some white point at places other than this, it will think that it is at the circumference of the drop and give wrong result.

### 1.8.4. If you were to do something differently, what would that be?

I might try to write an algorithm which determines whether a point is on the circumference of the circle by not only looping through the rows and columns but also by keeping track of where the previous points are and whether they are related to each other in a way which forms a "circle"?

### 1.8.5. Some mistakes you made