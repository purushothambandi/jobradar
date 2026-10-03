from jobradar.models import Job
def test_job_strips_whitespace():
    job = Job("1","Python Dev ", " Acme ", "Hyderabad", "desc", "http://x.com")
    assert job.title == "Python Dev"
    assert job.company== "Acme"