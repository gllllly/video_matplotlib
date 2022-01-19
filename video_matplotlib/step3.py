from PIL import Image
import matplotlib.pyplot as plt

# step3 将线稿转成matplotlib图
# 因为这步转化速度非常慢，所以建议分批处理
for i in range(2758, 2776):   # 分批处理
    image_path = "线稿路径" + str(i) +".jpg"
    fig_save_path = "matplotlib图输出路径" + str(i) +".jpg"

    im = Image.open(image_path)
    rgb_im = im.convert('RGB')

    '''以下两个list是需要调整的，选取图片中最多的点的rgb数值
    我猜测这里先使用使用二值化，再找其中(0,0,0)的点也是可以的，而且可以加快效率
    后续960、240等参数也是需要根据图片具体大小调整的
    可以多用debug看看'''

    list = [164, 208, 11, 139, 97, 40]
    list2 = [70, 2, 60, 10, 73, 72, 0, 52, 64, 62, 21, 17]
    data_x = []
    data_y = []
    for j in list2:
        color = (j, j, j)
        for x in range(rgb_im.size[0]):
            for y in range(rgb_im.size[1]):
                r, g, b = rgb_im.getpixel((x, y))
                if (r,g,b) == color:
                    y = 960 - y

                    data_x.append(x)
                    data_y.append(y)

    # print(X)
    # print(Y)
    plt.scatter(data_x, data_y, s=1)
    plt.xlim((0, 960))
    plt.ylim((240, 960))
    plt.savefig(fig_save_path)
    # plt.show()
    plt.clf()

    data_x = []
    data_y = []

    print(i, "ok")

print("all,ok")