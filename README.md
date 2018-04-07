# arXiv-Spider
A Web Spider - to crawl papers on arXiv by specify the submission  date

You can change the configuration in main.py

Belows are the variables and their explanations you may concern:
- `SAVE_DIR`: the path to save the crawled files
- `WORKER_NUM`: the total number of the threads(workers) 
- `BEGIN_YEAR`、`BEGIN_MONTH`、`END_YEAR`、`END_MONTH`:
With the default configuration, it can crawl the papers with submission dates from January 2015 to March 2018


Tips: When you meet the 403 error or "Access Denied" error, don't worry. It means the download speed was so fast that the system has detected our crawler. You should be patient, and try again a few minutes later.