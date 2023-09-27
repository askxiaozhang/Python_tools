import string
import imageio
import os
import cv2
import shutil
import base64
import random

def video_to_image(videoPath,imgPath,save_format = '.jpg',imgNumber = 0,nameLength = 4):
    '''
    params:
        videoPath : 视频路径 例如  u'E:\Test/123.mp4'
        imgPath : 图片路径 例如 r'F:\Test/tu/'      #保存图片路径,路径最后加/斜杠
        save_format : 保存的图片格式，默认为jpg可以改为'.png'
        imgNumber : 图片保存的名字数量默认为0开始
    '''
    print("视频转图片的方法")
    if imgPath[-1] != '/':imgPath + '/'
    capture = cv2.VideoCapture(videoPath)
    frame_num = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    suc = capture.isOpened()  # 是否成功打开
    frame_count = imgNumber  # 图片张数从多少开始
    while suc:
        try:
           frame_count += 1
           suc, frame = capture.read()
           cv2.imwrite(imgPath + str(frame_count).zfill(4) + save_format, frame)
           # zfill() 方法返回指定长度的字符串,原字符串右对齐,前面填充0
           #:str.zfill(width) 参数width
           if frame_num == frame_count:
               suc = False
        except:
            break
    capture.release()
    print("视频转图片结束! ")

def image_to_gif(st_imagename=1,end_imagename=1,gifname = "demo.gif"):
    import imageio
    '''
    uri：合成后的gif动图的名字，可以随意更改。
    mode：操作模式，I表示多图，不用更改。
    fps：帧率，也就是画面每秒传输帧数，值越大，gif动图的播放速度越大。
    gifname:保存的gif名字
    '''
    os.chdir(os.getcwd())
    if not os.path.exists("images"):
        os.makedirs("images")

    with imageio.get_writer(uri = gifname,mode = "I",fps = 25) as writer:
        for i in range(st_imagename, end_imagename + 1): #选择多少张
            print(f"正在处理第{i}张")
            filename =  str(i).zfill(4)
            file_path = os.path.join(os.getcwd(),'images',filename)
            writer.append_data(imageio.imread(file_path+".jpg"))
def video_to_gif(videoPath,resultName,fps=25):
    '''
    :param videoPath: 视频路径 绝对路径。且路径不要含中文
    :param resultName: 输出的gif文件名
    :param fps: 保存的gif帧率，fps默认为25
    '''
    sample = [chr(i) for i in range(97,97+26)] + [str(i) for i in range(10)]
    random_name = "_" + "".join(random.sample(sample,10)) #用于临时存储数据图片
    #shutil.rmtree(file_path) #删除
    if not os.path.exists(random_name):
        os.makedirs(random_name)
    tmp_path = os.path.join(os.getcwd(),random_name) + '/'
    print("step 1 loading:video_to_image start")
    video_to_image(videoPath,tmp_path) #视频转化完毕
    print("step 1 finished:video_to_image end")
    image_nums = len(os.listdir(tmp_path))
    image_nums = 375 if image_nums > 375 else image_nums #TODO 默认上限为15s 即：25 * 15 = 375张照片
    print("step 2 loading:image_to_gif start")
    image_to_gif(st_imagename=1,end_imagename=image_nums,gifname = resultName)
    print("step 2 finished:image_to_gif end")
    shutil.rmtree(random_name)
    print("All Finished")

if __name__ == '__main__':
    video_to_gif(r"E:\Python_tools\Python_tools\video\test.mp4","test1.gif")