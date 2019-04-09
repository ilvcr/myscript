#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: image_filter_process.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: Tue Apr  9 11:36:15 2019
# Description: 真真真
#************************************************************************#


class imageFilter(object):
    '''
        真真真
    '''
    def __init__(self):
        pass

    def mean_filter_image(self, im):
        '''
            真opencv真真真
            真真:
                result = cv2.blur(真真 ,真�)
            真:
                真真(真, 真)真真真�,
                真真真�(3, 3)�(5, 5)
        '''
        #img = cv2.imread('test01.png')
        im_source = cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)

        # 真真
        im_result = cv2.blur(im_source, (5, 5))

        # 真真
        titles = ['Source Image', 'Blur Image'] 
        blur_image = [im_source, im_result] 
        for i in range(2): 
            plt.subplot(1,2,i+1)
            plt.imshow(blur_images[i], 'gray') 
            plt.title(titles[i]) 
            plt.xticks([])
            plt.yticks([]) 
        
        plt.show() 
        
        return im_source, im_result, blur_image


    def box_filter_image(self, im):
        '''
            真opencv真真真
            真真: 
                result = cv2.boxFilter(真真, 真真真, 真�, normalize真)
            真:
                真真真�int真, 真�"-1"真真真真�;
                真真真�(3, 3)�(5, 5)
        '''
        im_source = cv2.cvtColor(self.im, cv2.COLOR_BGR2RGB)
        
        #真真
        im_result = cv2.boxFilter(im_source, -1, (5,5), normalize=1) 
        
        #真真
        titles = ['Source Image', 'BoxFilter Image'] 
        box_filter_image = [im_source, im_result] 
        
        for i in range(2): 
            plt.subplot(1,2,i+1)
            plt.imshow(box_filter_image[i], 'gray') 
            plt.title(titles[i]) 
        plt.xticks([])
        plt.yticks([])
    
    plt.show() 
    
    return im_source, im_result, box_filter_image


    def gaussian_blur_filter_image(self, im):
        '''
            真opencv真真真
            真真:
                dst = cv2.GaussianBlur(src, ksize, sigmax)
            真:
                真真真�int真, 真�"-1"真真真真�
                真真真�(3, 3)�(5, 5)
        '''
        im_source = cv2.cvtColor(self.im,cv2.COLOR_BGR2RGB) 
        
        #真真 
        im_result = cv2.GaussianBlur(im_source, (3,3), 0) 
        
        #真真
        titles = ['Source Image', 'GaussianBlur Image'] 
        gaussian_filter_image = [im_source, im_result] 
        
        for i in range(2): 
            plt.subplot(1,2,i+1)
            plt.imshow(gaussian_filter_image[i], 'gray') 
            plt.title(titles[i]) 
            plt.xticks([])
            plt.yticks([]) 
        
        plt.show() 
        
        return im_source, im_result, gaussian_filter_image


    def median_blur_filter_image(self, im):
        '''
            真opencv真真真
            真真:
                dst = cv2.medianBlur(src, ksize)
            真:
                src真真�, ksize真真�;
                真真真1真�, �3�5�7�
        '''
        
        #真真
        im_result = cv2.medianBlur(self.im, 3) 
        
        #真真
        cv2.imshow("source img", self.im) 
        cv2.imshow("medianBlur", im_result) 
        
        #真真
        cv2.waitKey(0) 
        cv2.destroyAllWindows()
        
        return self.im, im_result


