import imageio
import os
import cv2

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
       frame_count += 1
       suc, frame = capture.read()
       cv2.imwrite(imgPath + str(frame_count).zfill(4) + save_format, frame)
       # zfill() 方法返回指定长度的字符串,原字符串右对齐,前面填充0
       #:str.zfill(width) 参数width
       if frame_num == frame_count:
           suc = False
    capture.release()
    print("视频转图片结束! ")

def image_to_gif(st_imagename=1,end_imagename=1):
    import imageio
    '''
    uri：合成后的gif动图的名字，可以随意更改。
    mode：操作模式，I表示多图，不用更改。
    fps：帧率，也就是画面每秒传输帧数，值越大，gif动图的播放速度越大。
    '''
    gifname = "demo.gif" #TODO 这里修改为保存到 gif文件名
    with imageio.get_writer(uri = gifname,mode = "I",fps = 25) as writer:
        for i in range(st_imagename, end_imagename + 1): #选择多少张
            filename =  str(i).zfill(4)
            file_path = os.path.join(os.getcwd(),'images',filename)
            writer.append_data(imageio.imread(file_path+".jpg"))

if __name__ == '__main__':
    image_to_gif(st_imagename=1,end_imagename=25)