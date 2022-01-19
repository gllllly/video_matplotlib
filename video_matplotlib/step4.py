import cv2

# step4 将matplotlib图重新合成为视频
# 如果在这一步出错大概率是图片尺寸和视频尺寸不符的问题 回头检查一遍参数 基本上就可以解决问题
def main():
    fps = 29.92  # 视频帧率
    size = (640, 480)  # 需要转为视频的图片的尺寸
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter("视频输出路径", fourcc, fps, (640, 480), True)

    for i in range(1, 2776):   # 图片数量
        image_path = "matplotlib图输出路径" + str(i) +".jpg"
        print(image_path)
        img = cv2.imread(image_path)
        video.write(img)

    video.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()