import re
from spider import Spider
import threading

# the patten to extract file id from the HTML context
s_pattern_pdf = r'<span class="list-identifier">.*?\[<a href="/pdf/(.*?)" title="Download PDF">pdf</a>'
base_url = 'https://arxiv.org'
# skip means the offset, show means how many entries per page
page_url = 'list/cs/1801?skip=0&show=1000'
save_dir = './pdfs/'
task_list = []
task_list_lock = threading.Lock()
worker_num = 50


class Worker(threading.Thread):
    def __init__(self, thread_id, thread_name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.thread_name = thread_name

    def run(self):
        while True:
            task_list_lock.acquire()
            if len(task_list) == 0:
                task_list_lock.release()
                break
            file_id = task_list[0]
            task_list.pop(0)
            task_list_lock.release()
            file_name = file_id + ".pdf"
            file_url = '/pdf/' + file_id
            spider.get_file(file_name, file_url)


if __name__ == '__main__':
    spider = Spider(base_url, save_dir)
    page = spider.get_page(page_url)
    pattern_pdf = re.compile(s_pattern_pdf, re.S)
    # get all the file id
    task_list = re.findall(pattern_pdf, page)
    workers = []
    if task_list:
        for index in range(1, worker_num):
            worker = Worker(index, "Thread-%d" % index)
            worker.start()
            workers.append(worker)
        for worker in workers:
            worker.join()
        print("All tasks finished! Exiting Main Thread")
    else:
        print('match failed:[%s]' % s_pattern_pdf)
