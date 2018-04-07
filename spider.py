import os
import urllib2


class Spider:
    base_url = ''
    save_dir = './'

    def __init__(self, base_url, save_dir="./"):
        self.base_url = base_url
        self.save_dir = save_dir
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

    # to get the web page, default using relative path
    def get_page(self, page_url, is_complete=False):
        url = page_url if is_complete else self.base_url + page_url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read()

    # to downloadd the file, default using relative path
    # save_path should contain the file's name
    def get_file(self, file_name, file_url, is_complete=False):
        url = file_url if is_complete else self.base_url + file_url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        data = response.read()
        save_path = self.save_dir + file_name
        fd = open(save_path, 'wb')
        fd.write(data)
        fd.close()
        print("success:[%s]" % url)
