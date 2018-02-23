## Reviewer Submission Requests

Udacity reviewer submission requests details


### Installation

```
git clone https://github.com/sksq9/ur-submission-requests
cd ur-submission-requests
pip install -r requirements.txt
```

### Run

```shell
python getrequest.py -T [your-reviewer-auth-token]
>>> 
2316007
        2018-02-23 23:57   an hour ago
        2018-02-24 00:43   6 minutes ago
        2018-02-24 12:43   in 11 hours
2315866
        2018-02-23 23:19   an hour ago
        2018-02-24 00:33   16 minutes ago
        2018-02-24 12:33   in 11 hours
2315690
        2018-02-23 22:38   2 hours ago
        2018-02-24 00:38   11 minutes ago
        2018-02-24 12:38   in 11 hours
2312758
        2018-02-23 07:32   17 hours ago
        2018-02-24 00:48   a minute ago
        2018-02-24 12:48   in 11 hours
2310748
        2018-02-22 21:57   a day ago
        2018-02-24 00:28   21 minutes ago
        2018-02-24 12:28   in 11 hours
```

An example response above, with fields `created_at`, `updated_at`, `closing_in` respectively. 
