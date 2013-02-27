#!/usr/bin/python

from joblib import delayed, Parallel

hashes_per_job = 10000
min_job = 0
max_job = 2**32 / hashes_per_job


def verify(job_number):
	nonce_start = job_number * hashes_per_job
	nonce_end = nonce_start + hashes_per_job

	nonce = -1

	# redo the calculations locally here (using the python miner) to find the
	# right nonce

	return nonce


def dispatch(job_number):
	nonce_start = job_number * hashes_per_job
	nonce_end = nonce_start + hashes_per_job

	# generate the PS
	# send it to the printer
	# wait for response

	if promising_result:
		return True
	else:
		return False

# parallel out
results = Parallel(n_jobs=10)(delayed(dispatch)(i) for i in xrange(max_job))

# verify the promising results
for i in [ n for n,v in enumerate(results) if v == True ]:
	n = verify(i)
	if n != -1:
		print "NONCE FOUND: ", n
