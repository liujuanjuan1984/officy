import os
import pytesseract
from PIL import Image


class Img:
    """图片识别为文本数据"""

    def __init__(self, filepath=None):
        self.filepath = filepath

    def imginfo(self):
        img = Image.open(self.filepath)
        return {
            "filepath": self.filepath,
            "format": img.format,
            "size": img.size,
        }

    def imgdata(self):
        imgdata = self.imginfo()
        imgdata["content"] = self.get_img_content
        return imgdata

    def get_img_content(self):
        try:
            img = Image.open(self.filepath)
            content = pytesseract.image_to_string(img)
        except Exception as e:
            print(e)
            content = "未能读取成功"
        return content

    def get_size(self, infile=""):
        # 获取文件大小:KB
        if infile == "":
            infile = self.filepath
        size = os.path.getsize(infile)
        return size / 1024

    def get_outfile(self, outfile):
        """拼接输出图片的地址"""
        if outfile:
            return outfile
        dir, suffix = os.path.splitext(self.filepath)
        outfile = "{}-out{}".format(dir, suffix)
        return outfile

    def compress_image(self, outfile="", mb=198, step=10, quality=80):
        """不改变图片尺寸压缩到指定大小
        :param infile: 压缩源文件
        :param outfile: 压缩文件保存地址
        :param mb: 压缩目标，KB
        :param step: 每次调整的压缩比率
        :param quality: 初始压缩比率
        :return: 压缩文件地址，压缩文件大小
        """
        infile = self.filepath
        o_size = self.get_size()
        if o_size <= mb:
            return infile
        outfile = self.get_outfile(outfile)
        while o_size > mb:
            im = Image.open(infile)
            im.save(outfile, quality=quality)
            if quality - step < 0:
                break
            quality -= step
            o_size = get_size(outfile)
        return outfile
