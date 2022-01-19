# coding=utf-8
import os
import cv2


# step1 提取视频中的帧
def save_img():  # 提取视频中图片 按照每帧提取
    video_path = "输入视频所在路径"  # 视频所在的路径
    f_save_path = "输入保存图片的文件夹"  # 保存图片的上级目录
    videos = os.listdir(video_path)  # 返回指定路径下的文件和文件夹列表。
    for video_name in videos:  # 依次读取视频文件
        file_name = video_name.split('.')[0]  # 拆分视频文件名称 ，剔除后缀
        folder_name = f_save_path + file_name  # 保存图片的上级目录+对应每条视频名称 构成新的目录存放每个视频的
        os.makedirs(folder_name, exist_ok=True)  # 创建存放视频的对应目录
        vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
        c = 0  # 计数  统计对应帧号
        rval = vc.isOpened()  # 判断视频是否打开  返回True或Flase

        while rval:  # 循环读取视频帧
            rval, frame = vc.read()  # videoCapture.read() 函数，第一个返回值为是否成功获取视频帧，第二个返回值为返回的视频帧：
            pic_path = folder_name + '/'
            if rval:
                cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                cv2.waitKey(1)  # waitKey()--这个函数是在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环)
                c = c + 1
            else:
                break
        vc.release()
        print('save_success' + folder_name)


save_img()


def save_img2():  # 提取视频中图片 按照每秒提取   间隔是视频帧率
    video_path = "输入视频所在路径"  # 视频所在的路径
    f_save_path = "输入保存图片的文件夹"  # 保存图片的上级目录
    videos = os.listdir(video_path)  # 返回指定路径下的文件和文件夹列表。
    for video_name in videos:  # 依次读取视频文件
        file_name = video_name.split('.')[0]  # 拆分视频文件名称 ，剔除后缀
        folder_name = f_save_path + file_name  # 保存图片的上级目录+对应每条视频名称 构成新的目录存放每个视频的
        os.makedirs(folder_name, exist_ok=True)  # 创建存放视频的对应目录
        vc = cv2.VideoCapture(video_path + video_name)  # 读入视频文件
        fps = vc.get(cv2.CAP_PROP_FPS)  # 获取帧率
        print(fps)  # 帧率可能不是整数  需要取整
        rval = vc.isOpened()  # 判断视频是否打开  返回True或Flase
        c = 1
        while rval:  # 循环读取视频帧
            rval, frame = vc.read()  # videoCapture.read() 函数，第一个返回值为是否成功获取视频帧，第二个返回值为返回的视频帧：
            pic_path = folder_name + '/'
            if rval:

                if (c % round(fps) == 0):  # 每隔fps帧进行存储操作   ,可自行指定间隔
                    cv2.imwrite(pic_path + file_name + '_' + str(c) + '.jpg', frame)  # 存储为图像,保存名为 文件夹名_数字（第几个文件）.jpg
                cv2.waitKey(1)  # waitKey()--这个函数是在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环)
                c = c + 1
            else:
                break
        vc.release()
        print('save_success' + folder_name)


save_img2()